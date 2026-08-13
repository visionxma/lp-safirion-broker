# -*- coding: utf-8 -*-
"""
Gera o blog: /blog/ (indice) e /blog/<slug>/ (artigos).

    python3 scripts/blog.py public https://safirion.com

Fica fora da landing de proposito: a home tem trabalho de conversao, o blog tem
trabalho de busca. Cada artigo e uma porta de entrada propria, com title,
description, canonical e JSON-LD Article dele.
"""
import io, os, re, sys, json, html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artigos import ARTIGOS, AVISO

PUB = sys.argv[1].rstrip('/')
URL = sys.argv[2].rstrip('/')
BLOG = os.path.join(PUB, 'blog')

MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
         'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']


def data_extenso(iso):
    a, m, d = iso.split('-')
    return '%d de %s de %s' % (int(d), MESES[int(m) - 1], a)


CSS = """
@font-face{font-family:Mazzard;src:url(/_ext/fonts/MazzardM-Light.woff2) format('woff2');font-weight:300;font-display:swap}
@font-face{font-family:Mazzard;src:url(/_ext/fonts/MazzardM-Regular.woff2) format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:Mazzard;src:url(/_ext/fonts/MazzardM-Medium.woff2) format('woff2');font-weight:500;font-display:swap}
@font-face{font-family:Mazzard;src:url(/_ext/fonts/MazzardM-SemiBold.woff2) format('woff2');font-weight:600;font-display:swap}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:#060b18;color:#fff;font-family:Mazzard,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
 line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
img{max-width:100%;height:auto;display:block}
.wrap{max-width:1180px;margin:0 auto;padding:0 clamp(20px,4vw,40px)}
.mono{font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,monospace;
 font-size:11px;letter-spacing:.16em;text-transform:uppercase}

/* ---------- topo ---------- */
.top{position:sticky;top:0;z-index:30;background:rgba(6,11,24,.86);backdrop-filter:blur(16px) saturate(1.4);
 -webkit-backdrop-filter:blur(16px) saturate(1.4);border-bottom:1px solid rgba(255,255,255,.08)}
.top .in{max-width:1180px;margin:0 auto;padding:15px clamp(20px,4vw,40px);display:flex;align-items:center;
 justify-content:space-between;gap:16px}
.top img{height:30px;width:auto}
.top nav{display:flex;align-items:center;gap:6px}
.top a.btn{background:#2389e6;color:#060b18;font-weight:700;font-size:14px;padding:10px 19px;
 border-radius:999px;box-shadow:0 0 26px rgba(35,137,230,.32);white-space:nowrap}
.top a.btn:hover{filter:brightness(1.07)}
.top a.gh{color:#a1b8c3;font-size:14px;padding:10px 12px;white-space:nowrap}
.top a.gh:hover{color:#fff}

/* ---------- cabecalho do blog: alinhado a esquerda, com regra ---------- */
.cab{padding:clamp(40px,6vw,72px) 0 clamp(24px,3vw,34px);border-bottom:1px solid rgba(255,255,255,.08)}
.cab .in{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;flex-wrap:wrap}
.cab h1{font-size:clamp(30px,4.6vw,50px);font-weight:600;line-height:1.06;letter-spacing:-.025em;
 margin:10px 0 0;max-width:15ch}
.cab .sub{color:#7a8f9b;font-size:15px;max-width:34ch;margin:0;padding-bottom:5px}
.cab .mono{color:#4ba3f0;display:block}

/* ---------- destaque ---------- */
.dest{padding:clamp(28px,4vw,44px) 0;border-bottom:1px solid rgba(255,255,255,.08)}
.dest a{display:grid;grid-template-columns:1fr;gap:22px;align-items:center}
.dest .img{border-radius:16px;overflow:hidden;border:1px solid rgba(255,255,255,.10);background:#0a1120}
.dest .img img{aspect-ratio:16/9;object-fit:cover;width:100%;transition:transform .6s cubic-bezier(.2,.8,.2,1)}
.dest a:hover .img img{transform:scale(1.025)}
.dest h2{font-size:clamp(23px,3.3vw,36px);font-weight:600;line-height:1.12;letter-spacing:-.02em;margin:12px 0 12px}
.dest a:hover h2{color:#d6edf8}
.dest p{color:#a1b8c3;font-size:16.5px;line-height:1.6;margin:0 0 16px;max-width:52ch}
.dest .meta{color:#6f818f;font-size:13.5px}
@media(min-width:900px){.dest a{grid-template-columns:1.25fr 1fr;gap:44px}}

/* ---------- corpo: lista + barra lateral ---------- */
.corpo{display:grid;gap:clamp(30px,5vw,56px);padding:clamp(30px,4vw,48px) 0 clamp(48px,7vw,80px)}
@media(min-width:940px){.corpo{grid-template-columns:minmax(0,1fr) 306px}}

.lista{display:flex;flex-direction:column;gap:2px}
/* itens em linha, com divisoria — leitura de indice, nao de galeria de cartoes */
.item{display:grid;grid-template-columns:118px minmax(0,1fr);gap:20px;align-items:center;
 padding:22px 0;border-top:1px solid rgba(255,255,255,.08);transition:opacity .25s ease}
.item:first-child{border-top:0;padding-top:4px}
.lista:hover .item{opacity:.55}
.lista .item:hover{opacity:1}
.item .th{border-radius:11px;overflow:hidden;border:1px solid rgba(255,255,255,.10);background:#0a1120}
.item .th img{aspect-ratio:4/3;object-fit:cover;width:100%}
.item h3{font-size:clamp(17px,2vw,20.5px);font-weight:600;line-height:1.3;letter-spacing:-.012em;margin:7px 0 6px}
.item:hover h3{color:#4ba3f0}
.item p{color:#8fa5b1;font-size:14.5px;line-height:1.5;margin:0 0 8px;display:none}
.item .meta{color:#6f818f;font-size:12.5px}
@media(min-width:620px){.item{grid-template-columns:172px minmax(0,1fr);gap:26px}.item p{display:block}}

/* ---------- barra lateral ---------- */
.lado{display:flex;flex-direction:column;gap:26px}
@media(min-width:940px){.lado{position:sticky;top:88px;align-self:start}}
.bloco{border:1px solid rgba(255,255,255,.10);border-radius:16px;overflow:hidden;background:#0a1120}
.bloco > h2{font-size:13px;font-weight:600;letter-spacing:.05em;margin:0;padding:15px 18px;color:#fff;
 border-bottom:1px solid rgba(255,255,255,.08);display:flex;justify-content:space-between;align-items:center;gap:10px}
.bloco > h2 span{color:#6f818f;font-weight:400;letter-spacing:0;font-size:11.5px}
.tags{display:flex;flex-wrap:wrap;gap:8px;padding:16px 18px}
.tags a{border:1px solid rgba(255,255,255,.14);border-radius:999px;padding:7px 14px;font-size:13px;color:#a1b8c3}
.tags a:hover{border-color:rgba(35,137,230,.5);color:#fff;background:rgba(35,137,230,.10)}
.news__item{display:block;padding:13px 18px;border-top:1px solid rgba(255,255,255,.07);transition:background .2s ease}
.news__item:first-of-type{border-top:0}
.news__item:hover{background:#111a2b}
.news__item b{display:block;font-size:14px;font-weight:500;color:#fff;line-height:1.38;margin-bottom:4px}
.news__item i{font-style:normal;color:#4ba3f0;font-size:11.5px}
.news__item i::after{content:" ↗";font-size:10px}
.news__vazio{padding:15px 18px;color:#6f818f;font-size:14px}
.cta-lado{display:block;padding:20px 18px;background:linear-gradient(155deg,#111a2b,#0a1120 72%)}
.cta-lado b{display:block;font-size:16.5px;font-weight:600;margin-bottom:6px}
.cta-lado span{display:block;color:#a1b8c3;font-size:13.5px;line-height:1.5;margin-bottom:14px}
.cta-lado i{display:inline-block;font-style:normal;background:#2389e6;color:#060b18;font-weight:700;
 font-size:13.5px;padding:9px 17px;border-radius:999px}
.cta-lado:hover i{filter:brightness(1.07)}

/* ---------- artigo ---------- */
.artigo{padding:clamp(30px,4.5vw,52px) 0 0}
.artigo .col{max-width:720px}
.tag{display:inline-block;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.04);
 border-radius:999px;padding:6px 14px;font-size:12.5px;color:#d6edf8}
.artigo h1{font-size:clamp(28px,4.4vw,44px);font-weight:600;line-height:1.1;letter-spacing:-.025em;margin:16px 0 14px}
.artigo .meta{color:#6f818f;font-size:14px;display:flex;gap:9px;flex-wrap:wrap;align-items:center}
.artigo .meta i{font-style:normal;color:#3d4d59}
.capa{margin:clamp(26px,3.4vw,38px) 0 clamp(28px,3.6vw,40px);border-radius:18px;overflow:hidden;
 border:1px solid rgba(255,255,255,.10)}
.capa img{width:100%;aspect-ratio:16/9;object-fit:cover}
article h2{font-size:clamp(21px,2.9vw,27px);font-weight:600;line-height:1.22;letter-spacing:-.015em;
 margin:clamp(34px,4.4vw,46px) 0 13px}
article h3{font-size:clamp(16.5px,2vw,19px);font-weight:600;margin:28px 0 9px;color:#d6edf8}
article p{margin:0 0 17px;color:#a1b8c3;font-size:17px;line-height:1.72}
article strong{color:#fff;font-weight:600}
article em{color:#d6edf8;font-style:italic}
article ul{margin:0 0 20px;padding:0;list-style:none}
article ul li{position:relative;padding-left:25px;margin-bottom:10px;color:#a1b8c3;font-size:17px}
article ul li::before{content:"";position:absolute;left:2px;top:11px;width:6px;height:6px;border-radius:50%;background:#2389e6}
.cta{display:block;margin:clamp(32px,4.4vw,44px) 0;padding:clamp(22px,3vw,30px);border-radius:18px;
 border:1px solid rgba(35,137,230,.28);background:linear-gradient(155deg,#111a2b,#0a1120 70%)}
.cta b{display:block;font-size:18.5px;font-weight:600;color:#fff;margin-bottom:5px}
.cta span{color:#a1b8c3;font-size:14.5px}
.cta:hover{border-color:rgba(35,137,230,.5)}
.aviso{margin-top:clamp(32px,4.4vw,44px);padding-top:20px;border-top:1px solid rgba(255,255,255,.08);
 color:#6f818f;font-size:13px;line-height:1.65}

/* ---------- leia tambem ---------- */
.mais{border-top:1px solid rgba(255,255,255,.08);margin-top:clamp(36px,5vw,52px);
 padding:clamp(32px,4.4vw,44px) 0 clamp(44px,6vw,64px)}
.mais h2{font-size:13px;font-weight:600;letter-spacing:.05em;margin:0 0 20px;color:#7a8f9b}
.mais__grid{display:grid;gap:16px}
@media(min-width:680px){.mais__grid{grid-template-columns:repeat(3,1fr)}}
.mais__i{display:block;border-radius:13px;overflow:hidden;border:1px solid rgba(255,255,255,.10);
 background:#0a1120;transition:border-color .3s ease,transform .3s cubic-bezier(.2,.8,.2,1)}
.mais__i:hover{border-color:rgba(35,137,230,.34);transform:translateY(-2px)}
.mais__i img{width:100%;aspect-ratio:16/9;object-fit:cover}
.mais__i span{display:block;padding:13px 15px;color:#fff;font-size:14.5px;font-weight:500;line-height:1.35}

/* ---------- rodape ---------- */
footer{border-top:1px solid rgba(255,255,255,.08);padding:34px 0;color:#6f818f;font-size:13px}
footer .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
footer a{color:#a1b8c3}
footer a:hover{color:#fff}
@media(max-width:560px){.top a.gh{display:none}}

/* ---------- legal ---------- */
.legal .col{max-width:800px}
.legal h2{font-size:clamp(19px,2.6vw,23px);margin:34px 0 12px}
.legal h3{font-size:17px;margin:26px 0 9px}
.legal p,.legal li{color:#a1b8c3;font-size:16px;line-height:1.72}
.legal ol,.legal ul{padding-left:22px;margin:0 0 18px}
.legal li{margin-bottom:9px}
.legal table{width:100%;border-collapse:collapse;margin:18px 0;font-size:14.5px}
.legal td,.legal th{border:1px solid rgba(255,255,255,.10);padding:10px 12px;text-align:left;color:#a1b8c3}
.legal th{color:#fff;font-weight:600}
.legal a{color:#4ba3f0;text-decoration:underline}
.legal strong,.legal b{color:#fff}
"""


NEWS = ('<section class="bloco"><h2>Mercado hoje <span>fonte externa</span></h2>'
        '<div id="news"><div class="news__vazio">Carregando…</div></div></section>'
        '<script>(function(){'
        'function q(t){var d=document.createElement("div");d.textContent=t;return d.innerHTML;}'
        'fetch("/api/noticias").then(function(r){return r.ok?r.json():null;}).then(function(d){'
        'var alvo=document.getElementById("news");if(!alvo)return;'
        'var n=(d&&d.noticias)||[];'
        'if(!n.length){alvo.innerHTML=\'<div class="news__vazio">Sem manchetes agora.</div>\';return;}'
        'alvo.innerHTML=n.slice(0,6).map(function(x){'
        # rel=nofollow: e link para fora; nao passamos autoridade nem parecemos
        # troca de links. target=_blank mantem o visitante no site.
        'return \'<a class="news__item" href="\'+q(x.link)+\'" target="_blank" rel="noopener nofollow">\''
        '+\'<b>\'+q(x.titulo)+\'</b><i>\'+q(x.fonte)+\'</i></a>\';}).join("");'
        '}).catch(function(){});'
        '})();</script>')


def topo():
    return ('<header class="top"><div class="in">'
            '<a href="/" aria-label="Safirion"><img src="/_ext/icons/safirion-logo-horizontal.svg"'
            ' alt="Safirion" width="234" height="55"></a>'
            '<nav><a class="gh" href="/">Início</a><a class="gh" href="/blog/">Blog</a>'
            '<a class="btn" href="https://trade.safirion.com/register?aff=818084&amp;aff_model=revenue&amp;afftrack=LPP"'
            ' target="_blank" rel="noopener">Abrir conta</a></nav>'
            '</div></header>')


def rodape():
    return ('<footer><div class="wrap">'
            '<span>© 2026 Safirion. Todos os direitos reservados.</span>'
            '<span><a href="/">Início</a> · <a href="/blog/">Blog</a> · '
            '<a href="mailto:contato@safirion.com">contato@safirion.com</a></span>'
            '</div></footer>')


def cabeca(titulo, desc, canonical, extra='', imagem=None):
    return ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>%s</title>'
            '<meta name="description" content="%s">'
            '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">'
            '<link rel="canonical" href="%s">'
            '<link rel="icon" type="image/svg+xml" href="/_ext/icons/safirion-icon.svg">'
            '<meta name="theme-color" content="#060b18">'
            '<meta property="og:type" content="article">'
            '<meta property="og:site_name" content="Safirion">'
            '<meta property="og:locale" content="pt_BR">'
            '<meta property="og:title" content="%s">'
            '<meta property="og:description" content="%s">'
            '<meta property="og:url" content="%s">'
            '<meta property="og:image" content="%s">'
            '<meta name="twitter:card" content="summary_large_image">'
            '<link rel="preload" as="font" type="font/woff2" crossorigin'
            ' href="/_ext/fonts/MazzardM-Regular.woff2">'
            '<style>%s</style>%s</head><body>'
            % (html.escape(titulo), html.escape(desc), canonical,
               html.escape(titulo), html.escape(desc), canonical,
               imagem or (URL + '/_ext/img/og-image.jpg'), CSS, extra))


# ---------------------------------------------------------------------------
def render_corpo(a):
    out = ''
    for tipo, val in a['corpo']:
        if tipo == 'p':
            out += '<p>%s</p>' % val
        elif tipo == 'h2':
            out += '<h2>%s</h2>' % val
        elif tipo == 'h3':
            out += '<h3>%s</h3>' % val
        elif tipo == 'ul':
            out += '<ul>%s</ul>' % ''.join('<li>%s</li>' % x for x in val)
        elif tipo == 'cta':
            out += ('<a class="cta" href="/"><b>%s</b>'
                    '<span>Ver condições, taxas e documentos na página da corretora →</span></a>' % val)
    return out


def leia_tambem(atual):
    """Links internos entre artigos: ajuda o leitor e distribui autoridade."""
    outros = [x for x in ARTIGOS if x['slug'] != atual['slug']][:3]
    if not outros:
        return ''
    itens = ''.join(
        '<a class="mais__i" href="/blog/%s/">'
        '<img src="/_ext/img/blog/%s.webp" alt="" width="1200" height="675" loading="lazy">'
        '<span>%s</span></a>' % (x['slug'], x['slug'], x['titulo']) for x in outros)
    return ('<section class="mais"><div class="wrap"><h2>Leia também</h2>'
            '<div class="mais__grid">%s</div></div></section>' % itens)


def ld_artigo(a, canonical):
    return ('<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a['seo_titulo'],
        "description": a['seo_desc'],
        "datePublished": a['data'],
        "dateModified": a['data'],
        "inLanguage": "pt-BR",
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "image": URL + "/_ext/img/blog/" + a["slug"] + ".webp",
        "author": {"@type": "Organization", "name": "Safirion", "url": URL + "/"},
        "publisher": {"@type": "Organization", "name": "Safirion",
                      "logo": {"@type": "ImageObject",
                               "url": URL + "/_ext/icons/safirion-logo-horizontal.svg"}},
        "isPartOf": {"@type": "Blog", "@id": URL + "/blog/#blog", "name": "Blog da Safirion"},
    }, ensure_ascii=False))


def ld_lista():
    return ('<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org",
        "@type": "Blog",
        "@id": URL + "/blog/#blog",
        "name": "Blog da Safirion",
        "description": "Artigos sobre saque, spread, regulamentação e primeiros passos no trading.",
        "inLanguage": "pt-BR",
        "url": URL + "/blog/",
        "publisher": {"@type": "Organization", "name": "Safirion", "url": URL + "/"},
        "blogPost": [{"@type": "BlogPosting", "headline": a['titulo'],
                      "url": "%s/blog/%s/" % (URL, a['slug']),
                      "datePublished": a['data'], "description": a['resumo']} for a in ARTIGOS],
    }, ensure_ascii=False))


# ---------------------------------------------------------------------------
os.makedirs(BLOG, exist_ok=True)

for a in ARTIGOS:
    canonical = '%s/blog/%s/' % (URL, a['slug'])
    pasta = os.path.join(BLOG, a['slug'])
    os.makedirs(pasta, exist_ok=True)
    doc = (cabeca(a['seo_titulo'], a['seo_desc'], canonical, ld_artigo(a, canonical),
                  '%s/_ext/img/blog/%s.webp' % (URL, a['slug']))
           + topo()
           + '<div class="artigo"><div class="wrap"><div class="col">'
           + '<span class="tag">%s</span>' % a['tag']
           + '<h1>%s</h1>' % a['titulo']
           + ('<p class="meta"><time datetime="%s">%s</time><i>·</i>'
              '<span>%d min de leitura</span></p>' % (a['data'], data_extenso(a['data']), a['minutos']))
           + '</div>'
           + ('<div class="capa"><img src="/_ext/img/blog/%s.webp" alt="" width="1200" height="675"'
              ' fetchpriority="high" decoding="async"></div>' % a['slug'])
           + '<article class="col">' + render_corpo(a)
           + '<p class="aviso"><strong>Aviso de risco:</strong> %s</p>' % AVISO
           + '</article></div></div>'
           + leia_tambem(a) + rodape() + '</body></html>')
    io.open(os.path.join(pasta, 'index.html'), 'w', encoding='utf-8').write(doc)
    print('  /blog/%s/  (%.1f KB)' % (a['slug'], len(doc.encode()) / 1024))

destaque, restantes = ARTIGOS[0], ARTIGOS[1:]

dest = ('<section class="dest"><div class="wrap"><a href="/blog/%s/">'
        '<span class="img"><img src="/_ext/img/blog/%s.webp" alt="" width="1200" height="675"'
        ' fetchpriority="high" decoding="async"></span>'
        '<span><span class="tag">%s</span><h2>%s</h2><p>%s</p>'
        '<span class="meta"><time datetime="%s">%s</time> · %d min de leitura</span></span>'
        '</a></div></section>'
        % (destaque['slug'], destaque['slug'], destaque['tag'], destaque['titulo'],
           destaque['resumo'], destaque['data'], data_extenso(destaque['data']),
           destaque['minutos']))

itens = ''
for a in restantes:
    itens += ('<a class="item" href="/blog/%s/">'
              '<span class="th"><img src="/_ext/img/blog/%s.webp" alt="" width="1200" height="675"'
              ' loading="lazy" decoding="async"></span>'
              '<span><span class="mono" style="color:#4ba3f0">%s</span>'
              '<h3>%s</h3><p>%s</p>'
              '<span class="meta"><time datetime="%s">%s</time> · %d min</span></span></a>'
              % (a['slug'], a['slug'], a['tag'], a['titulo'], a['resumo'],
                 a['data'], data_extenso(a['data']), a['minutos']))

vistos, tags = set(), ''
for a in ARTIGOS:
    if a['tag'] in vistos:
        continue
    vistos.add(a['tag'])
    tags += '<a href="/blog/%s/">%s</a>' % (a['slug'], a['tag'])

lado = ('<aside class="lado">'
        '<section class="bloco"><h2>Temas</h2><div class="tags">%s</div></section>'
        '%s'
        '<a class="bloco cta-lado" href="https://trade.safirion.com/register'
        '?aff=818084&amp;aff_model=revenue&amp;afftrack=LPP" target="_blank" rel="noopener">'
        '<b>Abra sua conta</b><span>Depósito a partir de US$ 10, conta em cerca de 2 minutos.</span>'
        '<i>Começar agora →</i></a>'
        '</aside>' % (tags, NEWS))

indice = (cabeca('Blog da Safirion — saque, spread, regulamentação e primeiros passos',
                 'Artigos sobre como funciona o saque em corretoras, spread fixo, '
                 'regulamentação em Seychelles e quanto capital faz sentido para começar.',
                 URL + '/blog/', ld_lista())
          + topo()
          + '<header class="cab"><div class="wrap in"><div>'
            '<span class="mono" style="color:#4ba3f0">Blog</span>'
            '<h1>Como corretora funciona por dentro</h1></div>'
            '<p class="sub">Saque, spread, regulamentação e primeiros passos — '
            'explicados sem jargão, por quem opera.</p></div></header>'
          + dest
          + '<div class="wrap"><div class="corpo">'
          + '<div class="lista">' + itens + '</div>'
          + lado
          + '</div></div>'
          + rodape() + '</body></html>')
io.open(os.path.join(BLOG, 'index.html'), 'w', encoding='utf-8').write(indice)
print('  /blog/  (%.1f KB, %d artigos)' % (len(indice.encode()) / 1024, len(ARTIGOS)))
