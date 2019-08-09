FROM python:3.6.2
LABEL maintainer mark
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_api
WORKDIR /web_api
#COPY ./api_data /docker_api/
RUN apt-get update
RUN apt-get install vim -y -q
RUN echo "syntax on" >> /etc/vim/vimrc
RUN echo "colorscheme evening" >> /etc/vim/vimrc
RUN echo "set nu" >> /etc/vim/vimrc
RUN pip install --upgrade pip
RUN pip install django
RUN pip install psycopg2
RUN pip install django-bootstrap3
#RUN pip install -r requirements.txt
RUN echo "alias ll='ls -al'" >> /etc/bash.bashrc
#RUN django-admin startproject mysite
#WORKDIR /docker_api/mysite
