import pymysql


conexao = pymysql.connect(
    host='localhost',
    user='lucas',
    passwd='lucas123',
    database='cadastro_pessoas',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

