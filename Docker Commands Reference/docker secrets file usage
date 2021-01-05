version: "3.1"
services:
mysql:
image: mysql/mysql-server:latest
container_name: mysql
environment:
MYSQL_ROOT_PASSWORD: /run/secrets/my_secret
secrets:
- my_secret

secrets:
my_secret:
file: ./my_secret.txt
