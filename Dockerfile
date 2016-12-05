FROM ubuntu:14.04
MAINTAINER yuzhou@alauda.io

RUN apt-get update \
    && apt-get install -y python-pip

RUN mkdir /logtesting

COPY . /logtesting

RUN chmod +x /logtesting/*

WORKDIR /logtesting

CMD ["/logtesting/run.sh"]
