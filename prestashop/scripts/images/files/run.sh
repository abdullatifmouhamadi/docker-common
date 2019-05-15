#!/bin/sh

mkdir -p /usr/html
chown -R nginx:nginx /usr/html


echo "[i] Fixing permissions & ownership..."

find /usr/html/ -type f -exec chmod 644 {} \; && find /usr/html/ -type d -exec chmod 755 {} \;
chown -R nginx:nginx /usr/html

echo "[i] start php-fpm ..."

# start php-fpm
mkdir -p /usr/logs/php-fpm
php-fpm7


echo "[i] start nginx ..."
# start nginx
mkdir -p /usr/logs/nginx
mkdir -p /tmp/nginx
chown nginx /tmp/nginx
nginx
