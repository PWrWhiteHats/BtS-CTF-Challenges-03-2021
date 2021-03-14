# Request for proxies

_Author: [xxzxcuzx-me](https://github.com/xxzxcuzx-me)


I got tired of all those content restrictions on public WiFi or universities' networks, so I created this simple website to facilitate bypassing them. In fact it's so simple that there is no way anyone could possibly abuse it. All of my secrets will remain safe, hidden on the side of the server.

## Flag

```
bts{tempflag}
```

## How to run

Easiest way to set it up is using Docker. Just change the flag in `flag_webserver/index.php` and start the container using command:
```
docker build --tag forgery:1.0 . && docker run -p 80:80 forgery:1.0
```

## Solution

Check in [solution folder](./solution/README.md)
