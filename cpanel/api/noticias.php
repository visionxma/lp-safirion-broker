<?php
/**
 * Porte de /api/noticias (worker/index.js) para PHP.
 *
 * Curadoria, nao republicacao: titulo, resumo curto e link para a fonte.
 * Republicar materia seria problema de direito autoral, e o Google prefere o
 * original — por isso o site linka a fonte com rel="nofollow".
 */
declare(strict_types=1);
require __DIR__ . '/_http.php';

const SAFIRION_TTL = 900;   // 15 min

$FEEDS = [
    ['url' => 'https://www.infomoney.com.br/feed/',        'fonte' => 'InfoMoney'],
    ['url' => 'https://br.investing.com/rss/news_25.rss',  'fonte' => 'Investing.com'],
];

/** Extrai uma tag do bloco <item> e limpa CDATA, markup e entidades. */
function safirion_tag(string $bloco, string $nome): string
{
    if (!preg_match('#<' . $nome . '[^>]*>([\s\S]*?)</' . $nome . '>#i', $bloco, $m)) {
        return '';
    }
    $t = preg_replace('/<!\[CDATA\[([\s\S]*?)\]\]>/', '$1', $m[1]);
    $t = preg_replace('/<[^>]+>/', '', (string) $t);
    /* os feeds usam &#8216; e afins para aspas tipograficas; sem decodificar,
       elas apareciam cruas no titulo */
    $t = html_entity_decode((string) $t, ENT_QUOTES | ENT_HTML5, 'UTF-8');
    $t = str_replace("\xC2\xA0", ' ', $t);          // nbsp
    $t = preg_replace('/&\w+;/', ' ', $t);          // entidade que sobrou
    $t = preg_replace('/\s+/', ' ', (string) $t);
    return trim((string) $t);
}

try {
    $guardado = safirion_cache_ler('noticias', SAFIRION_TTL);
    if ($guardado !== null) {
        safirion_responder($guardado, SAFIRION_TTL);
        exit;
    }

    $urls = [];
    foreach ($FEEDS as $i => $f) $urls[$i] = $f['url'];
    $r = safirion_buscar($urls, 7);

    $listas = [];
    foreach ($FEEDS as $i => $f) {
        $listas[$i] = [];
        if (empty($r[$i])) continue;
        $itens = preg_split('/<item[\s>]/i', $r[$i]);
        $itens = array_slice($itens === false ? [] : $itens, 1, 8);
        foreach ($itens as $b) {
            $titulo = safirion_tag($b, 'title');
            $link   = safirion_tag($b, 'link');
            if ($titulo === '' || $link === '') continue;
            $resumo = safirion_tag($b, 'description');
            if (mb_strlen($resumo, 'UTF-8') > 160) {
                $resumo = rtrim(mb_substr($resumo, 0, 157, 'UTF-8')) . '…';
            }
            $listas[$i][] = [
                'titulo' => $titulo,
                'link'   => $link,
                'fonte'  => $f['fonte'],
                'data'   => safirion_tag($b, 'pubDate') ?: null,
                'resumo' => $resumo,
            ];
        }
    }

    /* intercala as fontes para nenhuma dominar a lista */
    $saida = [];
    for ($i = 0; $i < 8; $i++) {
        foreach ($listas as $l) if (isset($l[$i])) $saida[] = $l[$i];
    }

    $json = json_encode(
        ['atualizado' => gmdate('Y-m-d\TH:i:s\Z'), 'noticias' => array_slice($saida, 0, 12)],
        JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
    );
    if ($json === false) throw new RuntimeException('json_encode falhou');

    safirion_cache_gravar('noticias', $json);
    safirion_responder($json, SAFIRION_TTL);
} catch (Throwable $e) {
    safirion_responder(
        json_encode(['erro' => true, 'atualizado' => gmdate('Y-m-d\TH:i:s\Z'), 'noticias' => []]),
        30
    );
}
