import mysql.connector

class viewTable:
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
    
    """"função que retorna todos os dados na tabela tasks"""   
    def view_all_tasks(self):
        cursor=self.connection.cursor()
        comando=f'SELECT * FROM tasks'
        cursor.execute(comando)
        res=cursor.fetchall()
        for row in res:
            print("Nome:",row[1])
            print("Descrição:",row[2])
        cursor.close()
        self.connection.close()
        
    """"função que retorna os dados na tabela tasks que não estão completados"""
    def view_tasks(self):
        cursor=self.connection.cursor()
        comando=f'SELECT * FROM tasks WHERE statusTask=0'
        cursor.execute(comando)
        res=cursor.fetchall()
        for row in res:
            print("Nome:",row[1])
            print("Descrição:",row[2])
        cursor.close()
        self.connection.close()
        
    """"função que retorna os dados na tabela completed_tasks"""
    def view_completed_tasks(self):
        cursor=self.connection.cursor()
        comando=f'SELECT * FROM tasks WHERE statusTask=1'
        cursor.execute(comando)
        res=cursor.fetchall()
        for row in res:
            print("Nome:",row[1])
            print("Descrição:",row[2])
        cursor.close()
        self.connection.close()