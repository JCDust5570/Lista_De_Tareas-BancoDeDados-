import mysql.connector

meubd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jo@o5570",
    database="listadetarefas"
)
cursor = meubd.cursor()

# Criar uma nova tabela
cursor.execute("CREATE TABLE IF NOT EXISTS tarefas(id INT AUTO_INCREMENT PRIMARY KEY, descricao VARCHAR(255), concluido BOOLEAN NOT NULL DEFAULT FALSE)")
