FROM openjdk:11-jdk
LABEL version="0.1"
LABEL maintainer="Constantin Nica"
VOLUME /tmp

ARG DEPENDENCY=target/dependency
COPY ${DEPENDENCY}/BOOT-INF/lib /app/lib
COPY ${DEPENDENCY}/META-INF /app/META-INF
COPY ${DEPENDENCY}/BOOT-INF/classes /app
RUN ["bash", "-c", " echo 'Europe/Paris' > /etc/timezone"]
ENTRYPOINT ["java","-cp","app:app/lib/*","eu.europa.euvsvirus.EuVsVirus"]