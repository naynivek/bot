FROM bot-surebet-base:1.0

#RUN apt-get install -y python-pip python-dev

WORKDIR /app
COPY . .
RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot-surebet.py"]

