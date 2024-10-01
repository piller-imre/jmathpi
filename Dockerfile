FROM debian:12
MAINTAINER Imre Piller <imre.piller@uni-miskolc.hu>
LABEL Description="Debian 12, Apache, PHP"

RUN apt update
RUN apt install -y apache2

EXPOSE 80
CMD apache2ctl -D FOREGROUND

