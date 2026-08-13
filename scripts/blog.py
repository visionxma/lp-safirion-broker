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
@font-face{font-family:Mazzard;src:url(/_ext/fonts/MazzardM-Regular.woff2) format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:Mazzard;src:url(/_ext/fonts/MazzardM-Medium.woff2) format('woff2');font-weight:500;font-display:swap}
@font-face{font-family:Mazzard;src:url(/_ext/fonts/MazzardM-SemiBold.woff2) format('woff2');font-weight:600;font-display:swap}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:#060b18;color:#fff;font-family:Mazzard,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
 line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:inherit}
img{max-width:100%;height:auto;display:block}
.wrap{max-width:760px;margin:0 auto;padding:0 24px}

/* ---------- topo ---------- */
.top{position:sticky;top:0;z-index:20;background:rgba(6,11,24,.86);backdrop-filter:blur(16px) saturate(1.4);
 -webkit-backdrop-filter:blur(16px) saturate(1.4);border-bottom:1px solid rgba(255,255,255,.08)}
.top .in{max-width:1180px;margin:0 auto;padding:16px 24px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.top img{height:32px;width:auto}
.top nav{display:flex;align-items:center;gap:8px}
.top a.btn{background:#2389e6;color:#060b18;font-weight:700;font-size:14.5px;text-decoration:none;
 padding:11px 20px;border-radius:999px;box-shadow:0 0 26px rgba(35,137,230,.32);white-space:nowrap}
.top a.btn:hover{filter:brightness(1.07)}
.top a.gh{color:#a1b8c3;text-decoration:none;font-size:14.5px;padding:11px 14px;white-space:nowrap}
.top a.gh:hover{color:#fff}

/* ---------- cabecalho ---------- */
.head{padding:clamp(48px,7vw,84px) 0 clamp(28px,4vw,44px);position:relative;overflow:hidden}
.head::before{content:"";position:absolute;inset:0;z-index:0;pointer-events:none;
 background:radial-gradient(760px 420px at 50% -10%,rgba(35,137,230,.16),transparent 70%)}
.head .wrap{position:relative;z-index:1}
.tag{display:inline-block;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.04);
 border-radius:999px;padding:7px 15px;font-size:13px;color:#d6edf8;margin-bottom:20px}
h1{font-size:clamp(30px,5vw,46px);font-weight:600;line-height:1.14;letter-spacing:-.02em;margin:0 0 18px}
.meta{color:#7a8f9b;font-size:14.5px;display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.meta i{font-style:normal;color:#3d4d59}

/* ---------- corpo ---------- */
article{padding-bottom:clamp(40px,6vw,72px)}
article h2{font-size:clamp(22px,3.2vw,29px);font-weight:600;line-height:1.22;letter-spacing:-.015em;
 margin:clamp(38px,5vw,52px) 0 14px}
article h3{font-size:clamp(17px,2.2vw,20px);font-weight:600;margin:30px 0 10px;color:#d6edf8}
article p{margin:0 0 18px;color:#a1b8c3;font-size:17px}
article strong{color:#fff;font-weight:600}
article em{color:#d6edf8;font-style:italic}
article ul{margin:0 0 22px;padding:0;list-style:none}
article ul li{position:relative;padding-left:26px;margin-bottom:11px;color:#a1b8c3;font-size:17px}
article ul li::before{content:"";position:absolute;left:2px;top:11px;width:7px;height:7px;border-radius:50%;
 background:#2389e6}
.cta{display:block;margin:clamp(34px,5vw,46px) 0;padding:clamp(24px,3.4vw,32px);border-radius:20px;
 border:1px solid rgba(35,137,230,.28);background:linear-gradient(155deg,#111a2b,#0a1120 70%);text-decoration:none}
.cta b{display:block;font-size:19px;font-weight:600;color:#fff;margin-bottom:6px}
.cta span{color:#a1b8c3;font-size:15px}
.cta:hover{border-color:rgba(35,137,230,.5)}
.aviso{margin-top:clamp(34px,5vw,48px);padding-top:22px;border-top:1px solid rgba(255,255,255,.08);
 color:#6f818f;font-size:13.5px;line-height:1.65}


/* ---------- manchetes ---------- */
.news{padding-bottom:clamp(40px,6vw,64px)}
.news__cab{display:flex;align-items:baseline;justify-content:space-between;gap:14px;flex-wrap:wrap;
 margin:0 0 18px}
.news__cab h2{font-size:clamp(19px,2.6vw,23px);font-weight:600;margin:0}
.news__cab span{color:#6f818f;font-size:13px}
.news__lista{display:grid;gap:1px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.08);
 border-radius:16px;overflow:hidden}
.news__item{display:block;padding:16px 18px;background:#0a1120;text-decoration:none;
 transition:background .2s ease}
.news__item:hover{background:#111a2b}
.news__item b{display:block;font-size:15.5px;font-weight:500;color:#fff;line-height:1.4;margin-bottom:5px}
.news__item i{font-style:normal;color:#4ba3f0;font-size:12.5px}
.news__item i::after{content:" ↗";font-size:11px}
.news__vazio{padding:18px;background:#0a1120;color:#6f818f;font-size:14.5px}

/* ---------- lista ---------- */
.lista{display:grid;gap:16px;padding-bottom:clamp(48px,7vw,80px)}
.card{display:block;padding:clamp(22px,3vw,30px);border-radius:20px;border:1px solid rgba(255,255,255,.10);
 background:linear-gradient(155deg,#111a2b 0%,#0a1120 62%,#060b18 100%);text-decoration:none;
 transition:border-color .3s ease,transform .3s cubic-bezier(.2,.8,.2,1)}
.card:hover{border-color:rgba(35,137,230,.34);transform:translateY(-3px)}
.card h2{font-size:clamp(19px,2.6vw,23px);font-weight:600;line-height:1.26;margin:12px 0 10px;color:#fff}
.card p{color:#a1b8c3;font-size:15.5px;margin:0 0 14px}
.card .meta{font-size:13.5px}

/* ---------- rodape ---------- */
footer{border-top:1px solid rgba(255,255,255,.08);padding:40px 0;color:#6f818f;font-size:13.5px}
footer .wrap{max-width:1180px;display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap}
footer a{color:#a1b8c3;text-decoration:none}
footer a:hover{color:#fff}
@media(max-width:560px){.top .in{padding:12px 18px}.top a.gh{display:none}}
"""


NEWS = ('<section class="news"><div class="wrap">'
        '<div class="news__cab"><h2>Mercado hoje</h2>'
        '<span>Manchetes de fontes externas — o link leva ao original</span></div>'
        '<div class="news__lista" id="news"><div class="news__vazio">Carregando…</div></div>'
        '</div></section>'
        '<script>(function(){'
        'function q(t){var d=document.createElement("div");d.textContent=t;return d.innerHTML;}'
        'fetch("/api/noticias").then(function(r){return r.ok?r.json():null;}).then(function(d){'
        'var alvo=document.getElementById("news");if(!alvo)return;'
        'var n=(d&&d.noticias)||[];'
        'if(!n.length){alvo.innerHTML=\'<div class="news__vazio">Sem manchetes no momento.</div>\';return;}'
        'alvo.innerHTML=n.slice(0,8).map(function(x){'
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
            '<nav><a class="gh" href="/blog/">Blog</a>'
            '<a class="btn" href="https://trade.safirion.com/register?aff=818084&amp;aff_model=revenue&amp;afftrack=LPP"'
            ' target="_blank" rel="noopener">Abrir conta</a></nav>'
            '</div></header>')


def rodape():
    return ('<footer><div class="wrap">'
            '<span>© 2026 Safirion. Todos os direitos reservados.</span>'
            '<span><a href="/">Início</a> · <a href="/blog/">Blog</a> · '
            '<a href="mailto:contato@safirion.com">contato@safirion.com</a></span>'
            '</div></footer>')


def cabeca(titulo, desc, canonical, extra=''):
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
            '<meta property="og:image" content="%s/_ext/img/og-image.jpg">'
            '<meta name="twitter:card" content="summary_large_image">'
            '<link rel="preload" as="font" type="font/woff2" crossorigin'
            ' href="/_ext/fonts/MazzardM-Regular.woff2">'
            '<style>%s</style>%s</head><body>'
            % (html.escape(titulo), html.escape(desc), canonical,
               html.escape(titulo), html.escape(desc), canonical, URL, CSS, extra))


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
        "image": URL + "/_ext/img/og-image.jpg",
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
    doc = (cabeca(a['seo_titulo'], a['seo_desc'], canonical, ld_artigo(a, canonical))
           + topo()
           + '<div class="head"><div class="wrap">'
           + '<span class="tag">%s</span>' % a['tag']
           + '<h1>%s</h1>' % a['titulo']
           + '<p class="meta"><time datetime="%s">%s</time><i>·</i><span>%d min de leitura</span></p>'
             % (a['data'], data_extenso(a['data']), a['minutos'])
           + '</div></div>'
           + '<article><div class="wrap">' + render_corpo(a)
           + '<p class="aviso"><strong>Aviso de risco:</strong> %s</p>' % AVISO
           + '</div></article>' + rodape() + '</body></html>')
    io.open(os.path.join(pasta, 'index.html'), 'w', encoding='utf-8').write(doc)
    print('  /blog/%s/  (%.1f KB)' % (a['slug'], len(doc.encode()) / 1024))

cards = ''
for a in ARTIGOS:
    cards += ('<a class="card" href="/blog/%s/"><span class="tag">%s</span>'
              '<h2>%s</h2><p>%s</p>'
              '<p class="meta"><time datetime="%s">%s</time><i>·</i><span>%d min</span></p></a>'
              % (a['slug'], a['tag'], a['titulo'], a['resumo'], a['data'],
                 data_extenso(a['data']), a['minutos']))

indice = (cabeca('Blog da Safirion — saque, spread, regulamentação e primeiros passos',
                 'Artigos sobre como funciona o saque em corretoras, spread fixo, '
                 'regulamentação em Seychelles e quanto capital faz sentido para começar.',
                 URL + '/blog/', ld_lista())
          + topo()
          + '<div class="head"><div class="wrap"><span class="tag">Blog</span>'
            '<h1>Como corretora funciona por dentro</h1>'
            '<p class="meta">Saque, spread, regulamentação e primeiros passos — '
            'explicados sem jargão.</p></div></div>'
          + '<div class="wrap"><div class="lista">' + cards + '</div></div>'
          + NEWS
          + rodape() + '</body></html>')
io.open(os.path.join(BLOG, 'index.html'), 'w', encoding='utf-8').write(indice)
print('  /blog/  (%.1f KB, %d artigos)' % (len(indice.encode()) / 1024, len(ARTIGOS)))
