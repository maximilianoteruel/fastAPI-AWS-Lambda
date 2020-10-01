# base ################################################################################################

FROM python:3.8.5-alpine3.12 as base

WORKDIR /usr/src/app

EXPOSE 8000

RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc libc-dev make \
    # bcrypt dependencies
    musl-dev gcc libffi-dev \
    # mysqlclient dependencies
    mysql-dev \
    # PIP
    && pip3 install --upgrade pip

COPY  docker/requirements/base.txt /usr/src/docker/requirements/base.txt

RUN pip3 install -r /usr/src/docker/requirements/base.txt

RUN addgroup -S noroot && adduser -S noroot -G noroot

COPY --chown=noroot:noroot docker /usr/src/docker

RUN chmod +x -R /usr/src/docker/scripts

ENTRYPOINT ["/usr/src/docker/scripts/entrypoint.sh"]


# dev ################################################################################################

FROM base as dev

RUN pip3 install -r /usr/src/docker/requirements/dev.txt

CMD ["/usr/src/docker/scripts/start.dev.sh"]


# prod ################################################################################################

FROM base as prod

COPY --chown=noroot:noroot . .

RUN pip3 install -r /usr/src/docker/requirements/prod.txt

USER noroot

CMD ["/usr/src/docker/scripts/start.prod.sh"]
