from fastapi import FastAPI
from database import conexao
from datetime import date

app = FastAPI()

@app.get("/Cadastro Pessoa")
def cadastro_pessoa(first_name:str, cpf:str, email:str, dia:int, mes:int, ano:int, last_name:str=None):
    from utils import validate
    if not validate(cpf):
        return False
    with conexao.cursor() as cursor:
        try:
            cursor.execute(f"""INSERT INTO pessoas (first_name, last_name, cpf, email, data_nascimento) 
            VALUES ('{first_name}', '{last_name}', '{cpf}', '{email}', '{date(ano, mes, dia).isoformat()}');""")
            conexao.commit()
            return True
        except Exception as erro:
            return erro

        