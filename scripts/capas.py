# -*- coding: utf-8 -*-
"""
Gera as capas dos artigos do blog.

    python3 scripts/capas.py public [servidor]

Cada capa é desenhada aqui e rasterizada com o Chrome headless — nada de banco
de imagens, que traria custo de licença e a mesma foto genérica que todo site de
corretora usa. O motivo visual conversa com o assunto: velas para spread, escudo
para regulamentação, barras para capital.

A capa é só arte, sem texto: o título já está no HTML, e embutido na imagem ele
seria cortado em qualquer recorte e apareceria duas vezes no card.

Saída: public/_ext/img/blog/<slug>.webp, 1200x675 (16:9).
"""
import io, os, subprocess, sys

PUB = sys.argv[1].rstrip('/')
SAIDA = os.path.join(PUB, '_ext', 'img', 'blog')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

BASE = """<!doctype html><meta charset="utf-8">
<style>
*{margin:0;box-sizing:border-box}
body{width:1200px;height:675px;overflow:hidden;position:relative;background:#060b18}
.bg{position:absolute;inset:0;background:
 radial-gradient(880px 580px at 62% 34%,rgba(35,137,230,.28),transparent 68%),
 radial-gradient(680px 480px at 14% 90%,rgba(75,163,240,.14),transparent 70%),
 linear-gradient(160deg,#0a1120,#060b18 72%)}
.grade{position:absolute;inset:0;opacity:.45;
 background:repeating-linear-gradient(90deg,rgba(214,237,248,.05) 0 1px,transparent 1px 74px),
            repeating-linear-gradient(0deg,rgba(214,237,248,.05) 0 1px,transparent 1px 74px)}
.art{position:absolute;inset:0;z-index:2}
.marca{position:absolute;bottom:44px;right:52px;z-index:5;height:28px;opacity:.45}
</style>
<div class="bg"></div><div class="grade"></div>
__ARTE__
<img class="marca" src="/_ext/icons/safirion-logo-horizontal.svg" alt="">
"""

# Motivos centralizados na viewBox de 1200x675 (centro em 600, 337).
ARTE = {
    # saque: um bloco com o saldo e setas saindo dele — dinheiro que de fato sai
    'como-funciona-saque-corretora': """
<svg class="art" viewBox="0 0 1200 675" fill="none">
  <g>
    <rect x="330" y="238" width="330" height="200" rx="20" stroke="#2389e6" stroke-width="2.5"/>
    <rect x="330" y="238" width="330" height="56" rx="20" fill="#2389e6" fill-opacity=".16"/>
    <circle cx="368" cy="266" r="7" fill="#4ba3f0"/>
    <path d="M372 346h176M372 386h108" stroke="#4ba3f0" stroke-width="8"
          stroke-linecap="round" opacity=".5"/>
  </g>
  <g stroke="#34d399" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M700 290h150M818 260l32 30-32 30"/>
    <path d="M700 348h104M772 318l32 30-32 30" opacity=".62"/>
    <path d="M700 406h58M726 376l32 30-32 30" opacity=".32"/>
  </g>
</svg>""",

    # spread: bid e ask como duas linhas com a fresta destacada, sobre as velas
    'o-que-e-spread-fixo': """
<svg class="art" viewBox="0 0 1200 675" fill="none">
  <rect x="330" y="196" width="540" height="72" fill="#2389e6" fill-opacity=".16"/>
  <g stroke-width="3">
    <path d="M330 196h540" stroke="#34d399" opacity=".9"/>
    <path d="M330 268h540" stroke="#f87171" opacity=".9"/>
  </g>
  <g stroke="#4ba3f0" stroke-width="2.5" opacity=".9">
    <path d="M600 196v72M588 210l12-14 12 14M588 254l12 14 12-14"/>
  </g>
  <g opacity=".6">
    <rect x="342" y="366" width="30" height="112" rx="5" fill="#34d399"/>
    <rect x="414" y="334" width="30" height="144" rx="5" fill="#f87171"/>
    <rect x="486" y="392" width="30" height="86" rx="5" fill="#34d399"/>
    <rect x="558" y="356" width="30" height="122" rx="5" fill="#34d399"/>
    <rect x="630" y="404" width="30" height="74" rx="5" fill="#f87171"/>
    <rect x="702" y="342" width="30" height="136" rx="5" fill="#34d399"/>
    <rect x="774" y="378" width="30" height="100" rx="5" fill="#34d399"/>
    <rect x="846" y="322" width="30" height="156" rx="5" fill="#34d399"/>
  </g>
</svg>""",

    # regulacao: escudo com selo de verificacao e aneis de auditoria
    'corretora-regulamentada-seychelles': """
<svg class="art" viewBox="0 0 1200 675" fill="none">
  <g stroke="#4ba3f0" stroke-width="2" opacity=".35">
    <circle cx="600" cy="338" r="182"/>
    <circle cx="600" cy="338" r="226"/>
  </g>
  <path d="M600 160l132 50v134c0 90-58 152-132 180-74-28-132-90-132-180V210z"
        stroke="#2389e6" stroke-width="3" fill="#2389e6" fill-opacity=".12"/>
  <path d="M540 340l40 40 96-100" stroke="#34d399" stroke-width="10"
        stroke-linecap="round" stroke-linejoin="round"/>
</svg>""",

    # capital: barras crescendo com a curva de aporte por cima
    'quanto-preciso-para-comecar-a-operar': """
<svg class="art" viewBox="0 0 1200 675" fill="none">
  <g>
    <rect x="368" y="368" width="70" height="120" rx="9" fill="#2389e6" fill-opacity=".26"/>
    <rect x="466" y="316" width="70" height="172" rx="9" fill="#2389e6" fill-opacity=".42"/>
    <rect x="564" y="256" width="70" height="232" rx="9" fill="#2389e6" fill-opacity=".62"/>
    <rect x="662" y="186" width="70" height="302" rx="9" fill="#2389e6" fill-opacity=".88"/>
  </g>
  <path d="M380 356c110-16 216-72 330-160" stroke="#34d399" stroke-width="4"
        stroke-linecap="round" stroke-dasharray="14 12" opacity=".9"/>
  <circle cx="716" cy="192" r="12" fill="#34d399"/>
</svg>""",
}


def gerar(artigos, servidor):
    os.makedirs(SAIDA, exist_ok=True)
    tmp = os.path.join(PUB, '_capa_tmp.html')
    for a in artigos:
        io.open(tmp, 'w', encoding='utf-8').write(
            BASE.replace('__ARTE__', ARTE.get(a['slug'], '')))
        png = '/tmp/capa_%s.png' % a['slug']
        subprocess.run([CHROME, '--headless', '--disable-gpu', '--hide-scrollbars',
                        '--window-size=1200,675', '--screenshot=' + png,
                        '--virtual-time-budget=9000',
                        '%s/_capa_tmp.html' % servidor], capture_output=True)
        webp = os.path.join(SAIDA, a['slug'] + '.webp')
        subprocess.run(['cwebp', '-q', '86', '-quiet', png, '-o', webp], capture_output=True)
        tam = os.path.getsize(webp) / 1024 if os.path.exists(webp) else 0
        print('  %-42s %5.1f KB' % (a['slug'] + '.webp', tam))
    if os.path.exists(tmp):
        os.remove(tmp)


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from artigos import ARTIGOS
    gerar(ARTIGOS, sys.argv[2] if len(sys.argv) > 2 else 'http://127.0.0.1:8125')
