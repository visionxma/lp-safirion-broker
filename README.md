# Safirion Broker — Landing Page

Landing page da **Safirion**, corretora digital para operar Forex, criptomoedas
e ações globais em uma única plataforma.

Site estático, **100% offline**: fontes, ícones, scripts e imagens são todos
locais em `_ext/`. Não há build — é só servir a pasta.

## Estrutura

```
.
├── src/index.html      # FONTE em português — edite só aqui
├── scripts/
│   ├── gerar.py        # gera /pt/ /en/ /es/ /fr/ a partir da fonte
│   ├── i18n.py         # catálogo de traduções
│   ├── blog.py         # gera /blog/
│   └── artigos.py      # conteúdo dos artigos
├── wrangler.jsonc
└── public/             # SÓ arquivos gerados — é o que vai para o ar
    ├── pt/ en/ es/ fr/
    ├── blog/
    ├── 404.html  robots.txt  sitemap.xml
    ├── _headers        # cache e cabeçalhos de segurança
    ├── _redirects      # preserva as URLs antigas do safirion.com
    └── _ext/           # fontes, imagens e ícones
```

## Rodar localmente

```sh
cd public && python3 -m http.server 8123
```

## Publicar

```sh
wrangler deploy
```

## Notas

- **O mural usa cotações reais**, vindas de `/api/cotacoes` e atualizadas a cada
  minuto. Os valores no array `MURAL` são só o estado inicial, exibido enquanto
  a requisição não volta e como reserva se a fonte falhar. Já as sparklines
  continuam ilustrativas: são uma série determinística derivada do índice do
  ativo, não o histórico real.
- A base foi um export do Framer "de-hidratado" (sem JS remoto). Os blocos com
  `id="kv-*"` são código próprio — buscar por `kv-` para navegar.
- O CSS do Framer é minificado e não comentável internamente.

## Idiomas

A página existe em quatro idiomas. **O português é a fonte** — edite apenas
`public/index.html` e regenere os outros três:

```sh
python3 scripts/gerar.py public https://safirion.com
python3 scripts/blog.py  public https://safirion.com
```

| Idioma | URL | Arquivo |
|---|---|---|
| Português | `/pt/` | gerado |
| English | `/en/` | gerado |
| Español | `/es/` | gerado |
| Français | `/fr/` | gerado |

O gerador é idempotente: limpa o que injetou antes de injetar de novo, então
pode rodar quantas vezes quiser. As traduções ficam em `scripts/i18n.py` —
strings ausentes do catálogo permanecem em português de propósito (nomes
próprios, tickers, e-mail e os endereços societários).

Ele também cuida de: `hreflang` recíproco entre os quatro + `x-default`,
`canonical` próprio por idioma, `lang` do `<html>`, `og:locale`, tradução dos
`alt` das imagens e conversão dos caminhos de assets para absolutos (as páginas
traduzidas vivem em subpasta).

## Blog

Fica fora da landing de propósito: a home trabalha conversão, o blog trabalha
busca. Cada artigo é uma porta de entrada própria, com `title`, `description`,
`canonical` e JSON-LD `Article` dele.

```sh
python3 scripts/blog.py public https://safirion.com
```

O conteúdo mora em `scripts/artigos.py` — para publicar um artigo novo, some
uma entrada na lista `ARTIGOS` e rode o comando. O índice, o JSON-LD e os cards
são montados a partir dela.

Os artigos miram busca de cauda longa (menos volume, intenção clara, menos
concorrência), que é onde um domínio novo tem chance real de aparecer. Como é
conteúdo financeiro — YMYL para o Google — o texto evita promessa de retorno,
atribui os números da Safirion à fonte e fecha com aviso de risco.

## Migração do safirion.com

Este site substitui o safirion.com. O site antigo tinha URLs já indexadas, e
`public/_redirects` existe para não perdê-las:

| URL antiga | Destino | Motivo |
|---|---|---|
| `/` | `/pt/` (301) | a raiz servia com canonical para `/en/`; aqui o público é Brasil |
| `/terms.html` | PDF de Termos e Condições | página existia e respondia 200 |
| `/legal/terms/` | PDF de Termos e Condições | idem |
| `/legal/privacy/` | PDF de Política de Cookies | **provisório** — ver abaixo |

O português ficou em `/pt/`, e não na raiz, porque essa URL **já está indexada**
no safirion.com. Movê-la para `/` criaria um 404 na página que tem histórico.

⚠️ `/legal/privacy/` aponta para a Política de Cookies por falta de um documento
de privacidade nos materiais da Safirion. Substituir quando houver.

## Camada de dados (`worker/index.js`)

O site é estático, mas o Worker expõe dois endpoints com cache:

| Rota | Fonte | Cache |
|---|---|---|
| `/api/cotacoes` | Yahoo Finance | 60 s |
| `/api/noticias` | RSS do InfoMoney e Investing.com | 15 min |

Nenhuma exige chave. O cache existe porque sem ele cada visita bateria na fonte.

**Por que só o Yahoo para cotação:** CoinGecko, Binance e Frankfurter funcionam
no terminal mas bloqueiam ou limitam IPs de datacenter — voltavam vazias em
produção. O Yahoo foi a única que respondeu do Worker. É endpoint não oficial,
então pode mudar sem aviso: cada símbolo é buscado isolado e uma falha não
derruba os outros. Se um dia parar, o mural cai no estado inicial do array.

**Notícias são curadoria, não republicação:** título, fonte e link para o
original, com `rel="nofollow"`. Republicar matéria seria problema de direito
autoral, e o Google prefere a fonte.

⚠️ **Calendário econômico ficou de fora.** As fontes gratuitas devolvem 429 para
IP de Worker (ForexFactory via faireconomy) ou encerraram a conta de teste
(Trading Economics). Precisa de provedor com chave. Quando houver, o caminho é
um cron gravando em KV — a rota não pode buscar por visita.

## Capas do blog (`scripts/capas.py`)

```sh
python3 scripts/capas.py public http://127.0.0.1:8125
```

Desenha a capa de cada artigo em HTML/SVG e rasteriza com o Chrome headless.
Sem banco de imagens: evita custo de licença e a mesma foto genérica que todo
site de corretora usa. O motivo conversa com o assunto — velas para spread,
escudo para regulamentação, barras para capital.

**As capas não têm texto.** O título já está no HTML; embutido na imagem ele
seria cortado em qualquer recorte e apareceria duas vezes no card. Cada uma
pesa 8–16 KB.

Precisa do servidor local rodando, porque a capa carrega a logo e as fontes
por caminho absoluto.

## Páginas legais

`/legal/terms/`, `/legal/privacy/` e `/terms.html` foram trazidas do safirion.com
antigo e reestilizadas no sistema visual do blog. O texto legal foi preservado
sem alteração; só o invólucro mudou. Antes redirecionavam para os PDFs, o que
jogava fora conteúdo indexável (13.272 e 7.153 palavras).

⚠️ **Divergência societária a resolver.** O rodapé do safirion.com diz
SUNSET HORIZON LLC (Reg. L 22994); as páginas legais e o PDF oficial de Termos
dizem THUNDER FLASH LLC (Reg. L 22853). São empresas e registros diferentes —
o rodapé deste site ainda usa SUNSET HORIZON, copiado do site antigo. Precisa de
confirmação de qual é a entidade vigente.
