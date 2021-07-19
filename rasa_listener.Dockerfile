FROM rasa/rasa
USER root

WORKDIR /app/
COPY . /app/

RUN pip install --no-cache-dir pymysql
# RUN pip install mysqlclient

CMD ["run"]