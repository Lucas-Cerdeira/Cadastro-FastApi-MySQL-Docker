from fastapi import FastAPI
from database import conexao
from datetime import date

app = FastAPI()

@app.get("/Cadastro Pessoa")
def cadastro_pessoa(first_name, cpf, email, dia, mes, ano, last_name=None):
    from utils import validate
    if not validate(cpf):
        return False
    data_nascimento = date(ano, mes, dia)
    with conexao.cursor() as cursor:
        try:
            cursor.execute(
                'insert into pessoas (first_name, last_name, cpf, email, data_nascimento), values'
            )

    pass