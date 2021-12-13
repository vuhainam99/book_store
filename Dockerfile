FROM python:3.7.7

RUN pip install pymysql
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD manage.py /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN python manage.py makemigrations
# RUN python manage.py migrate

RUN apt-get update && apt-get install nodejs npm -y
RUN npm config set registry http://registry.npmjs.org/
RUN npm -g install yuglify
#RUN ln -s /usr/bin/nodejs /usr/bin/node

# TODO : install following module if you want support live reload js while development
# https://pypi.org/project/django-livereload/
#RUN pip install django-livereload 
