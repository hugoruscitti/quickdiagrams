<?php

/*
 * Emite un pedido post sin utilizar bibliotecas adicionales.
 *
 * Extraido de: http://netevil.org/blog/2006/nov/http-post-from-php-without-curl
 */
function do_post_request($url, $data, $optional_headers = null)
{
   $params = array('http' => array(
                'method' => 'POST',
                'content' => $data
             ));
   if ($optional_headers !== null) {
      $params['http']['header'] = $optional_headers;
   }
   $ctx = stream_context_create($params);
   $fp = @fopen($url, 'rb', false, $ctx);
   if (!$fp) {
      throw new Exception("Problem with $url, $php_errormsg");
   }
   $response = @stream_get_contents($fp);
   if ($response === false) {
      throw new Exception("Problem reading data from $url, $php_errormsg");
   }
   return $response;
}





function main()
{
    $url = "http://www.diagramadeclases.com.ar";
    $data = array ('diagram_code' => "Hello\n\tname");
    $data = http_build_query($data);
    try {
        $return = do_post_request("$url/draw", $data);
    } catch (Exception $e) {
        echo 'Ha ocurrido un error con el servicio remoto: '.$e->getMessage();
        return;
    }



    echo "Se ha creado el diagrama:\n";
    echo "$url/$return";
}

main();

?>
