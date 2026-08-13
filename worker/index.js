/**
 * Worker do safirion.com
 *
 * Serve os arquivos estáticos de public/ e expõe três endpoints de dados:
 *
 *   /api/cotacoes  cripto, câmbio, ações, commodities e índices
 *   /api/noticias  manchetes com link para a fonte
 *
 * Nenhuma fonte exige chave de API, então não há segredo para guardar. O que
 * existe aqui é cache: sem ele cada visita bateria nas fontes, o que estoura
 * limite e deixa a página lenta. As respostas ficam no cache da Cloudflare e
 * são compartilhadas entre todos os visitantes daquele PoP.
 */

const TTL = {
  cotacoes: 60,        // 1 min — preço muda o tempo todo
  noticias: 900,       // 15 min
};

const json = (dados, segundos) =>
  new Response(JSON.stringify(dados), {
    headers: {
      'content-type': 'application/json; charset=utf-8',
      'cache-control': `public, max-age=${segundos}, s-maxage=${segundos}`,
      'access-control-allow-origin': '*',
    },
  });

/* Busca com prazo: fonte lenta não pode segurar a resposta da página. */
async function buscar(url, ms = 6000) {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), ms);
  try {
    const r = await fetch(url, {
      signal: ctrl.signal,
      headers: { 'user-agent': 'Mozilla/5.0 (compatible; SafirionBot/1.0)' },
      cf: { cacheTtl: 45, cacheEverything: true },
    });
    if (!r.ok) return null;
    return r;
  } catch {
    return null;
  } finally {
    clearTimeout(t);
  }
}

/* ------------------------------------------------------------------ cotações */


/* Yahoo Finance: endpoint não oficial, sem chave. Ficou como fonte única de
   cotação porque foi a que respondeu a partir do Worker — CoinGecko e Binance
   funcionam no terminal mas bloqueiam IP de datacenter, e voltavam vazias em
   produção. Como não é API oficial, pode mudar sem aviso: cada símbolo é
   buscado isolado e uma falha não derruba os outros. */
const YAHOO = {
  /* cripto */
  'BTC': 'BTC-USD', 'ETH': 'ETH-USD', 'XRP': 'XRP-USD', 'SOL': 'SOL-USD',
  'ADA': 'ADA-USD', 'DOGE': 'DOGE-USD', 'DOT': 'DOT-USD', 'LINK': 'LINK-USD',
  'BNB': 'BNB-USD', 'LTC': 'LTC-USD', 'XLM': 'XLM-USD', 'XMR': 'XMR-USD',
  'MATIC': 'MATIC-USD',
  /* ações */
  'TSLA': 'TSLA', 'NVDA': 'NVDA', 'AAPL': 'AAPL', 'META': 'META', 'NFLX': 'NFLX',
  /* commodities e índice */
  'XAU': 'GC=F', 'WTI': 'CL=F', 'SPX': '^GSPC',
};

async function cotacoes(env) {
  const saida = {};


  /* câmbio — Frankfurter serve as taxas de referência do BCE */
  const rf = await buscar('https://api.frankfurter.app/latest?from=EUR&to=USD,GBP,JPY');
  const ro = await buscar('https://api.frankfurter.app/latest?from=GBP&to=USD');
  if (rf) {
    const d = await rf.json();
    if (d.rates?.USD) saida['EURUSD'] = { preco: d.rates.USD, variacao: 0 };
    if (d.rates?.JPY) saida['USDJPY'] = { preco: d.rates.JPY / (d.rates.USD || 1), variacao: 0 };
  }
  if (ro) {
    const d = await ro.json();
    if (d.rates?.USD) saida['GBPUSD'] = { preco: d.rates.USD, variacao: 0 };
  }

  /* USDT é lastro em dólar: fixo por definição */
  saida['USDT'] = { preco: 1, variacao: 0 };

  /* cripto, ações, commodities e índice — todos pelo mesmo endpoint */
  await Promise.all(Object.entries(YAHOO).map(async ([cod, sym]) => {
    const r = await buscar(
      `https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(sym)}?interval=1d&range=2d`
    );
    if (!r) return;
    try {
      const m = (await r.json())?.chart?.result?.[0]?.meta;
      if (m?.regularMarketPrice == null) return;
      const ant = m.chartPreviousClose || m.previousClose || m.regularMarketPrice;
      saida[cod] = {
        preco: m.regularMarketPrice,
        variacao: ant ? ((m.regularMarketPrice - ant) / ant) * 100 : 0,
      };
    } catch { /* símbolo isolado falha sem derrubar os outros */ }
  }));

  return { atualizado: new Date().toISOString(), ativos: saida };
}

/* O calendário econômico ficou de fora: as fontes gratuitas (ForexFactory via
   faireconomy) devolvem 429 para IP de Worker, e Trading Economics encerrou a
   conta de demonstração. Precisa de provedor com chave — quando houver, o
   caminho é um cron gravando em KV, porque a rota não pode buscar por visita. */

/* ----------------------------------------------------------------- notícias */

/* Só título, resumo curto e link para a fonte. Não republicamos matéria:
   isso seria problema de direito autoral e o Google prefere o original. */
const FEEDS = [
  { url: 'https://www.infomoney.com.br/feed/', fonte: 'InfoMoney' },
  { url: 'https://br.investing.com/rss/news_25.rss', fonte: 'Investing.com' },
];

function tag(bloco, nome) {
  const m = bloco.match(new RegExp(`<${nome}[^>]*>([\\s\\S]*?)</${nome}>`, 'i'));
  if (!m) return '';
  return m[1]
    .replace(/<!\[CDATA\[([\s\S]*?)\]\]>/g, '$1')
    .replace(/<[^>]+>/g, '')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&quot;/g, '"')
    .replace(/&#39;|&apos;/g, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/\s+/g, ' ')
    .trim();
}

async function noticias(env) {
  const listas = await Promise.all(FEEDS.map(async f => {
    const r = await buscar(f.url, 7000);
    if (!r) return [];
    const xml = await r.text();
    const itens = xml.split(/<item[\s>]/i).slice(1, 9);
    return itens.map(b => {
      const titulo = tag(b, 'title');
      const link = tag(b, 'link');
      if (!titulo || !link) return null;
      const resumo = tag(b, 'description');
      return {
        titulo,
        link,
        fonte: f.fonte,
        data: tag(b, 'pubDate') || null,
        resumo: resumo.length > 160 ? resumo.slice(0, 157).trimEnd() + '…' : resumo,
      };
    }).filter(Boolean);
  }));

  /* intercala as fontes para nenhuma dominar a lista */
  const saida = [];
  for (let i = 0; i < 8; i++) {
    for (const l of listas) if (l[i]) saida.push(l[i]);
  }
  return { atualizado: new Date().toISOString(), noticias: saida.slice(0, 12) };
}

/* --------------------------------------------------------------------- rota */

const ROTAS = {
  '/api/cotacoes': [cotacoes, TTL.cotacoes],
  '/api/noticias': [noticias, TTL.noticias],
};

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const rota = ROTAS[url.pathname.replace(/\/$/, '')];

    if (!rota) return env.ASSETS.fetch(request);

    const [fn, ttl] = rota;
    const cache = caches.default;
    const chave = new Request(url.toString(), { method: 'GET' });

    const guardado = await cache.match(chave);
    if (guardado) return guardado;

    let resposta;
    try {
      resposta = json(await fn(env), ttl);
    } catch (e) {
      /* fonte fora do ar não pode virar erro na página: devolve vazio e o
         cliente mantém o que já tinha na tela */
      return json({ erro: true, atualizado: new Date().toISOString() }, 30);
    }
    ctx.waitUntil(cache.put(chave, resposta.clone()));
    return resposta;
  },
};
