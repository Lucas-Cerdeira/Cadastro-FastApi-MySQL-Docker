from database import conexao
import json


def inserir_no_bd(first_name, last_name, cpf, email, dia, mes, ano):
    from datetime import date
    data_nascimento = date(ano, mes, dia).isoformat()
    mensagem_sucesso = f"Parabéns, {first_name}, seu cadastro foi realizado com sucesso!"
    with conexao.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO pessoas (first_name, last_name, cpf, email, data_nascimento) VALUES (%s, %s, %s, %s, %s);",
                (first_name, last_name, cpf, email, data_nascimento)
            )
        except Exception as erro:
            return erro
        else:
            return json.dumps({"status": "success", "mensagem": mensagem_sucesso}, ensure_ascii=False)
        finally:
            conexao.commit()


def ver_dados(cpf):
    if not in_on_database(cpf):
        return json.dumps({"mensagem": "Cpf não cadastrado na base de dados."}, ensure_ascii=False)

    with conexao.cursor() as cursor:
        cursor.execute(
            "SELECT id, first_name, last_name FROM pessoas WHERE cpf = %s order by id", (
                cpf,)
        )
        dados = cursor.fetchone()

        if not dados:
            return json.dumps({"mensagem": "Não foi encontrado nenhum registro com esse CPF."}, ensure_ascii=False)
        else:
            return json.dumps({"status": "success", "mensagem": dados}, ensure_ascii=False)


def in_on_database(cpf):
    with conexao.cursor() as cursor:
        cursor.execute(
            f"SELECT id, first_name, last_name FROM pessoas WHERE cpf = %s order by id", (
                cpf,)
        )
        dados = cursor.fetchone()
        if dados:
            return True
        else:
            return False


def deletar_dado(cpf):
    if not in_on_database(cpf):
        return json.dumps({"mensagem": "Cpf não cadastrado na base de dados."}, ensure_ascii=False)

    with conexao.cursor() as cursor:
        cursor.execute(
            "DELETE FROM pessoas WHERE cpf = %s", (cpf,)
        )
        conexao.commit()

        return json.dumps({"status": "success", "mensagem": "Seus dados foram deletados com sucesso."}, ensure_ascii=False)


def update_data(cpf, campo_alterado, novo_registro):
    with conexao.cursor() as cursor:
        cursor.execute(
            "UPDATE pessoas SET {} = %s WHERE cpf = %s".format(campo_alterado),
            (novo_registro, cpf)
        )
        conexao.commit()
        return json.dumps({"status": "success", "mensagem": "Alteração realizada com sucesso!"}, ensure_ascii=False)
