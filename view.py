import mysql.connector

# Conectando ao Banco de Dados
meubd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jo@o5570",
    database="listadetarefas"
)

cursor = meubd.cursor()


# Função para adicionar uma nova tarefa
def adicionar_tarefa(descricao):
    sql = "INSERT INTO tarefas (descricao) VALUES (%s)"
    val = (descricao,)
    cursor.execute(sql, val)
    meubd.commit()

# Função para listar todas as tarefas
def listar_tarefas():
    sql = "SELECT * FROM tarefas"
    cursor.execute(sql)
    return cursor.fetchall()

# Função para concluir uma tarefa
def concluir_tarefa(id):
    sql = "UPDATE tarefas SET concluido = True WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    meubd.commit()
    
# Função para remover uma tarefa
def remover_tarefa(id):
    sql = "DELETE FROM tarefas WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    meubd.commit()

# Função para remover todas as tarefas concluídas
def remover_tarefas_concluidas():
    cursor.execute("DELETE FROM tarefas WHERE concluido = 1")
    meubd.commit()
    
# Função para remover todas as tarefas não concluídas
def remover_tarefas_nao_concluidas():
    cursor.execute("DELETE FROM tarefas WHERE concluido = 0")
    meubd.commit()


# Função para remover todas as tarefas
def remover_todas_tarefas():
    cursor.execute("DELETE FROM tarefas")
    meubd.commit()
    

    
