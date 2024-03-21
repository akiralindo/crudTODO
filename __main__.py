from crud import Tasks
from register import Register
from login import Login

class Main:
    def main():
        crud=Tasks()
        reg=Register()
        log=Login()
        log.userLogin()
        
    if __name__ == "__main__":
        main()