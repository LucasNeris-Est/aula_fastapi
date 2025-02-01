from fastapi import FastAPI

app = FastAPI()

@app.get("/teste")
def hello_world():
    return {
        "mensagem": "Hello world"
    }

# Criando endpoint para receber dois números e retornar a soma
@app.get("/soma/{numero1}/{numero2}")
def soma(numero1:int, numero2:int):
    total = numero1 + numero2
    return {"total": total}

# Passando o número 1 e 2 no corpo da requisição
@app.get("/soma_formato2")
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}
