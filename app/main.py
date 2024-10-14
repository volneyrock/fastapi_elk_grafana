import json

import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


LOGSTASH_URL = "http://logstash:5044"


class Data(BaseModel):
    timestamp: str
    value: float
    message: str


def send_to_logstash(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        LOGSTASH_URL,
        data=json.dumps(data),
        headers=headers
    )

    if response.status_code == 200:
        print("Dados enviados com sucesso para o Logstash")
    else:
        print(f"Erro ao enviar dados para o Logstash: {response.status_code}")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/data")
def post_data(data: Data):
    send_to_logstash(data.model_dump())
    return {"message": "Data received"}
