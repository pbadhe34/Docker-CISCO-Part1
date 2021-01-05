
Initialize the swarm node



Create a docker secret for mysql password

echo "MyDataPass" | docker secret create myPass -


The docker secrets stored in /run/secrets/<secret_name> files of the container
. For example:
docker run --name app-mysql -e MYSQL_ROOT_PASSWORD=myPass -d mysql:5.6

