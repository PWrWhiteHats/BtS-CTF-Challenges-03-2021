require 'jwt'
require 'pry'
require 'openssl'

pemkey = '-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAsHXTovhvOghF96TflW7aF9f5CGeR8ESUNRJfU/XPBeO9wFtb
uV3B0nFH7ubIPGINyz9QEBxcS6Oi/wQuXGc+Y/VoH4KlzmzHnmVMyHaHI/WGzOij
4qE51QHfhoeUu/nhdXAY2dqa2Z6rj4OSBhSFKbHdMtj81C7/Vcrz/g1/rK1PZAix
+tIuciD3YkC3eKNggKzm9CCWKzwS0q6VtTLM4+NDNXfqZZouyNKcoT+Iuu5TH6uy
BBNuraU4BlsQFLAGDdTW5NbFLZYM4u+GUcBJqVaOtsBITuvhK7xTTpilIJ95GaHK
ulsA3OKdOzd/a+QmhSiiA2eHNv6/xJcZVOwPDwIDAQABAoIBAQCWtivp11H4OLS5
jEHB+YmgL7/s47iLg6cppOVyalFE8HxSXDT9Hwy51jLf4pBGsmChpROWjwJtP/eo
40NNfIiXCzTBJO7EXbgomtB3rnRBzCQzwsame5lPSmhFGGt6GTPs/67Z8pGrKI/S
5UbElqYdNGJ+WUGnX/SIq+y0oYbYTUpwR+SJw13+dKoqS70hXHpEdLLIAUw+whvJ
jXB+1N9rnhuirZkFaaMLUcRlDRMOQB5LBhrQSLay1TdZamj6bRDuYaShQNFZDDyW
TgWsv8tMjLCybdwnyt4Hh/UNUxhav7GuiRQmPFbCzSmjC8T8Nu/5HTjjq3J9IAYP
fUe/HY/BAoGBANtwuS6dgnSNCMPWM97CrYuKu0Uh8Qmm+WPXorAWdVaHOF8rm1qh
W+C8w8aC68G56y2wx7FkF6ArOEYzJKTgJNdzzVprsm8/f1aTezA7rxYooFQpWBq+
stNlkaFh1LS+yOaxN2Upj691opmpSVEfHBTy4PIRBs15rQkHmv+LmFOxAoGBAM3b
+Y3W6djJFUV9Qn814mMHfiTusmf987Ieodq3Km4/Cs+LoDqJ07PSkudSB3QUU1rN
IaVAs01fa4RQIrt+pOgZK95oO0FsP1q6ImMwwshoK5I7PGgK2nk7gYHslO75Z8xq
8iVRyWbUa8yTomyli51Ua/38XWw3F5155M55/P6/AoGAOvlvezyvi70/hsoxhIOT
enYdYDX//pUWXyPbwDE49bk/iCxDAzdsZti0UMxsqdLahpwE/wKkatJSvGMQTRNE
M3cW0F8zRDyvb0gRimPv6Sef9x5pZD6t9qxMWC/fp3fCrGUiOxjRWdlmip95acjP
lj20ALpctqolu9CEcntEw/ECgYEAjzm2Ni5Jwu+coh1VT6aQ3O+Qn2eHrvysOchA
OijoF447Gk197FyKc3lVhiW3U9b0a59/AjeyyGlUJ9mNYL/rQiSJNhN07r6+kYQh
erupOb/oWLRoAcdTW7fAEkIlGONjiYD6+mYd5zJx0gMBpe/D5HGhNTQJV8o43vK4
88NB94cCgYEAu7DWODgwPCST3J9jCI3ocnvPlagj4cLxw5h420kZXsWV/ZFWQsPs
kZNMClBDTlsH0Iw/T23lKt5pdL58LxpvP9h+1psVR0y8tHXfMqeYG8WGheWssUbM
HlVexO6ROyhL6Srb/rxP6aHbsQdWV4lvnESwx5ydIdipEukRNWEVOuw=
-----END RSA PRIVATE KEY-----'

key = OpenSSL::PKey::RSA.new pemkey
payload = { 'username' => 'chad_admin' }
meta = {'typ'=>'JWT'}
token = JWT::encode(payload, key, 'RS256', meta)

puts token

binding.pry