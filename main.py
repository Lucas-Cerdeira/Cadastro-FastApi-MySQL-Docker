from fastapi import FastAPI
from database import conexao
from def_database import inserir_no_bd, ver_dados, deletar_dado, update_data
from datetime import date
from utils import validate_cpf, valid_email
import json


app = FastAPI()


@app.get("/Inserir_Pessoa")
def cadastro_pessoa(first_name: str, last_name: str, cpf: str, email: str, dia: int, mes: int, ano: int):
    if not validate_cpf(cpf):
        retorno = 'Por favor insira um cpf válido.'
        return retorno
    if not valid_email(email):
        retorno = 'Por favor insira um e-mail válido.'
        return retorno
    retorno = inserir_no_bd(first_name, last_name, cpf, email, dia, mes, ano)
    return retorno


@app.get("Ver_pessoas")
def ver_pessoas():
    dados = ver_dados()
    return dados


@app.delete("/Remover_Pessoa")
def deletar(cpf):
    if not validate_cpf(cpf):
        retorno = 'Por favor insira um cpf válido.'
        return retorno
    retorno = deletar_dado(cpf)
    return retorno


@app.put("/att_info")
def atualiza_info(cpf: str, campo_alterado: str, novo_registro: str):
    if not validate_cpf(cpf):
        retorno = 'Por favor insira um cpf válido.'
        return retorno
    if not campo_alterado in ['email', 'first_name']:
        return False
    retorno = update_data(cpf, campo_alterado, novo_registro)
    return retorno
