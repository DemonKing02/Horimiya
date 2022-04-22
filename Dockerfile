FROM python:3.9.1-buster

WORKDIR /root/Flare_Robot

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","-m","Flare_Robot"]
