FROM webdevops/php-nginx 

COPY html/ /usr/share/nginx/html/
COPY conf/* /etc/nginx/

EXPOSE 80 443
# SET flag
ENV replaceFlagFile="/etc/nginx/nginx.conf"
COPY flag.txt /flag.txt
RUN flag=$(head -n 1 /flag.txt) && sed "s/--FLAG--/$flag/" $replaceFlagFile | sponge $replaceFlagFile
