FROM rasa/rasa

WORKDIR /app/
COPY . /app/

CMD ["run"]