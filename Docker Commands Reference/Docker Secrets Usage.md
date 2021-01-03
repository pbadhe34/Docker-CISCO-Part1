https://docs.docker.com/engine/swarm/secrets/#intermediate-example-use-secrets-with-a-nginx-service

Docker secret commands
Use these links to read about specific commands, or continue to the example about using secrets with a service.

docker secret create
docker secret inspect
docker secret ls
docker secret rm
--secret flag for docker service create
--secret-add and --secret-rm flags for docker service update



Examples
This section includes three graduated examples which illustrate how to use Docker secrets. The images used in these examples have been updated to make it easier to use Docker secrets. To find out how to modify your own images in a similar way, see Build support for Docker Secrets into your images.

Note: These examples use a single-Engine swarm and unscaled services for simplicity. The examples use Linux containers, but Windows containers also support secrets in Docker 17.06 and higher.  

The top-level secrets declaration defines or references secrets that can be granted to the services in this stack. The source of the secret is either file or external.

    1.file: The secret is created with the contents of the file at the specified path.
    2.external: If set to true, specifies that this secret has already been created. Docker does not attempt to create it, and if it does not exist, a secret not found error occurs.
    -->name: The name of the secret object in Docker. This field can be used to reference secrets that contain special characters. The name is used as is and will not be scoped with the stack name. Introduced in version 3.5 file format.



Defining and using secrets in compose files
Both the docker-compose and docker stack commands support defining secrets in a compose file. 

To Add a secret to Docker. The docker secret create command reads standard input because the last argument, which represents the file to read the secret from, is set to -.

$ printf "This is a secret" | docker secret create my_secret_data 

Create a redis service and grant it access to the secret. By default, the container can access the secret at /run/secrets/<secret_name>, but you can customize the file name on the container using the target option.

$ docker service  create --name redis --secret my_secret_data redis:alpine

Verify that the task is running without issues using docker service ps. If everything is working, the output looks similar to this:

$ docker service ps redis

if there were an error, and the task were failing and repeatedly restarting, you would see something like this:

$ docker service ps redis


docker ps --filter name=redis -q

docker container exec $(docker ps --filter name=redis -q) ls -l /run/secrets

Verify that the secret is not available if you commit the container.

$ docker commit $(docker ps --filter name=redis -q) committed_redis

$ docker run --rm -it committed_redis cat /run/secrets/my_secret_data

Try removing the secret. The removal fails because the redis service is running and has access to the secret.


$ docker secret ls

docker secret rm my_secret_data

Remove access to the secret from the running redis service by updating the service.

$ docker service update --secret-rm my_secret_data redis

epeat steps 3 and 4 again, verifying that the service no longer has access to the secret. The container ID is different, because the service update command redeploys the service.

$ docker container exec -it $(docker ps --filter name=redis -q) cat /run/secrets/my_secret_data

cat: can't open '/run/secrets/my_secret_data': No such file or directory

Stop and remove the service, and remove the secret from Docker.

$ docker service rm redis

$ docker secret rm my_secret_data
