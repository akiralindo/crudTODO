import mysql.connector
from viewTable import viewTable

class Tasks:
    def __init__(self):
        #estabelecendo conexão com o banco de dados
        self.connection=self.connect()
    
    
    """função que conecta ao banco de dados"""
    def connect(self):
        return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="todolist"
        )
    
    
    """função que insere os dados no banco de dados com os parametros = nome da task, 
    descrição da task e status da task com o valor 0 como padrão (não completada)"""
    def insert_tasks(self,nome,descricao):
        cursor=self.connection.cursor()
        comando=f'INSERT INTO tasks (nomeTask, descTask, statusTask) VALUES ("{nome}", "{descricao}", 0)'
        cursor.execute(comando)
        self.connection.commit()
        print("Task adicionada")
        cursor.close()
        self.connection.close()
    
    
    def select_view_tasks(self):
        int(input("1. All tasks\n2. Tasks\n3. Completed tasks"))
        v=viewTable()
    
    
    """"função que seta o valor de statusTask para 1 (task completada), usa idTask como parametro"""
    def update_task(self):
        cursor=self.connection.cursor()
        res=self.view_all_tasks()
        for row in res:
            print("Id:",row[0])
            print("Nome:",row[1])
        idTask=int(input("Qual task deseja atualizar?"))
        comando=f'UPDATE tasks SET statusTask=1 WHERE idTask="{idTask}"'
        cursor.execute(comando)
        self.connection.commit()
        print("Task atualizada")
        cursor.close()
        self.connection.close()
    
    
    """"função que deleta task com base em seu idTask, usa o idTask como parametro"""
    def delete_task(self, idTask):
        cursor=self.connection.cursor()
        res=self.view_all_tasks()
        for row in res:
            print("Id:",row[0])
            print("Nome:",row[1])
        idTask=int(input("Qual task deseja deletar?"))
        comando=f'DELETE FROM tasks WHERE idTask="{idTask}"'
        cursor.execute(comando)
        self.connection.commit()
        print("Task deletada")
        cursor.close()
        self.connection.close()