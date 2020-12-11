from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import orden
import csv





def no_found(var):
    var_s = str(var)
    MessageBox.showinfo("No se encontro", var_s + ' ' + "No se encontro")


def write_name():
    MessageBox.showinfo("No se encontro", "Necesitas escribir un contacto")


def write_contact():
    MessageBox.showinfo("Escribe un contacto", "Debes escribir la información del contacto para usarlo\"Añade contacto\"")


def delete_mesageBox(name):
    var_name = str(name)
    if var_name == '':
        write_name()
    else:
        search = MessageBox.askquestion("Borrar", "¿Quieres borrar el contacto?\n" + var_name)
        if search == "si":
            return True
        else:
            return False


def modify_mesageBox(contacto):
    var_nombre = str(contacto[0])
    var_numero = str(contacto[1])
    var_email = str(contacto[2])
    search = MessageBox.askquestion("Modificar",
                                    "¿Quieres guardar los cambios del contacto?\n" + " Nombre:" + var_nombre + "\n numero:" + var_numero + "\n Email:" + var_email)
    if search == "si":
        return True
    else:
        return False



class App():
    def __init__(self, root):
        self.window = root


        menub = Menu(self.window)
        self.window.config(menu=menub)

        fmenu = Menu(menub, tearoff=0, bg="#FFFFFF")
        fmenu.add_command(label="Mostrar todos los contactos", command=lambda: show_contacts(),
                             font=("Arial", "10", "normal"))
        fmenu.add_command(label="Usuario", font=("Arial", "10", "normal"))
        fmenu.add_separator()
        fmenu.add_command(label="Close", command=self.window.quit, font=("Arial", "10", "normal"))

        menub.add_cascade(label="Menu", menu=fmenu)


        inbox_frame = LabelFrame(self.window, bg="#FFFFFF")
        inbox_frame.grid(row=0, column=0)

        button_frame = LabelFrame(self.window, bg="#FFFFFF")
        button_frame.grid(row=2, column=0)

        three_frame = LabelFrame(self.window, bg="#FFFFFF")
        three_frame.grid(row=4, column=0)

        three_button_frame = LabelFrame(self.window, bg="#FFFFFF")
        three_button_frame.grid(row=5, column=0)

        # --------------- INBOX WIDGETS ZONE ------------------
        Label(inbox_frame, text='Nombre', bg="#FFFFFF", font=("Arial", "10", "normal")).grid(row=0, column=0)
        inbox_name = Entry(inbox_frame, font=("Arial", "10", "normal"), width=25)
        inbox_name.grid(row=1, column=0)
        inbox_name.focus()

        Label(inbox_frame, text='Numero', bg="#FFFFFF", font=("Arial", "10", "normal")).grid(row=0, column=1)
        inbox_phone = Entry(inbox_frame, font=("Arial", "10", "normal"), width=20)
        inbox_phone.grid(row=1, column=1)

        Label(inbox_frame, text='Email', bg="#FFFFFF", font=("Arial", "10", "normal")).grid(row=0, column=2)
        inbox_Email = Entry(inbox_frame, font=("Arial", "10", "normal"), width=28)
        inbox_Email.grid(row=1, column=2)

        # --------------- BUTTON WIDGETS ZONE -----------------
        Add_contact_button = Button(button_frame, command=lambda: add(), text='Añadir contacto', width=20)
        Add_contact_button.configure(bg="#FFFFFF", cursor='hand2', font=("Arial", "10", "normal"))
        Add_contact_button.grid(row=0, column=0, padx=2, pady=3, sticky=W + E)

        search_button = Button(button_frame, command=lambda: search(), text='Buscar contacto', width=20)
        search_button.configure(bg="#FFFFFF", cursor='hand2', font=("Arial", "10", "normal"))
        search_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        delete_button = Button(button_frame, command=lambda: delete(), text='Borrar contacto', width=20)
        delete_button.configure(bg="#F26262", cursor='hand2', font=("Arial", "10", "normal"))
        delete_button.grid(row=1, column=0, padx=2, pady=3, sticky=W + E)

        modify_button = Button(button_frame, command=lambda: modify(), text='Modificar contacto')
        modify_button.configure(bg="#FFFFFF", cursor='hand2', font=("Arial", "10", "normal"))
        modify_button.grid(row=1, column=1, padx=2, pady=3, sticky=W + E)

        show_contacts_button = Button(button_frame, command=lambda: show_contacts(), text='Mostrar todos los contactos', width=20)
        show_contacts_button.configure(bg="#FFFFFF", cursor='hand2', font=("Arial", "10", "normal"))
        show_contacts_button.grid(row=0, column=2, padx=2, pady=3, sticky=W + E)

        save_changes_button = Button(button_frame, command=lambda: clean(), text='Limpiar ventana', width=20)
        save_changes_button.configure(bg="#FFFFFF", cursor='hand2', font=("Arial", "10", "normal"))
        save_changes_button.grid(row=1, column=2, padx=2, pady=3, sticky=W + E)

        # -------------- COMBOBOX WIDGETS ZONE ----------------
        Label(button_frame, text='Buscar/Modificar', bg="#FFFFFF", font=("Arial", "10", "normal")).grid(
            row=0, column=3, columnspan=3)

        combo = ttk.Combobox(button_frame, state='readonly', width=17, justify='center',
                             font=("Arial", "10", "normal"))
        combo["values"] = ['Nombre', 'Numero', 'Email']
        combo.grid(row=1, column=3, padx=15)
        combo.current(0)

        # --------------- TREE DIRECTORY ZONE -----------------
        # Table for database
        self.tree = ttk.Treeview(three_frame, height=20, columns=("uno", "dos"))
        self.tree.grid(padx=5, pady=5, row=0, column=0, columnspan=1)
        self.tree.heading("#0", text='Nombre', anchor=CENTER)
        self.tree.heading("uno", text='Numero', anchor=CENTER)
        self.tree.heading("dos", text='Email', anchor=CENTER)

        # Scroll
        scrollVert = Scrollbar(three_frame, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollVert.set)
        scrollVert.grid(row=0, column=1, sticky="nsew")

        scroll_x = Scrollbar(three_frame, command=self.tree.xview, orient=HORIZONTAL)
        self.tree.configure(xscrollcommand=scroll_x.set)
        scroll_x.grid(row=2, column=0, columnspan=1, sticky="nsew")


        def _clean_inbox():

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
                self.tree.insert("", 0, text="----------------------",
                                 values=("----------------------", "------------------------"))
                self.tree.insert("", 0, text=name, values=(phone, email))
                self.tree.insert("", 0, text="Buscar resultado del nombre",
                                 values=("Buscar resultado de numero", "Buscar resultado de email"))
                self.tree.insert("", 0, text="------------------------",
                                 values=("---------------------------", "-------------------------"))

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
                self.tree.insert("", 0, text="------------------------",
                                 values=("--------------------------", "--------------------------"))
                self.tree.insert("", 0, text=str(name), values=(str(phone), str(email)))
                self.tree.insert("", 0, text="Nuevo nombre añadido", values=("Nuevo numero añadido", "Nuevo email añadido"))
                self.tree.insert("", 0, text="-------------------------",
                                 values=("--------------------------", "---------------------------"))
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
            elif var_search == 'Numero':
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
            if var_search == 'Nombre':
                var_inbox = inbox_name.get()
                possition = 0
                answer = _search(var_inbox, possition)
                _check_1(answer, var_search)
            elif var_search == 'Telefono':
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
            self.tree.insert("", 0, text="--------------------------",
                             values=("-------------------------", "-------------------------"))
            _view_csv()
            self.tree.insert("", 0, text="------------------------",
                             values=("------------------------", "---------------------------"))

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
        window_modify.title("Modificar contacto")
        window_modify.configure(bg="#FFFFFF")
        window_modify.geometry("+300+200")
        window_modify.resizable(0, 0)


        text_frame = LabelFrame(window_modify, bg="#FFFFFF")
        text_frame.grid(row=0, column=0)

        button_frame = LabelFrame(window_modify, bg="#FFFFFF")
        button_frame.grid(row=2, column=0)


        Label(text_frame, text="¿Quieres modificar el contacto?", bg="#FFFFFF",
              font=("Arial", "10", "normal")).grid(row=0, column=0, columnspan=3)
        Label(text_frame, text=self.name, bg="#FFFFFF", font=("Arial", "10", "bold")).grid(row=1, column=0)
        Label(text_frame, text=self.phone, bg="#FFFFFF", font=("Arial", "10", "bold")).grid(row=1, column=1)
        Label(text_frame, text=self.email, bg="#FFFFFF", font=("Arial", "10", "bold")).grid(row=1, column=2)


        Label(text_frame, text='Escribe un nombre nuevo', bg="#FFFFFF", font=("Arial", "10", "normal")).grid(row=2,
                                                                                                              column=0)
        n_inbox_name = Entry(text_frame, font=("Arial", "10", "normal"), width=28)
        n_inbox_name.grid(row=3, column=0)
        n_inbox_name.focus()

        Label(text_frame, text='Escribe un nuevo numero', bg="#FFFFFF", font=("Arial", "10", "normal")).grid(row=2,
                                                                                                               column=1)
        n_inbox_phone = Entry(text_frame, font=("Arial", "10", "normal"), width=20)
        n_inbox_phone.grid(row=3, column=1)

        Label(text_frame, text='Escribe un email nuevo', bg="#FFFFFF", font=("Arial", "10", "normal")).grid(row=2,
                                                                                                               column=2)
        n_inbox_Email = Entry(text_frame, font=("Arial", "10", "normal"), width=30)
        n_inbox_Email.grid(row=3, column=2)


        yes_button = Button(button_frame, command=lambda: yes(), text='Yes', width=20)
        yes_button.configure(bg="#FFFFFF", cursor='hand2', font=("Arial", "10", "normal"))
        yes_button.grid(row=1, column=0, padx=2, pady=3, sticky=W + E)

        no_button = Button(button_frame, command=window_modify.destroy, text='No', width=20, bg="blue",
                           cursor='hand2')
        no_button.configure(bg="#FFFFFF", cursor='hand2', font=("Arial", "10", "normal"))
        no_button.grid(row=1, column=1, padx=2, pady=3, sticky=W + E)

        cancel_button = Button(button_frame, command=window_modify.destroy, text='Cancelar', width=20, bg="green",
                               cursor='hand2')
        cancel_button.configure(bg="#FFFFFF", cursor='hand2', font=("Arial", "10", "normal"))
        cancel_button.grid(row=1, column=2, padx=2, pady=3, sticky=W + E)

        # ----------------- BUTTON FUNCTIONS ------------------
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