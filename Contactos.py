from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
import orden
import csv



def no_found(var):
    var_s = str(var)
    MessageBox.showinfo("No se ha encontrado", var_s + ' ' + "no se ha encontrado")


def write_name():
    MessageBox.showinfo("No se encuentra", "Tiene que escribir un contacto")


def write_contact():
    MessageBox.showinfo("Escribe un contacto", "Debes escribir la información de contacto para poder: \"Añadir un contacto\" opciones")


def delete_mesageBox(name):
    var_name = str(name)
    if var_name == '':
        write_name()
    else:
        search = MessageBox.askquestion("Alerta: Eliminar", "Desea eliminar este contacto?\n" + var_name)
        if search == "yes":
            return True
        else:
            return False


def modify_mesageBox(contact):
    var_name = str(contact[0])
    var_phone = str(contact[1])
    var_email = str(contact[2])
    search = MessageBox.askquestion("Alerta: Modificar",
                                    "Desea guardar los cambios realizados sobre este contacto?\n" + " Nombre:" + var_name +"\n Apellido:" + var_email+ "\n Número:" + var_phone)
    if search == "yes":
        return True
    else:
        return False



class App():
    def __init__(self, root):
        self.window = root


        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0, bg="#FFFFFF")
        filemenu.add_command(label="Mostrar todos los contactos", command=lambda: show_contacts(),
                             font=("Times New Roman", "9", "normal"))
        filemenu.add_command(label="Manual de Usuario", font=("Times New Roman", "9", "normal"))
        filemenu.add_separator()
        filemenu.add_command(label="Cerrar", command=self.window.quit, font=("Times New Roman", "9", "normal"))

        menubar.add_cascade(label="Menú", menu=filemenu)


        inbox_frame = LabelFrame(self.window, bg="#FFFFFF")
        inbox_frame.grid(row=2, column=0)

        button_frame = LabelFrame(self.window, bg="#FFFFFF")
        button_frame.grid(row=2, column=4)

        three_frame = LabelFrame(self.window, bg="#FFFFFF")
        three_frame.grid(row=4, column=0)

        three_button_frame = LabelFrame(self.window, bg="#FFFFFF")
        three_button_frame.grid(row=5, column=0)


        Label(inbox_frame, text='Nombre', bg="#FFFFFF", font=("Times New Roman", "11", "normal")).grid(row=0, column=0)
        inbox_name = Entry(inbox_frame, font=("Times New Roman", "11", "normal"), width=28)
        inbox_name.grid(row=0, column=1)
        inbox_name.focus()

        Label(inbox_frame, text='Apellido', bg="#FFFFFF", font=("Times New Roman", "11", "normal")).grid(row=1, column=0)
        inbox_Email = Entry(inbox_frame, font=("Times New Roman", "11", "normal"), width=30)
        inbox_Email.grid(row=1, column=1)

        Label(inbox_frame, text='Número de Teléfono', bg="#FFFFFF", font=("Times New Roman", "11", "normal")).grid(row=2, column=0)
        inbox_phone = Entry(inbox_frame, font=("Times New Roman", "11", "normal"), width=20)
        inbox_phone.grid(row=2, column=1)



        # --------------- BUTTON WIDGETS ZONE -----------------
        Add_contact_button = Button(button_frame, command=lambda: add(), text='Añadir Contacto', width=20)
        Add_contact_button.configure(bg="#FFFFFF", cursor='hand2', font=("Times New Roman", "10", "normal"))
        Add_contact_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)



        delete_button = Button(button_frame, command=lambda: delete(), text='Eliminar contacto', width=20)
        delete_button.configure(bg="#FFFFFF", cursor='hand2', font=("Times New Roman", "10", "normal"))
        delete_button.grid(row=1, column=1, padx=2, pady=3, sticky=W + E)

        modify_button = Button(button_frame, command=lambda: modify(), text='Modificar contacto')
        modify_button.configure(bg="#FFFFFF", cursor='hand2', font=("Times New Roman", "10", "normal"))
        modify_button.grid(row=2, column=1, padx=2, pady=3, sticky=W + E)



        save_changes_button = Button(button_frame, command=lambda: clean(), text='Limpiar todo', width=20)
        save_changes_button.configure(bg="#FFFFFF", cursor='hand2', font=("Times New Roman", "10", "normal"))
        save_changes_button.grid(row=3, column=1, padx=2, pady=3, sticky=W + E)


        Label(button_frame, text='Modificar Selección', bg="#FFFFFF", font=("Times New Roman", "10", "normal")).grid(
            row=0, column=0, columnspan=1)

        combo = ttk.Combobox(button_frame, state='readonly', width=17, justify='center',
                             font=("Times New Roman", "10", "normal"))
        combo["values"] = ['Nombre', 'Apellido', 'Número']
        combo.grid(row=1, column=0, padx=15)
        combo.current(0)



        self.tree = ttk.Treeview(three_frame, height=20, columns=("one", "two"))
        self.tree.grid(padx=5, pady=5, row=0, column=0, columnspan=1)
        self.tree.heading("#0", text='Nombre', anchor=CENTER)
        self.tree.heading("one", text='Apellido', anchor=CENTER)
        self.tree.heading("two", text='Número de Teléfono', anchor=CENTER)

        # Scroll
        scrollVert = Scrollbar(three_frame, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollVert.set)
        scrollVert.grid(row=0, column=1, sticky="nsew")

        scroll_x = Scrollbar(three_frame, command=self.tree.xview, orient=HORIZONTAL)
        self.tree.configure(xscrollcommand=scroll_x.set)
        scroll_x.grid(row=2, column=0, columnspan=1, sticky="nsew")




        def _clean_inbox():
            # Delete from first position (0) to the last position ('end')
            inbox_name.delete(0, 'end')
            inbox_phone.delete(0, 'end')
            inbox_Email.delete(0, 'end')

        def _clean_treeview():
            tree_list = self.tree.get_children()
            for item in tree_list:
                self.tree.delete(item)

        def _view_csv():
            contacts = orden.alphabetic_order()
            for i, row in enumerate(contacts):
                name = str(row[0])
                phone = str(row[1])
                email = str(row[2])
                self.tree.insert("", 0, text=name, values=(phone, email))

        def _save(name, phone, email):
            s_name = name
            s_phone = phone
            s_email = email
            with open('contacts_list.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_name, s_phone, s_email))

        def _search(var_inbox, possition):
            my_list = []
            s_var_inbox = str(var_inbox)
            var_possition = int(possition)
            with open('contacts_list.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if s_var_inbox == row[var_possition]:
                        my_list = [row[0], row[1], row[2]]
                        break
                    else:
                        continue
            return my_list

        def _check(answer, var_search):
            list_answer = answer
            var_search = var_search
            if list_answer == []:
                no_found(var_search)
            else:
                name = str(list_answer[0])
                phone = str(list_answer[1])
                email = str(list_answer[2])
                self.tree.insert("", 0, text="------------------------------",
                                 values=("------------------------------", "------------------------------"))
                self.tree.insert("", 0, text=name, values=(phone, email))
                self.tree.insert("", 0, text="Resultado de búsqueda por nombre",
                                 values=("Resultado de búsqueda por apellido", "Resultado de búsqueda por número de teléfono"))
                self.tree.insert("", 0, text="------------------------------",
                                 values=("------------------------------", "------------------------------"))

        def _check_1(answer, var_search):
            val_modify = answer
            var = var_search
            if val_modify == []:
                no_found(var)
            else:
                TopLevelModify(self.window, val_modify)


        def add():
            name = inbox_name.get()
            phone = inbox_phone.get()
            email = inbox_Email.get()
            contact_check = [name, phone, email]
            if contact_check == ['', '', '']:
                write_contact()
            else:
                if name == '':
                    name = '<Default>'
                if phone == '':
                    phone = '<Default>'
                if email == '':
                    email = '<Default>'
                _save(name, phone, email)
                self.tree.insert("", 0, text="------------------------------",
                                 values=("------------------------------", "------------------------------"))
                self.tree.insert("", 0, text=str(name), values=(str(email), str(phone)))
                self.tree.insert("", 0, text="Nuevo nombre añadido", values=("Nuevo apellido añadido", "Nuevo número de teléfono añadido"))
                self.tree.insert("", 0, text="------------------------------",
                                 values=("------------------------------", "------------------------------"))
            contact_check = []
            _clean_inbox()

        def search():
            answer = []
            var_search = str(combo.get())
            if var_search == 'Nombre':
                var_inbox = inbox_name.get()
                possition = 0
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            elif var_search == 'Apellido':
                var_inbox = inbox_phone.get()
                possition = 1
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            else:
                var_inbox = inbox_Email.get()
                possition = 2
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            _clean_inbox()

        def modify():
            answer = []
            var_search = str(combo.get())
            if var_search == 'Name':
                var_inbox = inbox_name.get()
                possition = 0
                answer = _search(var_inbox, possition)
                _check_1(answer, var_search)
            elif var_search == 'Phone':
                var_inbox = inbox_phone.get()
                possition = 1
                answer = _search(var_inbox, possition)
                _check_1(answer, var_search)
            else:
                var_inbox = inbox_Email.get()
                possition = 2
                answer = _search(var_inbox, possition)
                _check_1(answer, var_search)
            _clean_inbox()

        def show_contacts():
            self.tree.insert("", 0, text="------------------------------",
                             values=("------------------------------", "------------------------------"))
            _view_csv()
            self.tree.insert("", 0, text="------------------------------",
                             values=("------------------------------", "------------------------------"))

        def delete():
            name = str(inbox_name.get())
            a = delete_mesageBox(name)
            if a == True:
                with open('contacts_list.csv', 'r') as f:
                    reader = list(csv.reader(f))
                with open('contacts_list.csv', 'w') as f:
                    writer = csv.writer(f, lineterminator='\r', delimiter=',')
                    for i, row in enumerate(reader):
                        if name != row[0]:
                            writer.writerow(row)
            clean()
            show_contacts()

        def clean():
            _clean_inbox()
            _clean_treeview()




class TopLevelModify():
    def __init__(self, root, val_modify):
        self.root_window = root
        self.val_modify = val_modify
        self.name = str(self.val_modify[0])
        self.phone = str(self.val_modify[1])
        self.email = str(self.val_modify[2])

        window_modify = Toplevel(self.root_window)
        window_modify.title("Modificar Contacto")
        window_modify.configure(bg="#FFFFFF")
        window_modify.geometry("+400+100")
        window_modify.resizable(0, 0)


        text_frame = LabelFrame(window_modify, bg="#FFFFFF")
        text_frame.grid(row=0, column=0)

        button_frame = LabelFrame(window_modify, bg="#FFFFFF")
        button_frame.grid(row=2, column=0)


        Label(text_frame, text="Desea modificar este contacto?", bg="#FFFFFF",
              font=("Times New Roman", "11", "normal")).grid(row=0, column=0, columnspan=3)
        Label(text_frame, text=self.name, bg="#FFFFFF", font=("Times New Roman", "11", "normal")).grid(row=1, column=0)
        Label(text_frame, text=self.phone, bg="#FFFFFF", font=("Times New Roman", "11", "normal")).grid(row=1, column=1)
        Label(text_frame, text=self.email, bg="#FFFFFF", font=("Times New Roman", "11", "normal")).grid(row=1, column=2)


        Label(text_frame, text='Escriba un nuevo nombre', bg="#FFFFFF", font=("Times New Roman", "11", "normal")).grid(row=1,
                                                                                                              column=0)
        n_inbox_name = Entry(text_frame, font=("Times New Roman", "11", "normal"), width=28)
        n_inbox_name.grid(row=1, column=1)
        n_inbox_name.focus()

        Label(text_frame, text='Nuevo número de teléfono', bg="#FFFFFF", font=("Times New Roman", "11", "normal")).grid(row=2,
                                                                                                               column=0)
        n_inbox_phone = Entry(text_frame, font=("Times New Roman", "11", "normal"), width=20)
        n_inbox_phone.grid(row=2, column=1)

        Label(text_frame, text='Nuevo apellido', bg="#FFFFFF", font=("Times New Roman", "11", "normal")).grid(row=3,
                                                                                                               column=0)
        n_inbox_Email = Entry(text_frame, font=("Times New Roman", "11", "normal"), width=30)
        n_inbox_Email.grid(row=3, column=1)


        yes_button = Button(button_frame, command=lambda: yes(), text='Yes', width=20)
        yes_button.configure(bg="#FFFFFF", cursor='hand2', font=("Times New Roman", "10", "normal"))
        yes_button.grid(row=1, column=0, padx=2, pady=3, sticky=W + E)

        no_button = Button(button_frame, command=window_modify.destroy, text='No', width=20, bg="yellow",
                           cursor='hand2')
        no_button.configure(bg="#FFFFFF", cursor='hand2', font=("Times New Roman", "10", "normal"))
        no_button.grid(row=1, column=1, padx=2, pady=3, sticky=W + E)

        cancel_button = Button(button_frame, command=window_modify.destroy, text='Cancel', width=20, bg="green",
                               cursor='hand2')
        cancel_button.configure(bg="#FFFFFF", cursor='hand2', font=("Times New Roman", "10", "normal"))
        cancel_button.grid(row=1, column=2, padx=2, pady=3, sticky=W + E)


        def yes():
            contact = self.val_modify
            new_name = n_inbox_name.get()
            new_phone = n_inbox_phone.get()
            new_email = n_inbox_Email.get()
            a = modify_mesageBox(contact)
            if a == True:
                _del_old(contact[0])
                _add_new(new_name, new_phone, new_email)
            window_modify.destroy()

        def _add_new(name, phone, email):
            s_name = name
            s_phone = phone
            s_email = email
            with open('contacts_list.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_name, s_phone, s_email))

        def _del_old(old_name):
            name = old_name
            with open('contacts_list.csv', 'r') as f:
                reader = list(csv.reader(f))
            with open('contacts_list.csv', 'w') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                for i, row in enumerate(reader):
                    if name != row[0]:
                        writer.writerow(row)


