FROM ubuntu:16.04

LABEL maintainer="ys555han@gmail.com"

ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y --no-install-recommends apt-utils python3 python3-pip python3-setuptools python3-wheel gcc git dos2unix

RUN python3 -m pip install pip -U
RUN python3 -m pip install setuptools -U

ADD . /home/flaskapp

# 기본설정들
EXPOSE 5000

ENV DBUSER root
ENV DBPASS root1234

# 작업 디렉토리로 이동
WORKDIR /home/flaskapp

RUN pip3 install -r requirements.txt
RUN dos2unix wait-for-db.sh

# CMD python3 app.py
