from crud import Crud
from register import Register
from login import Login

class Main:
    def main():
        reg=Register()
        log=Login()
        crud=Crud()
        user=log.userLogin()
        crud.insert_tasks(user)
    if __name__ == "__main__":
        main()