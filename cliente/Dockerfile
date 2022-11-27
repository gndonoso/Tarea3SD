FROM bitnami/python:3.8.13

WORKDIR /cliente

COPY requirements.txt /cliente

RUN pip3 install -r requirements.txt

ENV FLASK_APP=api_cliente.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 8000
COPY . .
CMD ["flask", "run"]