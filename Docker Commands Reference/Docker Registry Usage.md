https://blog.docker.com/2013/07/how-to-use-your-own-registry/

Run a local registry
Use a command like the following to start the registry container:

$ docker run -d -p 5000:5000 --restart=always --name registry registry:2

Copy an image from Docker Hub to your own registry
You can pull an image from Docker Hub and push it to your registry.
 
The following pulls the ubuntu:16.04 image from Docker Hub and re-tags it as my-ubuntu, then pushes it to the local registry. Finally, the ubuntu:16.04 and my-ubuntu images are deleted locally and the my-ubuntu image is pulled from the local registry.

Pull the ubuntu:16.04 image from Docker Hub.

$ docker pull ubuntu:16.04

docker pull busybox

docker pull --all-tags fedora

 ***********************

Attach console for multiple uses

docker run -a stdin -a stdout -i -t ubuntu /bin/bash

docker run -a stdin -a stdout -a stderr ubuntu /bin/ls

*********************
Tag the local image as localhost:5000/my-ubuntu. This creates an additional tag for the existing image.

  
When the first part of the tag is a hostname and port, Docker interprets this as the location of a registry, when pushing.

$ docker tag ubuntu:16.04 localhost:5000/my-ubuntu

  docker tag pbadhe34/my-apps:app1 localhost:5000/my-app

Push the image to the local registry running at localhost:5000:

$ docker push localhost:5000/my-app

docker images --format "{{.ID}}: {{.Repository}} {{.Tag}}"

Remove the locally-cached   localhost:5000/my-app  images, so that you can test pulling the image from your registry. 

This does not remove the localhost:5000/my-app image from your registry.

http://localhost:5000/v2/

http://172.17.0.2:5000/v2/_catalog

  curl http://172.17.0.2:5000/v2/_catalog
  List image tags

 
curl http://172.17.0.2:5000/v2/my-app/tags/list

  {"name":"my-app","tags":["latest"]}

  Tot fetch he image manifest   with the following url:

  http://172.17.0.2:5000/v2/my-app/manifests/latest

  
  Deleting an Image on local regsirty

An image may be deleted from the registry via its name and reference. A delete can be issued with the delete method and  request format:

 DELETE /v2/<name>/manifests/<reference>

  DELETE /v2/my-app/manifests/latest





$ docker image remove pbadhe34/my-apps:app1
$ docker image remove localhost:5000/my-app
******************************************
 To search in docker-hub
docker search busybox

**********************
  docker search localhost:5000/my-app

docker exec -it 2f01f0eb343c ls -a /var/lib/registry/docker/registry/v2/repositories/


NOW DISCONNECT YOUR INTERNET CONNECTION WIFI OR LAN

Pull the localhost:5000/my-app image from your local registry.

$ docker pull localhost:5000/my-app


   docker image ls
  docker run -d localhost:5000/my-app

Stop a local registry
To stop the registry, use the same docker container stop command as with any other container.

$ docker container stop registry
To remove the container, use docker container rm.

$ docker container stop registry && docker container rm -v registry

****************
