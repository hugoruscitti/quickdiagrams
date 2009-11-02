<?php
/**
 * Hugo Ruscitti <hugoruscitti@gmail.com> 
 *
 * based on Note plugin by Olivier Cortès <olive@deep-ocean.net>
 * under the terms of the GNU GPL v2.
 *
 * @license    GNU_GPL_v2
 * @author     Hugo Ruscitti <hugoruscitti@gmail.com>
 */
 
if(!defined('DOKU_INC')) define('DOKU_INC',realpath(dirname(__FILE__).'/../../').'/');
if(!defined('DOKU_PLUGIN')) define('DOKU_PLUGIN',DOKU_INC.'lib/plugins/');
require_once(DOKU_PLUGIN.'syntax.php');


#define(URL, "http://localhost:8080");
define(URL, "http://www.diagramadeclases.com.ar");


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





class syntax_plugin_classdiagram extends DokuWiki_Syntax_Plugin
{
    var $input_data = "";

    function getInfo(){
        return array(
            'author' => 'Hugo Ruscitti (basado en Note plugin de Olivier Cortès / Eric Hameleers / Christopher Smith)',
            'email'  => 'hugoruscitti@gmail.com',
            'date'   => '2009-10-05',
            'name'   => 'plugin_classdiagram',
            'desc'   => 'Show a class diagram',
            'url'    => 'code.google.com/p/quickdiagrams/'
        );
    }
 
 
    function getType()
    {
        return 'container';
    }

    function getPType()
    {
        return 'block';
    }

    function getAllowedTypes()
    { 
        return array('formatting', 'disabled');
    }

    function getSort()
    {
        return 195;
    }

    function connectTo($mode)
    {
        $pattern = '<classdiagram.*?>(?=.*?</classdiagram>)';
        $this->Lexer->addEntryPattern($pattern, $mode, 'plugin_classdiagram');
    }

    function postConnect()
    {
        $this->Lexer->addExitPattern('</classdiagram>','plugin_classdiagram');
    }
 
    function handle($match, $state, $pos, &$handler)
    {
        switch ($state)
        {
          case DOKU_LEXER_ENTER : 
            return array($state, $match);
 
          case DOKU_LEXER_UNMATCHED :
            return array($state, $match);
        
          default:
            return array($state);
        }
    }
 
    function render($mode, &$renderer, $indata) 
    {
        if($mode == 'xhtml')
        {
          list($state, $data) = $indata;

          switch ($state)
          {
            case DOKU_LEXER_ENTER :
              break;
  
            case DOKU_LEXER_UNMATCHED :
                $this->input_data .= $renderer->_xmlEntities($data) . "\n";
              break;
  
            case DOKU_LEXER_EXIT :

                #$dst = $this->input_data;
                $dst = $this->call_remote_service($this->input_data);
                $renderer->doc .= $dst;
                //"<PRE style='border: 1px solid red'>$dst</PRE>";

              break;
          }
          return true;
        }
        
        return false;
    } 

    function call_remote_service($input_data)
    {
        $url = URL;
        $data = array ('diagram_code' => $input_data);
        $data = http_build_query($data);

        try {
            $return = do_post_request("$url/draw", $data);
        } catch (Exception $e) {
            return 'Ha ocurrido un error con el servicio remoto: '.$e->getMessage();
        }

        return "<img src='$url/$return'/>";
    }
}
 
?>
