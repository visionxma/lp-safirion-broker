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

- **Os preços do mural de ativos são ilustrativos**, não são cotações reais.
  A série de cada sparkline é determinística (derivada do índice do ativo), então
  o mural desenha igual em todo carregamento. Para dados reais, trocar o array
  `MURAL` no bloco `kv-mural-js` por um fetch da API de mercado.
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
