from fastapi import FastAPI
from database import conexao
from def_database import inserir_no_bd, ver_dados, deletar_dado, update_data, in_on_database
from datetime import date
from utils import validate_cpf, valid_email, format_cpf
import json


app = FastAPI()


@app.post("/cadastrar_pessoa")
def cadastro_pessoa(first_name: str, last_name: str, cpf: str, email: str, dia: int, mes: int, ano: int):
    cpf = format_cpf(cpf)
    if in_on_database(cpf):
        return {"message": "Pessoa já cadastrada na base de dados."}
    if not validate_cpf(cpf):
        return {"message": "CPF inválido."}
    if not valid_email(email):
        return {"message": "E-mail inválido."}
    retorno = inserir_no_bd(first_name, last_name, cpf, email, dia, mes, ano)
    return retorno



@app.get("/Ver_pessoas")
def ver_pessoas(cpf):
    cpf = format_cpf(cpf)
    if not in_on_database(cpf):
        return json.dumps({"error": "Cpf não cadastrado na base de dados."})
    if not validate_cpf(cpf):
        return json.dumps({"error": "Por favor insira um cpf válido."})
    return json.dumps(ver_dados(cpf))


@app.delete("/Remover_Pessoa")
def deletar(cpf):
    cpf = format_cpf(cpf)
    if not in_on_database(cpf):
        return {"status": "error", "message": "CPF não cadastrado na base de dados"}
    if not validate_cpf(cpf):
        return {"status": "error", "message": "Por favor insira um CPF válido"}
    retorno = deletar_dado(cpf)
    if retorno:
        return {"status": "success", "message": "Usuário removido com sucesso"}
    else:
        return {"status": "error", "message": "Ocorreu um erro ao remover o usuário"}


@app.put("/att_info")
def atualiza_info(cpf: str, campo_alterado: str, novo_registro: str):
    cpf = format_cpf(cpf)
    if not in_on_database(cpf):
        return {"status": "error", "message": "CPF não cadastrado na base de dados"}
    if not validate_cpf(cpf):
        return {"status": "error", "message": "Por favor insira um CPF válido"}
    if not campo_alterado in ['email', 'first_name']:
        return {"status": "error", "message": "Campo alterado inválido"}
    retorno = update_data(cpf, campo_alterado, novo_registro)
    if retorno:
        return {"status": "success", "message": "Informações atualizadas com sucesso"}
    else:
        return {"status": "error", "message": "Ocorreu um erro ao atualizar as informações"}
