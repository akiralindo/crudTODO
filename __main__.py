from crud import crud

class Main:
    def __init__(self):
        self.crud=crud()

    def main():
        c=crud()
        c.update_task(1)

    if __name__ == "__main__":
        main()