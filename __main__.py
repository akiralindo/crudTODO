from crud import Tasks
from register import Register

class Main:
    def main():
        crud=Tasks()
        reg=Register()
        reg.registerUser()
        crud.view_all_tasks()
    if __name__ == "__main__":
        main()