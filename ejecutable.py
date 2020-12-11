
from tkinter import *
import App

def main():

    root = Tk()
    root.title('Contactos')
    root.configure(bg = "#FFFFFF")
    root.geometry("+300+50")
    root.resizable(0,0)
    App.App(root)
    root.mainloop()

if __name__ == "__main__":
    main()