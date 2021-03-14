<?php 

ini_set('display_errors', '0');
ini_set('display_startup_errors', '0');
#error_reporting(E_ALL);

function requestedByTheSameDomain() {
    $myDomain       = $_SERVER['SCRIPT_URI'];
    $requestsSource = $_SERVER['HTTP_REFERER'];
    
    $left = parse_url($myDomain, PHP_URL_HOST);
    $right = parse_url($requestsSource, PHP_URL_HOST);
    $same_domain = ($left === $right);
    $nonce_matches = ($_SERVER['HTTP_NONCE'] === "JIYr435smMmKG1nAAFNlrKUewAEaTWt1");
    $is_browser_user_agent = strlen($_SERVER["HTTP_USER_AGENT"]) > 30;
    # NGINX would only replace **CSP_NONCE** in response given to client
    #echo "Left: [" . $left . "] === Right [" . $right . "]\n";
    #echo "\n **CSP_NONCE** === " . $_SERVER['HTTP_NONCE'];
    #echo "\nConditions: [$same_domain " . "$nonce_matches]";
    return $same_domain && $nonce_matches && $is_browser_user_agent;
}
#print_r($_SERVER);
if ( requestedByTheSameDomain() ) {
  #echo getenv("BTS_FLAG");
  readfile("/flag.txt");
}
?> 
