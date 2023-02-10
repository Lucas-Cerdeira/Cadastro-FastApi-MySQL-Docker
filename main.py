from fastapi import FastAPI
from database import conexao
from def_database import inserir_no_bd, ver_dados, deletar_dado, update_data, in_on_database
from datetime import date
from utils import validate_cpf, valid_email
import json


app = FastAPI()


@app.get("/Inserir_Pessoa")
def cadastro_pessoa(first_name: str, last_name: str, cpf: str, email: str, dia: int, mes: int, ano: int):
    if not in_on_database(cpf):
        return json.dumps("Cpf não cadastrado na base de dados.", ensure_ascii=False)
    if not validate_cpf(cpf):
        return json.dumps("Por favor insira um cpf válido.", ensure_ascii=False)
    if not valid_email(email):
        return json.dumps("Por favor insira um e-mail válido.")
    retorno = inserir_no_bd(first_name, last_name, cpf, email, dia, mes, ano)
    return json.dumps(retorno)


@app.get("/Ver_pessoas")
def ver_pessoas(cpf):
    if not in_on_database(cpf):
        return json.dumps("Cpf não cadastrado na base de dados.", ensure_ascii=False)
    if not validate_cpf(cpf):
        return json.dumps("Por favor insira um cpf válido.", ensure_ascii=False)
    return json.dumps(ver_dados(cpf))


@app.delete("/Remover_Pessoa")
def deletar(cpf):
    if not in_on_database(cpf):
        return json.dumps("Cpf não cadastrado na base de dados.", ensure_ascii=False)
    if not validate_cpf(cpf):
        return json.dumps("Por favor insira um cpf válido.", ensure_ascii=False)
    retorno = deletar_dado(cpf)
    return json.dumps(retorno)


@app.put("/att_info")
def atualiza_info(cpf: str, campo_alterado: str, novo_registro: str):
    if not in_on_database(cpf):
        return json.dumps("Cpf não cadastrado na base de dados.", ensure_ascii=False)
    if not validate_cpf(cpf):
        return json.dumps("Por favor insira um cpf válido.", ensure_ascii=False)
    if not campo_alterado in ['email', 'first_name']:
        return False
    retorno = update_data(cpf, campo_alterado, novo_registro)
    return json.dumps(retorno, ensure_ascii=False)
