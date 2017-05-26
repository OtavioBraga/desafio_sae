FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /estoque
WORKDIR /estoque
ADD requirements.txt /estoque/
RUN pip install -r requirements.txt
ADD . /estoque/
WORKDIR /estoque