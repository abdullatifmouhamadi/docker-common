FROM alpine:3.9.4
LABEL maintainer="ABDULLATIF Mouhamadi <abdullatif.mouhamadi@gmail.com>"

ENV URL="www.example.com" \
    PS_FOLDER_ADMIN="console" \
    PS_FOLDER_INSTALL="install" \
    PS_INSTALL_AUTO="1" \
    PS_ERASE_DB="0" \
    CLOUDFLARE_CDN="0" \
    MYSQL_HOST="172.17.0.2" \
    MYSQL_DATABASE="" \
    MYSQL_USER="" \
    MYSQL_PASSWORD=""

RUN apk update && \
    apk add bash nano less vim geoip nginx nginx-mod-http-headers-more nginx-mod-http-geoip nginx-mod-stream nginx-mod-stream-geoip ca-certificates git tzdata zip \
    libmcrypt-dev zlib-dev gmp-dev \
    freetype-dev libjpeg-turbo-dev libpng-dev \
    php7-fpm php7-json php7-zlib php7-xml php7-pdo php7-phar php7-openssl php7-fileinfo php7-imagick \
    php7-pdo_mysql php7-mysqli php7-session \
    php7-gd php7-iconv php7-mcrypt php7-gmp php7-zip \
    php7-curl php7-opcache php7-ctype php7-apcu php7-memcached \
    php7-intl php7-bcmath php7-dom php7-mbstring php7-simplexml php7-soap php7-tokenizer php7-xmlreader mysql-client curl && apk add -u musl && \
    rm -rf /var/cache/apk/*

RUN sed -i "s/nginx:x:100:101:nginx:\/var\/lib\/nginx:\/sbin\/nologin/nginx:x:100:101:nginx:\/usr:\/bin\/bash/g" /etc/passwd && \
    sed -i "s/nginx:x:100:101:nginx:\/var\/lib\/nginx:\/sbin\/nologin/nginx:x:100:101:nginx:\/usr:\/bin\/bash/g" /etc/passwd- && \
    ln -s /sbin/php-fpm7 /sbin/php-fpm

VOLUME ["/usr/html"]

COPY app/ /usr/html/

ADD files/nginx.conf /etc/nginx/
ADD files/php-fpm.conf /etc/php7/
ADD files/php.ini /etc/php7/


ADD files/startup.php /usr/html/
RUN chmod +x /usr/html/startup.php

ADD files/run.sh /
RUN chmod +x /run.sh

EXPOSE 80

CMD ["/run.sh"]