<?php
/**
 * Porte de /api/cotacoes (worker/index.js) para PHP.
 *
 * Mesmas fontes, mesmo formato de resposta e mesmo TTL. O que muda e a
 * infraestrutura: no Worker o cache era o da Cloudflare, aqui e um arquivo em
 * sys_get_temp_dir(); e o Promise.all virou curl_multi.
 *
 * Qualquer falha devolve JSON valido com erro:true — nunca uma pagina de erro
 * do PHP, que quebraria o parse no navegador e derrubaria o mural.
 */
declare(strict_types=1);
require __DIR__ . '/_http.php';

const SAFIRION_TTL = 60;

/* Yahoo Finance: endpoint nao oficial, sem chave. Ficou como fonte unica de
   cotacao porque foi a que respondeu — CoinGecko e Binance bloqueiam IP de
   datacenter. Cada simbolo e buscado isolado: uma falha nao derruba os outros. */
$YAHOO = [
    'BTC' => 'BTC-USD', 'ETH' => 'ETH-USD', 'XRP' => 'XRP-USD', 'SOL' => 'SOL-USD',
    'ADA' => 'ADA-USD', 'DOGE' => 'DOGE-USD', 'DOT' => 'DOT-USD', 'LINK' => 'LINK-USD',
    'BNB' => 'BNB-USD', 'LTC' => 'LTC-USD', 'XLM' => 'XLM-USD', 'XMR' => 'XMR-USD',
    'MATIC' => 'MATIC-USD',
    'TSLA' => 'TSLA', 'NVDA' => 'NVDA', 'AAPL' => 'AAPL', 'META' => 'META', 'NFLX' => 'NFLX',
    'XAU' => 'GC=F', 'WTI' => 'CL=F', 'SPX' => '^GSPC',
];

try {
    $guardado = safirion_cache_ler('cotacoes', SAFIRION_TTL);
    if ($guardado !== null) {
        safirion_responder($guardado, SAFIRION_TTL);
        exit;
    }

    $urls = [
        '__eur' => 'https://api.frankfurter.app/latest?from=EUR&to=USD,GBP,JPY',
        '__gbp' => 'https://api.frankfurter.app/latest?from=GBP&to=USD',
    ];
    foreach ($YAHOO as $cod => $sym) {
        $urls[$cod] = 'https://query1.finance.yahoo.com/v8/finance/chart/'
            . rawurlencode($sym) . '?interval=1d&range=2d';
    }

    $r = safirion_buscar($urls);
    $ativos = [];

    /* cambio — taxas de referencia do BCE via Frankfurter */
    if (!empty($r['__eur'])) {
        $d = json_decode($r['__eur'], true);
        $usd = $d['rates']['USD'] ?? null;
        $jpy = $d['rates']['JPY'] ?? null;
        if ($usd !== null) $ativos['EURUSD'] = ['preco' => $usd, 'variacao' => 0];
        if ($jpy !== null) $ativos['USDJPY'] = ['preco' => $jpy / ($usd ?: 1), 'variacao' => 0];
    }
    if (!empty($r['__gbp'])) {
        $d = json_decode($r['__gbp'], true);
        if (isset($d['rates']['USD'])) $ativos['GBPUSD'] = ['preco' => $d['rates']['USD'], 'variacao' => 0];
    }

    /* USDT e lastro em dolar: fixo por definicao */
    $ativos['USDT'] = ['preco' => 1, 'variacao' => 0];

    foreach ($YAHOO as $cod => $sym) {
        if (empty($r[$cod])) continue;
        $d = json_decode($r[$cod], true);
        $m = $d['chart']['result'][0]['meta'] ?? null;
        if (!is_array($m) || !isset($m['regularMarketPrice'])) continue;
        $preco = (float) $m['regularMarketPrice'];
        $ant   = (float) ($m['chartPreviousClose'] ?? $m['previousClose'] ?? $preco);
        $ativos[$cod] = [
            'preco'    => $preco,
            'variacao' => $ant ? (($preco - $ant) / $ant) * 100 : 0,
        ];
    }

    $json = json_encode(
        ['atualizado' => gmdate('Y-m-d\TH:i:s\Z'), 'ativos' => (object) $ativos],
        JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
    );
    if ($json === false) throw new RuntimeException('json_encode falhou');

    safirion_cache_gravar('cotacoes', $json);
    safirion_responder($json, SAFIRION_TTL);
} catch (Throwable $e) {
    /* fonte fora do ar nao pode virar erro na pagina: o mural mantem o estado
       inicial que ja esta na tela */
    safirion_responder(
        json_encode(['erro' => true, 'atualizado' => gmdate('Y-m-d\TH:i:s\Z')]),
        30
    );
}
