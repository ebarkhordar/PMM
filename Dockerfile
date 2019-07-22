FROM python:3.7


ENV TZ 'Asia/Tehran'

RUN apt-get update
RUN cp /usr/share/zoneinfo/Asia/Tehran /etc/localtime && \
    echo $TZ > /etc/timezone

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./ ./

COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

#RUN  /code/docker-entrypoint.sh
RUN ["chmod", "+x", "/code/docker-entrypoint.sh"]

#RUN ["/code/docker-entrypoint.sh"]
ENTRYPOINT ["/code/docker-entrypoint.sh"]