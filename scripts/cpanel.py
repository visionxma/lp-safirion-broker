# -*- coding: utf-8 -*-
"""
Monta a pasta que vai para o public_html do cPanel.

    python3 scripts/cpanel.py

O site foi feito para Cloudflare Workers. Tres coisas de la nao existem no
Apache e sao traduzidas aqui:

  _redirects  -> RewriteRule no .htaccess
  _headers    -> Header/Cache-Control no .htaccess e em _ext/.htaccess
  worker/     -> api/cotacoes.php e api/noticias.php

O conteudo estatico e o mesmo de public/, sem alteracao.
"""
import io, os, shutil, sys, zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(RAIZ, 'public')
EXTRA = os.path.join(RAIZ, 'cpanel')
SAIDA = os.path.join(RAIZ, 'dist-cpanel')

# so o Cloudflare le esses dois; no Apache sao arquivos mortos que ficariam
# expostos na raiz do site
SO_CLOUDFLARE = {'_redirects', '_headers'}

if os.path.isdir(SAIDA):
    shutil.rmtree(SAIDA)

copiados = 0
for base, _, arquivos in os.walk(PUB):
    for nome in arquivos:
        if nome in SO_CLOUDFLARE or nome == '.DS_Store':
            continue
        origem = os.path.join(base, nome)
        destino = os.path.join(SAIDA, os.path.relpath(origem, PUB))
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        shutil.copy2(origem, destino)
        copiados += 1

extras = 0
for base, _, arquivos in os.walk(EXTRA):
    for nome in arquivos:
        origem = os.path.join(base, nome)
        destino = os.path.join(SAIDA, os.path.relpath(origem, EXTRA))
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        shutil.copy2(origem, destino)
        extras += 1

zip_path = os.path.join(RAIZ, 'safirion-cpanel.zip')
if os.path.exists(zip_path):
    os.remove(zip_path)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for base, _, arquivos in os.walk(SAIDA):
        for nome in arquivos:
            caminho = os.path.join(base, nome)
            z.write(caminho, os.path.relpath(caminho, SAIDA))

tam = sum(os.path.getsize(os.path.join(b, n))
          for b, _, fs in os.walk(SAIDA) for n in fs)
print('dist-cpanel/  %d arquivos de public/ + %d de cpanel/  (%.1f MB)'
      % (copiados, extras, tam / 1048576))
print('safirion-cpanel.zip  %.1f MB' % (os.path.getsize(zip_path) / 1048576))
