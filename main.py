import mysql.connector
from view import *
from BancoDeDados import *

# Conectando ao Banco de Dados
meubd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jo@o5570",
    database="listadetarefas"
)


cursor = meubd.cursor()

input_usuario = ""


while input_usuario != "0":
    print("Bem vindo ao seu gerenciador de tarefas!")
    print("Digite um numero para escolher uma opção:")
    print("1 -> para adicionar uma nova tarefa")
    print("2 -> para listar todas as tarefas")
    print("3 -> para concluir uma tarefa")
    print("4 -> para remover uma tarefa")
    print("5 -> para remover todas as tarefas concluídas")
    print("6 -> para remover todas as tarefas não concluídas")
    print("7 -> para remover todas as tarefas")
    print("0 -> para sair")
    input_usuario = input("")
    print("\n--------------------------------------------------\n")
    if input_usuario == "1":
        tarefa = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(tarefa)
        print("Tarefa adicionada com sucesso!")
    
    elif input_usuario == "2":
        tarefas = listar_tarefas()
        
        if len(tarefas) == 0:
            print("Não há tarefas cadastradas!")
        else:
            for tarefa in tarefas:
                print(f"ID: {tarefa[0]} - Descrição: {tarefa[1]} - {'Concluída' if tarefa[2] else 'Incompleta'}")
        
    elif input_usuario == "3":
        id = input("Digite o id da tarefa que deseja concluir: ")
        concluir_tarefa(id)
        print("Tarefa concluída com sucesso!")
    
    elif input_usuario == "4":
        id = input("Digite o id da tarefa que deseja remover: ")
        remover_tarefa(id)
        print("Tarefa removida com sucesso!")
        
    
    elif input_usuario == "5":
        remover_tarefas_concluidas()
        print("Tarefas concluídas removidas com sucesso!")
    
    elif input_usuario == "6":
        remover_tarefas_nao_concluidas()
        print("Tarefas não concluídas removidas com sucesso!")
    
    elif input_usuario == "9":
        remover_todas_tarefas()
        print("Todas as tarefas removidas com sucesso!")
    
    else:
        print("Opção inválida!")
    
    print("\n--------------------------------------------------\n")
    
