FROM python:3.8-slim

#RUN apt-get install -y python-pip python-dev

WORKDIR /app
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y python-pip python-dev \
    wget \
    curl

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable


RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#CMD ["python", "bot-surebet.py"]

