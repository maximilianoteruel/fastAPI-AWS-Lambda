FROM python:3.8.6-slim-buster

WORKDIR /usr/src/app

EXPOSE 8000

ENV PYTHONPATH=/usr/src/app

RUN pip3 install --upgrade pip

COPY  ./requirements.txt ./requirements.txt

RUN pip3 install -r ./requirements.txt

COPY  ./scripts /usr/src/scripts

RUN chmod +x -R /usr/src/scripts
# CMD ["/bin/bash", "-c", "--", "while true; do sleep 30; done;"]   

CMD ["/usr/src/scripts/init.sh"]
