from database import conexao


def inserir_no_bd(first_name, last_name, cpf, email, dia, mes, ano):
    from datetime import date
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
            return f'Parabéns, {first_name}, seu cadastro foi realizado com sucesso!'
        

def ver_dados():
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
        

def deletar_dado(cpf):
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
            return 'Seus dados foram deletados com sucesso.'
        
    
def update_data(cpf, campo_alterado, novo_registro):
    with conexao.cursor() as cursor:
        try:
            cursor.execute(
                f"""UPDATE pessoas 
                SET {campo_alterado} = '{novo_registro}' 
                WHERE cpf = '{cpf}';"""
            )
            conexao.commit()
        except Exception as erro:
            return erro
        else:
            return 'Alteração realizada com sucesso!'