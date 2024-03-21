import mysql.connector

class Register:
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
        
    def registerUser(self):
        cursor=self.connection.cursor()
        user=input("Digite o usuário: ")
        comando=f'SELECT * FROM user'
        cursor.execute(comando)
        res=cursor.fetchall()
        for row in res:
            if(row[1]==user):
                print("Username já cadastrado")
                self.registerUser()
        pas=input("Digite a senha: ")
        comando=f'INSERT INTO user (username,password) VALUES("{user}","{pas}")'
        cursor.execute(comando)
        self.connection.commit()
        cursor.close()
        self.connection.close()