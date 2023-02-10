from database import conexao
import json


def inserir_no_bd(first_name, last_name, cpf, email, dia, mes, ano):
    from datetime import date
    with conexao.cursor() as cursor:
        try:
            cursor.execute(f"""INSERT INTO pessoas 
            (first_name, last_name, cpf, email, data_nascimento) 
            VALUES 
            ('{first_name}', '{last_name}', '{cpf}', '{email}', '{date(ano, mes, dia).isoformat()}');""")
        except Exception as erro:
            return erro
        else:
            retorno = f"Parabéns, {first_name}, seu cadastro foi realizado com sucesso!"
            return json.dumps(retorno)
        finally:
            conexao.commit()


def ver_dados(cpf):
    if not in_on_database(cpf):
        return "Cpf não cadastrado na base de dados."
    with conexao.cursor() as cursor:
        try:
            cursor.execute(
                f"""SELECT id, first_name, last_name
                FROM pessoas 
                WHERE cpf = '{cpf}'
                order by id;"""
            )
            dados = cursor.fetchone()
        except Exception as erro:
            return erro
        else:
            return dados


def in_on_database(cpf):
    with conexao.cursor() as cursor:
        try:
            cursor.execute(
                f"""SELECT id, first_name, last_name
                FROM pessoas 
                WHERE cpf = '{cpf}'
                order by id;"""
            )
            dados = cursor.fetchone()
            if dados == None:
                return False
        except Exception as erro:
            return erro
        else:
            return True


def deletar_dado(cpf):  # verificar se cpf está cadastrado
    with conexao.cursor() as cursor:
        try:
            cursor.execute(
                f"""DELETE FROM pessoas as p
                WHERE cpf = '{cpf}';"""
            )
        except Exception as erro:
            return erro
        else:
            return 'Seus dados foram deletados com sucesso.'
        finally:
            conexao.commit()


def update_data(cpf, campo_alterado, novo_registro):
    with conexao.cursor() as cursor:
        try:
            cursor.execute(
                f"""UPDATE pessoas 
                SET {campo_alterado} = '{novo_registro}' 
                WHERE cpf = '{cpf}';"""
            )
        except Exception as erro:
            return erro
        else:
            return 'Alteração realizada com sucesso!'
        finally:
            conexao.commit()
