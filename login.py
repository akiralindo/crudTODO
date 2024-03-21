import mysql.connector

class Login:
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
        
    def userLogin(self):
        cursor=self.connection.cursor()
        user=input("Usuário: ")
        comando=f'SELECT * FROM user WHERE username="{user}"'
        cursor.execute(comando)
        res=cursor.fetchall()
        if res:
            pas=input("Senha: ")
            if(res[0][2]==pas):
                print("Login efetuado com sucesso")
            else:
                print("Senha incorreta")
                self.userLogin()
        else:
            print("Usuário não encontrado!")
            self.userLogin()