FROM python:3.8.10

RUN apt-get update -y

COPY ./ ./
COPY ./requirements.txt ./

WORKDIR ./

RUN pip install -r requirements.txt


ENTRYPOINT ["python3","main.py"]