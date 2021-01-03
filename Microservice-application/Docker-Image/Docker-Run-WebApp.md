 

 
 
******************************************

To build the war webapp as container image  

docker build -t web-app -f Dockerfile-Tomcat-War.txt .

 To build with version tag

docker build -t web-app:v1 -f Dockerfile-Tomcat-War.txt .

To Run the web-app image in detacheed mode with host port mapping/forwarding  

docker run -p 9090:9090 --name user-app -d web-app  

Check the application log by
 
docker logs web-app
 
Open in browser  

http://localhost:9090/webapp/info
http://192.168.1.208:9090/webapp/info

 
After successful testing of user-web-app, push this image to    docker-hub

 docker tag web-app  pbadhe34/training:webapp
 docker login

 docker push pbadhe34/training:webapp

docker run -p 1090:9090 --name user-app1 -d pbadhe34/training:webapp


**********************************



 