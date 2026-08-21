<?php
/**
 * Busca paralela com prazo, compartilhada pelos dois endpoints.
 *
 * No Worker isso era Promise.all com fetch. Aqui e curl_multi: sao ~20 chamadas
 * por atualizacao de cotacao, e sequencial elas somariam minutos.
 */
declare(strict_types=1);

function safirion_buscar(array $urls, int $timeout = 6): array
{
    if (!function_exists('curl_multi_init')) {
        return array_fill_keys(array_keys($urls), null);
    }
    $mh = curl_multi_init();
    $hs = [];
    foreach ($urls as $k => $u) {
        $ch = curl_init($u);
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_MAXREDIRS      => 3,
            CURLOPT_TIMEOUT        => $timeout,
            CURLOPT_CONNECTTIMEOUT => 4,
            CURLOPT_ENCODING       => '',
            CURLOPT_USERAGENT      => 'Mozilla/5.0 (compatible; SafirionBot/1.0)',
        ]);
        curl_multi_add_handle($mh, $ch);
        $hs[$k] = $ch;
    }
    $ativos = null;
    do {
        curl_multi_exec($mh, $ativos);
        if ($ativos > 0) curl_multi_select($mh, 0.2);
    } while ($ativos > 0);

    $saida = [];
    foreach ($hs as $k => $ch) {
        $corpo  = curl_multi_getcontent($ch);
        $codigo = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $saida[$k] = ($codigo >= 200 && $codigo < 300 && $corpo !== '') ? $corpo : null;
        curl_multi_remove_handle($mh, $ch);
        curl_close($ch);
    }
    curl_multi_close($mh);
    return $saida;
}

/** Cache em arquivo. O Worker usava o cache da Cloudflare; aqui nao ha. */
function safirion_cache_ler(string $nome, int $ttl): ?string
{
    $f = sys_get_temp_dir() . '/safirion-' . $nome . '.json';
    if (is_readable($f) && (time() - (int) filemtime($f)) < $ttl) {
        $c = file_get_contents($f);
        if ($c !== false && $c !== '') return $c;
    }
    return null;
}

function safirion_cache_gravar(string $nome, string $conteudo): void
{
    @file_put_contents(sys_get_temp_dir() . '/safirion-' . $nome . '.json', $conteudo, LOCK_EX);
}

function safirion_responder(string $json, int $ttl): void
{
    header('Content-Type: application/json; charset=utf-8');
    header('Access-Control-Allow-Origin: *');
    header('Cache-Control: public, max-age=' . $ttl);
    echo $json;
}
