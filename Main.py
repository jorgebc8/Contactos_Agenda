
from tkinter import *
import Contactos

def main():
    # ----------------- ROOT DECLARATION ------------------
    root = Tk()
    root.title('Agenda de Contactos')
    root.configure(bg = "#FFFFFF")
    root.geometry("+350+80")
    root.resizable(0,0)
    Contactos.App(root) # Call to the App
    root.mainloop()

if __name__ == "__main__":
    main()