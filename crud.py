import tkinter as tk
import mysql.connector

class crud:
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
        cursor.close()
        self.connection.close()
    
    
    """"função que retorna todos os dados na tabela tasks"""
    def view_all_tasks(self):
        cursor=self.connection.cursor()
        comando=f'SELECT * FROM tasks'
        cursor.execute(comando)
        res=cursor.fetchall()
        print(res)
        cursor.close()
        self.connection.close()
    
    
    """"função que retorna os dados na tabela tasks que não estão completados"""
    def view_tasks(self):
        cursor=self.connection.cursor()
        comando=f'SELECT * FROM tasks WHERE statusTask=0'
        cursor.execute(comando)
        res=cursor.fetchall()
        print(res)
        cursor.close()
        self.connection.close()
    
    
    """"função que retorna os dados na tabela completed_tasks"""
    def view_completed_tasks(self):
        cursor=self.connection.cursor()
        comando=f'SELECT * FROM tasks WHERE statusTask=1'
        cursor.execute(comando)
        res=cursor.fetchall()
        print(res)
        cursor.close()
        self.connection.close()
    
    
    """"função que seta o valor de statusTask para 1 (task completada), usa idTask como parametro"""
    def update_task(self, idTask):
        cursor=self.connection.cursor()
        comando=f'UPDATE tasks SET statusTask=1 WHERE idTask="{idTask}"'
        cursor.execute(comando)
        self.connection.commit()
        cursor.close()
        self.connection.close()
    
    
    """"função que deleta task com base em seu idTask, usa o idTask como parametro"""
    def delete_task(self, idTask):
        cursor=self.connection.cursor()
        comando=f'DELETE FROM tasks WHERE idTask="{idTask}"'
        cursor.execute(comando)
        self.connection.commit()
        cursor.close()
        self.connection.close()