from fastapi import FastAPI
from database import conexao
from datetime import date
from utils import validate


app = FastAPI()


@app.get("/Cadastro/Inserir_Pessoa")
def cadastro_pessoa(first_name: str, cpf: str, email: str, dia: int, mes: int, ano: int, last_name: str = None):
    if not validate(cpf):
        return False
    with conexao.cursor() as cursor:
        try:
            cursor.execute(f"""INSERT INTO pessoas 
            (first_name, last_name, cpf, email, data_nascimento) 
            VALUES 
            ('{first_name}', '{last_name}', '{cpf}', '{email}', '{date(ano, mes, dia).isoformat()}');""")
            conexao.commit()
        except Exception as erro:
            return erro
        else:
            return True


@app.get("/Cadastro/Ver_pessoas")
def ver_pessoas():
    with conexao.cursor() as cursor:
        try:
            cursor.execute(
                f"""SELECT id, first_name, last_name
                FROM pessoas 
                order by id;"""
            )
            dados = cursor.fetchall()
        except Exception as erro:
            return erro
        else:
            return [registro for registro in dados]


@app.delete("/Cadastro/Remover_Pessoa")
def deletar(cpf):
    if not validate(cpf):
        return False
    with conexao.cursor() as cursor:
        try:
            cursor.execute(
                f"""DELETE FROM pessoas as p
                WHERE cpf = '{cpf}';"""
            )
            conexao.commit()
        except Exception as erro:
            return erro
        else:
            return True


@app.put("/Cadastro/Atualiza_Informações")
def atualiza_info(cpf: str, campo_alterado: str, novo_registro: str):
    if not validate(cpf):
        return False
    if not campo_alterado in ['email', 'first_name']:
        return False
    with conexao.cursor() as cursor:
        cursor.execute(
            f"""UPDATE FROM pessoas SET {campo_alterado} = '{novo_registro}' WHERE cpf = '{cpf}';"""
        )
