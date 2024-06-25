import tkinter as tk
from tkinter import messagebox
from estructura_datos.listas import ListaEnlazadaSimple, ListaDoblementeEnlazada

class EstructuraDatosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estructura de Datos")
        self.lista_simple = ListaEnlazadaSimple()
        self.lista_doble = ListaDoblementeEnlazada()
        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.root, text="Ingrese un valor:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.btn_add_simple = tk.Button(self.root, text="Agregar a Lista Simple", command=self.add_to_simple)
        self.btn_add_simple.pack()

        self.btn_add_doble = tk.Button(self.root, text="Agregar a Lista Doble", command=self.add_to_doble)
        self.btn_add_doble.pack()

        self.btn_show_simple = tk.Button(self.root, text="Mostrar Lista Simple", command=self.show_simple)
        self.btn_show_simple.pack()

        self.btn_show_doble = tk.Button(self.root, text="Mostrar Lista Doble", command=self.show_doble)
        self.btn_show_doble.pack()

    def add_to_simple(self):
        valor = self.entry.get()
        if valor:
            self.lista_simple.agregar_inicio(int(valor))
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Valor {valor} agregado a la Lista Simple")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un valor")

    def add_to_doble(self):
        valor = self.entry.get()
        if valor:
            self.lista_doble.agregar_inicio(int(valor))
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Valor {valor} agregado a la Lista Doble")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un valor")

    def show_simple(self):
        elementos = []
        actual = self.lista_simple.cabeza
        while actual is not None:
            elementos.append(str(actual.obtener_dato()))
            actual = actual.derecha
        messagebox.showinfo("Lista Simple", " -> ".join(elementos) + " -> None")

    def show_doble(self):
        elementos = []
        actual = self.lista_doble.cabeza
        while actual is not None:
            elementos.append(str(actual.obtener_dato()))
            actual = actual.siguiente
        messagebox.showinfo("Lista Doble", " <-> ".join(elementos) + " <-> None")
