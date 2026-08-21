# -*- coding: utf-8 -*-
"""
Gera as versoes en / es / fr a partir do index.html em portugues.

Rode sempre que editar o index.html da raiz:
    python3 gerar.py <pasta public> <url base>

Assim as edicoes ficam num arquivo so e se propagam para os quatro idiomas.
"""
import io, os, re, sys, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n

PUB = sys.argv[1].rstrip('/')
URL = sys.argv[2].rstrip('/')
# a fonte fica fora de public/ para nao ser servida e duplicar o /pt/
FONTE = os.path.join(os.path.dirname(PUB), 'src', 'index.html')

TODOS = ['pt'] + i18n.IDIOMAS


# ---------------------------------------------------------------------------
def seletor(lang):
    """Capsula com o idioma atual e os links para os outros."""
    itens = ''
    for l in TODOS:
        ativo = ' aria-current="true"' if l == lang else ''
        # caminho relativo de proposito: funciona tanto no dominio de testes
        # quanto no definitivo. Absoluto levava para o site antigo enquanto o
        # DNS nao apontasse para ca.
        itens += ('<a class="kv-lang__op%s" href="%s" hreflang="%s" lang="%s"%s>%s</a>'
                  % (' is-on' if l == lang else '', i18n.CAMINHO[l],
                     i18n.META['lang_attr'][l], i18n.META['lang_attr'][l], ativo, i18n.NOMES[l]))
    return ('<div class="kv-lang"><button class="kv-lang__btn" type="button"'
            ' aria-haspopup="true" aria-expanded="false" aria-label="Idioma">'
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"'
            ' aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/>'
            '<path d="M12 3c2.4 2.6 2.4 15.4 0 18M12 3c-2.4 2.6-2.4 15.4 0 18"/></svg>'
            '<b>%s</b><i aria-hidden="true"></i></button>'
            '<div class="kv-lang__menu">%s</div></div>' % (i18n.CURTO[lang], itens))


CSS_LANG = ('<!-- [kv] Seletor de idioma. -->'
            '<style id="kv-lang-css">'
            '.kv-lang{position:relative;display:inline-flex;align-items:center;'
            'font-family:"Mazzard",sans-serif;flex:0 0 auto;margin-right:10px}'
            '.kv-lang__btn{display:inline-flex;align-items:center;gap:7px;padding:9px 12px;'
            'border:1px solid rgba(255,255,255,.16);border-radius:999px;background:rgba(255,255,255,.04);'
            'color:#fff;font:inherit;font-size:14px;font-weight:600;cursor:pointer;line-height:1}'
            '.kv-lang__btn:hover{border-color:rgba(35,137,230,.5);background:rgba(35,137,230,.10)}'
            '.kv-lang__btn svg{width:17px;height:17px;color:#4ba3f0;flex:0 0 auto}'
            '.kv-lang__btn i{width:0;height:0;border-left:4px solid transparent;'
            'border-right:4px solid transparent;border-top:5px solid #a1b8c3;margin-left:1px}'
            '.kv-lang__menu{position:absolute;top:calc(100% + 8px);right:0;min-width:158px;'
            'display:none;flex-direction:column;padding:6px;border-radius:14px;'
            'border:1px solid rgba(255,255,255,.12);background:#0a1120;'
            'box-shadow:0 18px 44px rgba(0,0,0,.55);z-index:60}'
            '.kv-lang.is-open .kv-lang__menu{display:flex}'
            '.kv-lang__op{padding:10px 12px;border-radius:9px;color:#a1b8c3;text-decoration:none;'
            'font-size:14px;white-space:nowrap}'
            '.kv-lang__op:hover{background:rgba(255,255,255,.06);color:#fff}'
            '.kv-lang__op.is-on{color:#fff;background:rgba(35,137,230,.14)}'
            # no overlay do celular o seletor vira uma linha de opcoes
            '.kv-mmenu .kv-lang{width:100%;margin:0 0 14px}'
            '.kv-mmenu .kv-lang__btn{display:none}'
            '.kv-mmenu .kv-lang__menu{position:static;display:flex;flex-direction:row;flex-wrap:wrap;'
            'gap:8px;min-width:0;background:none;border:0;box-shadow:none;padding:0}'
            '.kv-mmenu .kv-lang__op{border:1px solid rgba(255,255,255,.16);border-radius:999px;'
            'padding:9px 14px}'
            # o seletor entra dentro do container do botao "Entrar": vira linha
            '@media(min-width:1200px){'
            '.framer-1pulp5i-container{display:flex!important;flex-direction:row!important;'
            'align-items:center!important;gap:10px!important;width:auto!important;flex:0 0 auto!important}'
            '.framer-dgbif5{width:auto!important;flex:0 0 auto!important;flex-wrap:nowrap!important;gap:10px!important}'
            '.framer-1wrsd4m{gap:10px!important;flex-wrap:nowrap!important}'
            '.kv-lang{margin-right:0}'
            '.kv-lang__btn{padding:8px 11px;font-size:13.5px;white-space:nowrap}'
            # em frances as palavras do menu sao mais longas e colidiam com os botoes
            '.framer-1419ah{max-width:calc(100% - 600px)!important;gap:6px!important}'
            '.framer-1419ah .framer-dztj6u p{font-size:14.5px!important}'
            '}'
            '@media(min-width:1200px) and (max-width:1439px){'
            '.framer-1419ah .framer-dztj6u p{font-size:13px!important}'
            '.framer-1419ah{gap:2px!important;max-width:calc(100% - 560px)!important}}'
            # De 1200 a 1279 a barra nao comporta logo + menu + botoes: o menu
            # em portugues pede 629px e o teto acima da 554, entao os itens
            # vazavam da caixa e caiam por cima do seletor. Aqui o seletor vira
            # so o globo (o rotulo PT sai, e o globo ja diz o que e) e o menu
            # aperta o suficiente para caber no que sobra.
            '@media(min-width:1200px) and (max-width:1279.98px){'
            '.kv-lang__btn b{display:none}'
            '.kv-lang__btn{padding:8px 9px}'
            '.kv-lang{margin-right:6px}'
            '.framer-1419ah{gap:0!important;max-width:calc(100% - 505px)!important}'
            '.framer-1419ah .framer-oZlM5{padding:6px 4px!important}'
            '.framer-1419ah .framer-dztj6u p{font-size:12.5px!important}}'
            '@media(max-width:1199px){.framer-tPXQv .kv-lang{display:none}}'
            '</style>')

JS_LANG = ('<script id="kv-lang-js">(function(){function init(){'
           'var wraps=document.querySelectorAll(".kv-lang");if(!wraps.length)return;'
           'wraps.forEach(function(w){var b=w.querySelector(".kv-lang__btn");if(!b)return;'
           'b.addEventListener("click",function(e){e.preventDefault();e.stopPropagation();'
           'var on=w.classList.toggle("is-open");b.setAttribute("aria-expanded",on?"true":"false");});});'
           'document.addEventListener("click",function(){wraps.forEach(function(w){'
           'w.classList.remove("is-open");var b=w.querySelector(".kv-lang__btn");'
           'if(b)b.setAttribute("aria-expanded","false");});});'
           '}if(document.readyState!=="loading")init();'
           'else document.addEventListener("DOMContentLoaded",init);})();</script>')


def hreflang(lang):
    out = ''
    for l in TODOS:
        out += '<link rel="alternate" hreflang="%s" href="%s%s">' % (
            i18n.META['lang_attr'][l], URL, i18n.CAMINHO[l])
    # x-default aponta para /pt/, nao para a raiz: a raiz responde 301 e mandar
    # o Google para um redirecionamento gasta rastreio a toa. O sitemap ja fazia
    # assim; era o HTML que divergia.
    out += '<link rel="alternate" hreflang="x-default" href="%s%s">' % (
        URL, i18n.CAMINHO['pt'])
    return out


def traduzir_caminhos(s):
    """Assets em caminho absoluto: todas as paginas vivem em subpasta."""
    s = s.replace('href="_ext/', 'href="/_ext/').replace('src="_ext/', 'src="/_ext/')
    s = s.replace('url(_ext/', 'url(/_ext/').replace("src='_ext/", "src='/_ext/")
    s = s.replace('"_ext/icons/ativos/', '"/_ext/icons/ativos/')
    return s


# ---------------------------------------------------------------------------
def traduzir(s, lang):
    # 1. textos visiveis, do mais longo para o mais curto para nao quebrar
    #    strings que sao subcadeia de outras.
    #    O espaco em volta do no de texto entra no casamento e sai preservado:
    #    titulos como "Opere em todos os <em>mercados</em> globais" deixam um
    #    espaco colado no sinal de menor, e com casamento exato so o miolo do
    #    <em> era traduzido — o /en/ exibia "Opere em todos os global globais".
    for pt in sorted(i18n.T, key=len, reverse=True):
        alvo = i18n.T[pt].get(lang)
        if not alvo:
            continue
        s = re.sub(r'>(\s*)%s(\s*)<' % re.escape(pt),
                   lambda m: '>' + m.group(1) + alvo + m.group(2) + '<', s)

    # 2. respostas do FAQ: no objeto ANS do JS e no FAQPage do JSON-LD
    for pergunta, versoes in i18n.FAQ.items():
        s = s.replace(json.dumps(versoes['pt'], ensure_ascii=False),
                      json.dumps(versoes[lang], ensure_ascii=False))
        s = s.replace(versoes['pt'], versoes[lang])
        pt_q = pergunta
        alvo_q = i18n.T.get(pt_q.rstrip('?'), {}).get(lang) or i18n.T.get(pt_q, {}).get(lang)
        if alvo_q:
            if not alvo_q.endswith('?'):
                alvo_q += '?'
            s = s.replace('"%s"' % pt_q, '"%s"' % alvo_q)

    # 2b. textos que vivem em atributos (alt das imagens)
    for pt_a, versoes in i18n.ATRIBUTOS.items():
        if versoes.get(lang):
            s = s.replace('"%s"' % pt_a, '"%s"' % versoes[lang])

    # 2c. link para o blog no rodape (o Google precisa de link interno para achar)
    nav = i18n.T['Navegação'].get(lang, 'Navegação')
    a = '<h3>%s</h3>\n    <ul>' % nav
    if a in s and 'href="/blog/"' not in s:
        s = s.replace(a, a + '<li><a href="/blog/">Blog</a></li>', 1)

    # 3. meta tags
    M = i18n.META
    s = s.replace(M['title']['pt'], M['title'][lang])
    s = s.replace(M['description']['pt'], M['description'][lang])
    s = s.replace(M['twitter_title']['pt'], M['twitter_title'][lang])
    s = s.replace(M['keywords']['pt'], M['keywords'][lang])
    s = s.replace('<html lang="pt-BR">', '<html lang="%s">' % M['lang_attr'][lang])
    s = s.replace('content="pt_BR"', 'content="%s"' % M['og_locale'][lang])

    # 4. as paginas ficam em subpasta: caminho relativo quebraria
    s = traduzir_caminhos(s)

    return s


def ajustar_jsonld(s, lang):
    """Poe a pagina no dominio real e separa as entidades do JSON-LD por idioma.

    A fonte carrega o dominio de teste do Worker: nos @id do grafo e tambem em
    og:image, twitter:image e og:image:secure_url. Pior que o dominio: WebPage,
    FAQPage e BreadcrumbList nasciam ancorados na raiz, entao os quatro idiomas
    declaravam a MESMA pagina. Aqui cada um passa a declarar a sua; Organization
    e WebSite continuam na raiz, que e onde devem ficar — sao do site, nao da
    pagina.

    A origem antiga sai do proprio grafo, e nao de uma constante: assim trocar o
    dominio na fonte nao quebra isto em silencio.
    """
    marca = '<script type="application/ld+json">'
    ini = s.find(marca + '{"@context"')
    if ini < 0:
        return s
    a = ini + len(marca)
    b = s.find('</script>', a)
    try:
        grafo = json.loads(s[a:b])
    except ValueError:
        return s
    if '@graph' not in grafo:
        return s

    org = next((e for e in grafo['@graph'] if '@id' in e and '#organization' in e['@id']), None)
    if not org:
        return s
    origem = org['@id'].split('#')[0].rstrip('/')
    if origem == URL:
        return s

    # o dominio velho aparece tambem em og:image e twitter:image, fora do grafo
    s = s.replace(origem, URL)
    a = s.find(marca + '{"@context"') + len(marca)   # a troca encurtou o texto
    b = s.find('</script>', a)
    grafo = json.loads(s[a:b])
    pagina = URL + i18n.CAMINHO[lang]
    DA_PAGINA = {'WebPage', 'FAQPage', 'BreadcrumbList'}
    for e in grafo['@graph']:
        tipos = e.get('@type', '')
        tipos = {tipos} if isinstance(tipos, str) else set(tipos)
        if tipos & DA_PAGINA:
            if '@id' in e and '#' in e['@id']:
                e['@id'] = pagina + '#' + e['@id'].split('#', 1)[1]
            if 'url' in e:
                e['url'] = pagina
    return s[:a] + json.dumps(grafo, ensure_ascii=False) + s[b:]


def canonicalizar(s, lang):
    s = re.sub(r'<link rel="canonical" href="[^"]*">',
               '<link rel="canonical" href="%s%s">' % (URL, i18n.CAMINHO[lang]), s)
    s = re.sub(r'<meta property="og:url" content="[^"]*">',
               '<meta property="og:url" content="%s%s">' % (URL, i18n.CAMINHO[lang]), s)
    return s



def limpar(s):
    """Remove o que uma execucao anterior injetou, para o gerador ser idempotente."""
    for ident in ['kv-lang-css', 'kv-lang-fit']:
        s = re.sub(r'(?:<!--[^>]*?-->)?\s*<style id="%s">.*?</style>' % ident, '', s, flags=re.S)
    s = re.sub(r'<script id="kv-lang-js">.*?</script>', '', s, flags=re.S)
    s = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', s)
    s = re.sub(r'<div class="kv-lang">.*?</div></div>', '', s, flags=re.S)
    return s


def injetar_comuns(s, lang):
    """CSS, JS, hreflang e o seletor — iguais em todos os idiomas."""
    s = limpar(s)
    s = canonicalizar(s, lang)
    s = ajustar_jsonld(s, lang)
    s = s.replace('</head>', CSS_LANG + hreflang(lang) + '</head>', 1)
    s = s.replace('</body>', JS_LANG + '</body>', 1)

    sel = seletor(lang)
    # header desktop: antes do botao "Entrar"
    alvo = '<a class="framer-yHDvT framer-TfBSh framer-1kzd2fj'
    n = s.count(alvo)
    s = s.replace(alvo, sel + alvo)
    # overlay do celular
    s = s.replace('<div class="kv-mmenu__cta">', '<div class="kv-mmenu__cta">' + sel, 1)
    return s, n


# ---------------------------------------------------------------------------
base = limpar(io.open(FONTE, encoding='utf-8').read())

# o portugues tambem vira subpasta (/pt/), para bater com a URL ja indexada.
# O index.html da raiz segue sendo a FONTE de edicao, nao uma pagina servida.
pt = traduzir_caminhos(base)
pt, n_pt = injetar_comuns(pt, 'pt')
os.makedirs(os.path.join(PUB, 'pt'), exist_ok=True)
io.open(os.path.join(PUB, 'pt', 'index.html'), 'w', encoding='utf-8').write(pt)
print('pt : pt/index.html  (seletor em %d ponto do header + overlay)' % n_pt)

for lang in i18n.IDIOMAS:
    s = traduzir(base, lang)
    s, n = injetar_comuns(s, lang)
    pasta = os.path.join(PUB, lang)
    os.makedirs(pasta, exist_ok=True)
    io.open(os.path.join(pasta, 'index.html'), 'w', encoding='utf-8').write(s)
    restante = sum(1 for pt_s in i18n.T
                   if re.search(r'>\s*%s\s*<' % re.escape(pt_s), s)
                   and i18n.T[pt_s].get(lang))
    print('%s : %s/index.html  (%d bytes) — strings pt restantes: %d'
          % (lang, lang, len(s.encode('utf-8')), restante))
