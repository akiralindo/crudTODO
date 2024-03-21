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
        self.res=cursor.fetchall()
        print(self.res)
        if self.res:
            pas=input("Senha: ")
            if(self.res[0][2]==pas):
                print("Login efetuado com sucesso")
                self.userid=self.res[0][0]
                return self.userid
            else:
                print("Senha incorreta")
                self.userLogin()
        else:
            print("Usuário não encontrado!")
            self.userLogin()
