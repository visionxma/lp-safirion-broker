# Subir para o cPanel

O site foi feito para Cloudflare Workers. cPanel é Apache, e três coisas do
Cloudflare não existem lá. Este guia cobre a tradução.

Para gerar a pasta:

```sh
python3 scripts/cpanel.py
```

Saem duas coisas, ambas fora do versionamento:

| | O que é |
|---|---|
| `dist-cpanel/` | o conteúdo exato do `public_html` |
| `safirion-cpanel.zip` | o mesmo, para subir e extrair no File Manager |

## O que vai

```
public_html/
├── .htaccess          ← redirects, cabeçalhos e a rota /api/*
├── 404.html
├── robots.txt
├── sitemap.xml
├── site.webmanifest
├── terms.html
├── _ext/              ← fontes, imagens e ícones (+ .htaccess de cache)
├── api/               ← cotacoes.php, noticias.php, _http.php
├── blog/
├── legal/
└── pt/  en/  es/  fr/
```

O site só depende de `/_ext/`, `/blog/`, `/legal/`, `/pt/`, `/en/`, `/es/`,
`/fr/` e dos arquivos da raiz. Nada mais.

## O que muda em relação ao Cloudflare

**`_redirects` → `.htaccess`.** As regras 301 viraram `RewriteRule`. São as
que preservam as URLs já indexadas: `/` → `/pt/` e as variantes sem barra
final. **Não suba `_redirects` nem `_headers`** — o Apache não os lê, e eles
ficariam expostos na raiz do site.

**`_headers` → `.htaccess` + `_ext/.htaccess`.** Cache de um ano nos assets,
revalidação no HTML, mais `X-Content-Type-Options` e `Referrer-Policy`.

**O Worker → PHP.** `worker/index.js` servia `/api/cotacoes` e `/api/noticias`.
Viraram `api/cotacoes.php` e `api/noticias.php`, com as mesmas fontes, o mesmo
formato de resposta e o mesmo TTL. O que mudou foi a infraestrutura: o cache da
Cloudflare virou arquivo em `sys_get_temp_dir()`, e o `Promise.all` virou
`curl_multi`. O `.htaccess` reescreve `/api/cotacoes` para `/api/cotacoes.php`,
então a URL que o navegador vê continua a mesma.

## Como subir (extrair dentro do `public_html`)

**Extrair um zip mescla, não substitui.** Arquivo que existe nos dois é
sobrescrito; arquivo que só existe no servidor **fica**. Por isso a ordem
importa.

### 1. Faça backup primeiro

No File Manager, entre em `public_html`, **Select All** → **Compress** →
`backup-antes-safirion.zip`. Baixe o arquivo antes de continuar. Sem isso não
há como voltar atrás.

### 2. Apague o que vai ser trocado

Antes de extrair, apague estas pastas e arquivos. Extrair por cima sem apagar
deixa os arquivos do site antigo lá dentro, e eles continuam sendo servidos:

```
_ext/   blog/   en/   es/   fr/   legal/   pt/   404.html
```

**⚠️ `api/` é o único que não dá para eu decidir por você.** A pasta nova traz
três `.php`. Olhe o que há na atual: se for do site antigo e nada mais usar,
apague; se algo ainda depender, extraia por cima e confira depois.

**Sobras do site antigo, que o site novo não usa:** `assets/`, `css/`, `js/`,
`ziplanguage/`, `404.shtml`. Verifiquei que nenhum arquivo do site novo aponta
para elas — ele só pede `/_ext/`, `/blog/`, `/legal/`, `/pt/`, `/en/`, `/es/`,
`/fr/` e os arquivos da raiz. Ainda assim, confira se nada externo depende.

**Lixo de upload:** `__MACOSX/` e `__MACOSX.zip` (31,81 MB). Resíduo de zip
feito no Mac.

**Não toque:** `cgi-bin/`, do cPanel.

### 3. Suba e extraia

Upload de `safirion-cpanel.zip` dentro de `public_html` → **Extract**. O zip não
tem pasta-invólucro: o conteúdo cai direto na raiz, que é o que você quer.

### 4. Ligue "Show Hidden Files"

**Settings → Show Hidden Files (dotfiles).** Sem isso o File Manager não mostra
os `.htaccess`, e são eles que fazem os redirects e os cabeçalhos funcionarem.
Confirme que chegaram os três:

```
public_html/.htaccess
public_html/_ext/.htaccess
public_html/api/.htaccess
```

### 5. Apague o zip do servidor

Deixá-lo lá expõe uma cópia do site inteiro em
`safirion.com/safirion-cpanel.zip`.

## Uma URL só, não quatro

Antes desta versão o mesmo conteúdo respondia em quatro endereços — com e sem
`www`, em `http` e em `https`. O canonical apontava todos para
`https://safirion.com/`, mas o Google escolhe o que rastreia: escolheu
`http://www.safirion.com`, e é por isso que o resultado de busca ainda mostrava
o título antigo do site.

O `.htaccess` agora manda `www` para o apex preservando o esquema. Preserva de
propósito: redirecionar para `https` antes do certificado estar ativo deixaria o
`www` fora do ar.

**Depois de confirmar o AutoSSL no cPanel**, troque o bloco ativo pelo que está
comentado logo abaixo dele — aí `http://www.safirion.com` vira
`https://safirion.com` num salto só, em vez de dois.

Isso não desfaz o que já está indexado. Para acelerar, use o Search Console:
Inspeção de URL → Solicitar indexação. É mais um motivo para instalar a tag de
verificação, que continua pendente.

## Verificar depois de subir

```sh
curl -sI https://safirion.com/           | head -2   # 301 para /pt/
curl -sI https://safirion.com/pt         | head -2   # 301 para /pt/
curl -sI https://safirion.com/pt/        | head -2   # 200
curl -sI https://safirion.com/nao-existe | head -2   # 404
curl -sI https://safirion.com/_ext/img/og-image.jpg | grep -i cache   # 1 ano

# o teste que mais importa: tem de vir JSON, nunca "<?php"
curl -s https://safirion.com/api/cotacoes | head -c 120
curl -s https://safirion.com/api/noticias | head -c 120
```

Se `/api/cotacoes` responder com `<?php`, o PHP não está processando a pasta e o
**código está sendo servido como texto**. Não há segredo ali dentro (as fontes
não usam chave), mas apague a pasta `api/` na hora: o site continua de pé, só
com o mural em valores fixos.

## Se o PHP não funcionar

**O PHP não pôde ser testado aqui** — a máquina onde ele foi escrito não tem
PHP nem Docker instalados. Ele foi escrito para falhar em silêncio: qualquer
erro devolve JSON válido com `erro: true`, nunca uma página de erro do PHP (que
quebraria o parse no navegador).

Se os endpoints não responderem, o site **continua funcionando**, degradado:

- o mural de cotações mostra os valores iniciais que já estão no HTML, fixos
- o bloco de manchetes do blog fica vazio

Requisitos: PHP 7.4 ou mais novo, com `curl` e permissão de saída HTTP. Se o
`curl_multi` não existir, os endpoints devolvem `erro: true` em vez de quebrar.

## Uma consequência boa da mudança

No Cloudflare, `/terms.html` respondia 307 e redirecionava para `/terms`, por
causa do `html_handling: auto-trailing-slash`. O sitemap lista `/terms.html`,
então havia divergência. No Apache não há esse redirecionamento: a URL do
sitemap passa a responder 200 direto.
