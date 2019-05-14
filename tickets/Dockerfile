FROM openjdk

WORKDIR /app

COPY . /app

EXPOSE 8080

ARG JAR_FILE=target/flights-1.0-SNAPSHOT.jar

ADD ${JAR_FILE} flights-1.0-SNAPSHOT.jar

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","target/flights-1.0-SNAPSHOT.jar"]
