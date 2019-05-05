# docker-common
My docker commons


## docker without sudo
```
sudo usermod -aG docker $USER
```

## docker basics
```
docker container run --publish 9095:80 nginx
docker container run --publish 9095:80 --detach nginx
docker container ls -a

docker container stop id
docker container logs id # --follow
docker container rm id
docker container top # process

docker container run -d -p 5050:5050 --name pgdb -e POSTGRES_PASSWORD=change_me_please -d postgres
docker container run --detach --publish 8080:80 --name webserver nginx
docker container stop pgdb webserver

docker ps
docker image ls
```

## Container stats
```
docker container start webserver
docker container top webserver
docker container inspect webserver
docker container stats webserver
```

## Shell inside a container
```
docker container run -it --name proxy nginx bash
docker container exec -it pgdb bash
docker pull archlinux/base
docker container exec -it arch bash
docker image ls
docker container run -it alpine sh
```


## Docker networks
```
docker container port webserver
docker container inspect --format '{{ .NetworkSettings.IPAddress}}' webserver

docker network ls
docker network inspect bridge
docker network create my_app_net
docker network ls

docker container run -d --name new_nginx --network my_app_net nginx
docker container inspect new_nginx
docker network inspect my_app_net
docker network connect net_1 net_2
docker network discounnect net_1 net_2

docker container run -d --name my_nginx --network my_app_net nginx
docker container exec -it my_nginx ping new_nginx
```


## CLI App Testing
```
docker contaner run --rm -it centos:7 bash
docker container run --rm -it ubuntu:14.04 bash
~ apt-get update && apt-get install -y curl
~ curl --version
```


## Container images
```
docker image ls
docker image tag nginx abdullatifmouhamadi/nginx
docker login
docker image push abdullatifmouhamadi/nginx
docker image tag abdullatifmouhamadi/nginx abdullatifmouhamadi/nginx:testing
```

## Building images
```
docker image build -t customnginx .
docker image build -t nginx-with-html .
docker container run -p 80:80 --rm nginx-with-html
```

## Persistent Data
1) "data volumes"
```
docker volume ls
docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True -v mysql-db:/var/lib/mysql mysql
docker volume create --help
```

2) "bind mounts"
```
docker container run -d --name nginx -p 80:80 -v $(pwd):/usr/share/nginx/html nginx
docker container exec -it nginx bash

docker container run -d --name psql -v psql:/var/lib/postgresql/data postgres:9.6.1

docker pull bretfisher/jekyll-serve
docker container run -p 80:4000 -v $(pwd):/site bretfisher/jekyll-serve
```

## Docker compose
```
docker-compose up -d
docker-compose logs
docker-compose ps
docker-compose top
docker-compose down
```
