# Safirion Broker — Landing Page

Landing page da **Safirion**, corretora digital para operar Forex, criptomoedas
e ações globais em uma única plataforma.

Site estático, **100% offline**: fontes, ícones, scripts e imagens são todos
locais em `_ext/`. Não há build — é só servir a pasta.

## Estrutura

```
.
├── wrangler.jsonc      # deploy na Cloudflare (Workers Static Assets)
└── public/             # ÚNICA pasta publicada
    ├── index.html      # página inteira (HTML + CSS + JS embutidos)
    ├── robots.txt
    ├── sitemap.xml
    ├── site.webmanifest
    └── _ext/
        ├── fonts/      # Mazzard (4 pesos, .ttf)
        ├── img/        # fundo do hero e captura da plataforma
        └── icons/      # logo, favicon, mapa-múndi e ícones dos ativos
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
python3 scripts/gerar.py public https://lp-safirion-broker.visionxma.workers.dev
```

| Idioma | URL | Arquivo |
|---|---|---|
| Português (padrão) | `/` | `public/index.html` |
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
