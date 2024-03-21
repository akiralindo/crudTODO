import tkinter as tk

class menu:
    def __init__(self,master):
        self.master=master
        self.root=tk.Tk()
        self.frame=tk.Frame()
    
    def draw_menu(self):
        self.root.geometry("300x200")
        self.root.title("Menu")
        