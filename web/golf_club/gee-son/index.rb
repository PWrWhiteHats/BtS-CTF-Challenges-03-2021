#!/usr/bin/env ruby

require 'webrick'
require 'webrick/https'
require 'jwt'
# require 'pry'

require './cert_stuff.rb'

$https_port = 8443
$flag = 'BtS-CTF{3z3_g5oN_mAN1pulAti0n_7f774de6}'

$ssl_key, $ssl_cert = generate_cert

def render( template, message )
  x = File.read("#{template}.html")
  x.gsub!('TEMPLATE_PLACEHOLDER',message)
  return x
end

def generate_user_cookie()
  payload = { 'username' => 'virgin_noob' }
  meta = {'typ'=>'JWT'}
  token = JWT::encode(payload, $ssl_key, 'RS256', meta)
  
  cookie = WEBrick::Cookie.new('sessionid',token);

  return cookie
end  

def get_user_session(cookie)
  return { 'username' => 'virgin_noob' } if cookie.nil?
  token = cookie.value
  begin
    session,meta = JWT::decode(token,$ssl_key,true, { algorithm: 'RS256' } )
  rescue => e
    session = { 'username'=>'virgin_noob' }
  end
  return session
end

def prepare_web_server
  http_server = WEBrick::HTTPServer.new(
    :Port => $https_port,
    :SSLEnable => true,
    :SSLVerifyClient => OpenSSL::SSL::VERIFY_NONE,
    :SSLPrivateKey => $ssl_key,
    :SSLCertificate => $ssl_cert
  )

  http_server.mount_proc '/' do |req, resp|
    session = get_user_session(req.cookies[0])

    resp.status = 200
    resp.cookies << generate_user_cookie()
    if session['username'] === 'chad_admin' then
      resp.body = render('index', "
        <h1> C0NGRATZ </h1>
        Here goes flag: <span style=\"font-size:2em; background-image: linear-gradient(to left, violet, indigo, blue, green, yellow, orange, red); -webkit-background-clip: text; color: transparent;\">#{$flag}</span>
      ")
    else
      junk = "0%C2%82%02%C3%B40%C2%82%01%C3%9C%C2%A0%03%02%01%02%02%01%020%0D%06%09*%C2%86H%C2%86%C3%B7%0D%01%01%0B%05%000%221%200%1E%06%0A%09%C2%92&%C2%89%C2%93%C3%B2,d%01%19%16%10%a0%1E%17%0D210202211038Z%17%0D%22%06%0A%09%C2%92&%C2%89%C2%93%C3%B2,d%01%19%n0%C2%82%01%22%0D%06%09*%C2%86H%C2%86%C3%B7%0D%01%01%01%05%00%03%C2%82%01%0F%000%C2%82%01%0A%02%C2%82%01%01%00%C3%89(D(%00%C2%8B%C3%95%C2%9A%1D%C2%A79%C3%96%C3%8DX%C3%8BQ%C3%AC%20%1D%C2%9C%1A%C2%9F%C2%B0%C2%AF%C3%8C%04%C2%B7%1DB7"
      resp.body = render('index', "
        <h2>Welcome fellow hacker!</h2>
        <article>
          You're now logged in as #{session['username']}. Log in to 'chad_admin' to get the flag.
        </article>
        <article>
          If you have any questions or suggestions, you can reach me at: <a href=\"mailto:chad_admin@bts.ctf?cc=another_chad@bts.ctf,anotheremail@example.com&bcc=lastemail@example.com&subject=Mail about your Website&body=Remeber to encrypt every mail you send to us using the key: #{URI::encode_www_form_component($ssl_key.export)}%0d%0aSincerely Yours,%0d%0aVirgin%20Noob\">chad_admin@bts.ctf</a>
      ")
    end
  end

  return http_server
end

prepare_web_server().start
