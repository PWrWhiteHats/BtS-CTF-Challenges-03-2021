FROM webdevops/php-nginx 

COPY html/ /usr/share/nginx/html/
COPY conf/* /etc/nginx/

EXPOSE 80 443
COPY flag.txt /flag.txt
#ENV BTS_FLAG=$(head -n 1 /flag.txt)