FROM tomcat:8.0-jre8 

##RUN apt-get update && apt-get -y upgrade

WORKDIR /usr/local/tomcat

ADD tomcat-users.xml $CATALINA_HOME/conf 

ADD server.xml $CATALINA_HOME/conf 

ADD user-service.war $CATALINA_HOME/webapps 

EXPOSE 8090
