import tkinter as tk
from tkinter import ttk

from Model.dbconnect import DatabaseMd


class DatabaseVw(DatabaseMd):

    def __init__(self):
        self.conectarBanco()

    def conectarBanco(self):
        conectar_banco_window = tk.Toplevel()
        conectar_banco_window.title("Conectar ao banco de dados")
        conectar_banco_window.geometry("300x300")
        conectar_banco_window.lift()
        conectar_banco_window.attributes("-topmost", True)

        dbhost_label = ttk.Label(master=conectar_banco_window, text='Host')
        dbhost_label.grid(row=1, column=0, padx=4, pady=4)

        dbhost = tk.StringVar()
        dbhost_entry = ttk.Entry(master=conectar_banco_window, textvariable=dbhost)
        dbhost_entry.grid(row=1, column=1, padx=4, pady=4)

        dbusername_label = ttk.Label(master=conectar_banco_window, text='Username')
        dbusername_label.grid(row=2, column=0, padx=4, pady=4)

        dbusername = tk.StringVar()
        dbusername_entry = ttk.Entry(master=conectar_banco_window, textvariable=dbusername)
        dbusername_entry.grid(row=2, column=1, padx=4, pady=4)

        dbpassword_label = ttk.Label(master=conectar_banco_window, text='Senha')
        dbpassword_label.grid(row=3, column=0, padx=4, pady=4)

        dbpassword = tk.StringVar()
        dbpassword_entry = ttk.Entry(master=conectar_banco_window, textvariable=dbpassword, show="*")
        dbpassword_entry.grid(row=3, column=1, padx=4, pady=4)

        dbname_label = ttk.Label(master=conectar_banco_window, text='Nome do Banco de Dados')
        dbname_label.grid(row=4, column=0, padx=4, pady=4)

        dbname = tk.StringVar()
        dbname_entry = ttk.Entry(master=conectar_banco_window, textvariable=dbname)
        dbname_entry.grid(row=4, column=1, padx=4, pady=4)

        def connect(host, username, password, name):
            DatabaseMd.banco_host = host
            DatabaseMd.banco_username = username
            DatabaseMd.banco_password = password
            DatabaseMd.banco_nome = name
            DatabaseMd.dbConnect()
            conectar_banco_window.destroy()

        connect_button = tk.Button(master=conectar_banco_window, text="Conectar", width=33, height=1,
                                   command=lambda: connect(dbhost.get(), dbusername.get(),
                                                           dbpassword.get(), dbname.get()))
        connect_button.grid(row=5, column=0, padx=4, pady=4, columnspan=2)
