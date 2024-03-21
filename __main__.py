from crud import crud

class Main:
    def __init__(self):
        self.crud=crud()

    def main():
        c=crud()
        c.view_tasks()
    if __name__ == "__main__":
        main()