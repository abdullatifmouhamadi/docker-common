# Datastore for mariadb datastore

-> mariadb

# images

https://hub.docker.com/_/mariadb

mariadb:10.4

# Connecting to MariaDB from Outside the Container

```
# run container and find db ip
docker run --name test-mariadb --net my_app_net --ip 172.18.0.2 -v test-mariadb:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=1234 -d mariadb:10.4
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' test-mariadb

# grant access to remote host
docker container exec -it test-mariadb bash
mysql -u root -p
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '1234' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'172.18.0.%' IDENTIFIED BY '1234' WITH GRANT OPTION;

# connecting from remote host
mysql -h 172.18.0.2 -P 3306 --protocol=TCP -u root -p
mysql -h 172.18.0.2 -P 3306 -u root -p

# erase
docker container stop test-mariadb && docker container rm test-mariadb && docker volume rm test-mariadb

```

https://forums.docker.com/t/configuring-mariadb-in-a-container-for-remote-client-access/8761/4

https://mariadb.com/kb/en/library/installing-and-using-mariadb-via-docker/

# docker-compose
