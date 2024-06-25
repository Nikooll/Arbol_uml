import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from estructura_datos.listas import ListaEnlazadaSimple, ListaDoblementeEnlazada
from estructura_datos.arbol import ArbolBinarioBusqueda
from estructura_datos.grafo import Grafo

class EstructuraDatosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estructura de Datos")
        self.root.configure(bg='#282c34')
        self.lista_simple = ListaEnlazadaSimple()
        self.lista_doble = ListaDoblementeEnlazada()
        self.arbol = ArbolBinarioBusqueda()
        self.grafo = Grafo()
        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12), padding=10)
        style.configure('TLabel', background='#282c34', foreground='#ffffff', font=('Helvetica', 12))
        style.configure('TEntry', font=('Helvetica', 12), padding=10)
        style.map('TButton', background=[('active', '#61afef'), ('!disabled', '#61afef')])

        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label = ttk.Label(main_frame, text="Ingrese un valor:")
        self.label.grid(row=0, column=0, pady=5, sticky=tk.W)

        self.entry = ttk.Entry(main_frame)
        self.entry.grid(row=0, column=1, pady=5, sticky=tk.E)

        list_frame = ttk.LabelFrame(main_frame, text="Listas Enlazadas", padding="10")
        list_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        self.btn_add_simple = ttk.Button(list_frame, text="Agregar a Lista Simple", command=self.add_to_simple)
        self.btn_add_simple.grid(row=0, column=0, pady=5, padx=5)

        self.btn_add_doble = ttk.Button(list_frame, text="Agregar a Lista Doble", command=self.add_to_doble)
        self.btn_add_doble.grid(row=0, column=1, pady=5, padx=5)

        self.btn_remove_simple = ttk.Button(list_frame, text="Eliminar de Lista Simple", command=self.remove_from_simple)
        self.btn_remove_simple.grid(row=1, column=0, pady=5, padx=5)

        self.btn_remove_doble = ttk.Button(list_frame, text="Eliminar de Lista Doble", command=self.remove_from_doble)
        self.btn_remove_doble.grid(row=1, column=1, pady=5, padx=5)

        self.btn_show_simple = ttk.Button(list_frame, text="Mostrar Lista Simple", command=self.show_simple)
        self.btn_show_simple.grid(row=2, column=0, pady=5, padx=5)

        self.btn_show_doble = ttk.Button(list_frame, text="Mostrar Lista Doble", command=self.show_doble)
        self.btn_show_doble.grid(row=2, column=1, pady=5, padx=5)

        tree_frame = ttk.LabelFrame(main_frame, text="Árbol Binario de Búsqueda", padding="10")
        tree_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        self.btn_add_arbol = ttk.Button(tree_frame, text="Agregar a Árbol", command=self.add_to_tree)
        self.btn_add_arbol.grid(row=0, column=0, pady=5, padx=5)

        self.btn_remove_arbol = ttk.Button(tree_frame, text="Eliminar de Árbol", command=self.remove_from_tree)
        self.btn_remove_arbol.grid(row=0, column=1, pady=5, padx=5)

        self.btn_show_arbol = ttk.Button(tree_frame, text="Mostrar Árbol (Inorden)", command=self.show_tree_inorder)
        self.btn_show_arbol.grid(row=1, column=0, columnspan=2, pady=5, padx=5)

        graph_frame = ttk.LabelFrame(main_frame, text="Grafo", padding="10")
        graph_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        self.btn_add_grafo = ttk.Button(graph_frame, text="Agregar Nodo a Grafo", command=self.add_to_graph)
        self.btn_add_grafo.grid(row=0, column=0, pady=5, padx=5)

        self.btn_add_arista = ttk.Button(graph_frame, text="Agregar Arista a Grafo", command=self.add_edge_to_graph)
        self.btn_add_arista.grid(row=0, column=1, pady=5, padx=5)

        self.btn_remove_grafo = ttk.Button(graph_frame, text="Eliminar Nodo de Grafo", command=self.remove_from_graph)
        self.btn_remove_grafo.grid(row=1, column=0, pady=5, padx=5)

        self.btn_remove_arista = ttk.Button(graph_frame, text="Eliminar Arista de Grafo", command=self.remove_edge_from_graph)
        self.btn_remove_arista.grid(row=1, column=1, pady=5, padx=5)

        self.btn_show_grafo = ttk.Button(graph_frame, text="Mostrar Grafo", command=self.show_graph)
        self.btn_show_grafo.grid(row=2, column=0, columnspan=2, pady=5, padx=5)

        # Canvas para visualización gráfica
        self.canvas = tk.Canvas(self.root, width=400, height=600, bg='#ffffff')
        self.canvas.grid(row=0, column=1, rowspan=4, padx=20, pady=20)

    def draw_elements(self):
        self.canvas.delete("all")
        self.draw_list(self.lista_simple, 20, 20, "#61afef")
        self.draw_list(self.lista_doble, 20, 120, "#98c379")
        self.draw_tree(self.arbol.raiz, 200, 300, 100, "#e5c07b")
        self.draw_graph(self.grafo, 20, 420)

    def draw_list(self, lista, x, y, color):
        actual = lista.cabeza
        while actual is not None:
            self.canvas.create_oval(x, y, x+30, y+30, fill=color)
            self.canvas.create_text(x+15, y+15, text=str(actual.obtener_dato()))
            x += 40
            actual = actual.derecha if isinstance(lista, ListaEnlazadaSimple) else actual.siguiente

    def draw_tree(self, nodo, x, y, spacing, color):
        if nodo is not None:
            self.canvas.create_oval(x, y, x+30, y+30, fill=color)
            self.canvas.create_text(x+15, y+15, text=str(nodo.dato))
            if nodo.izquierda is not None:
                self.canvas.create_line(x+15, y+30, x-spacing+15, y+60)
                self.draw_tree(nodo.izquierda, x-spacing, y+60, spacing//2, color)
            if nodo.derecha is not None:
                self.canvas.create_line(x+15, y+30, x+spacing+15, y+60)
                self.draw_tree(nodo.derecha, x+spacing, y+60, spacing//2, color)

    def draw_graph(self, grafo, x, y):
        nodos_pos = {}
        spacing = 60
        for idx, nodo in enumerate(grafo.nodos):
            x_pos = x + (idx % 5) * spacing
            y_pos = y + (idx // 5) * spacing
            nodos_pos[nodo] = (x_pos, y_pos)
            self.canvas.create_oval(x_pos, y_pos, x_pos+30, y_pos+30, fill="#c678dd")
            self.canvas.create_text(x_pos+15, y_pos+15, text=nodo)
        for nodo in grafo.nodos:
            for adyacente in grafo.nodos[nodo].adyacentes:
                x1, y1 = nodos_pos[nodo]
                x2, y2 = nodos_pos[adyacente.dato]
                self.canvas.create_line(x1+15, y1+15, x2+15, y2+15)

    def add_to_simple(self):
        valor = self.entry.get()
        if valor:
            self.lista_simple.agregar_inicio(int(valor))
            self.entry.delete(0, tk.END)
            self.draw_elements()
            messagebox.showinfo("Éxito", f"Valor {valor} agregado a la Lista Simple")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un valor")

    def remove_from_simple(self):
        valor = self.lista_simple.eliminar_ultimo()
        if valor is not None:
            self.draw_elements()
            messagebox.showinfo("Éxito", f"Valor {valor} eliminado de la Lista Simple")
        else:
            messagebox.showwarning("Advertencia", "La Lista Simple está vacía")

    def show_simple(self):
        elementos = []
        actual = self.lista_simple.cabeza
        while actual is not None:
            elementos.append(actual.obtener_dato())
            actual = actual.derecha
        messagebox.showinfo("Lista Simple", " -> ".join(map(str, elementos)))

    def add_to_doble(self):
        valor = self.entry.get()
        if valor:
            self.lista_doble.agregar_inicio(int(valor))
            self.entry.delete(0, tk.END)
            self.draw_elements()
            messagebox.showinfo("Éxito", f"Valor {valor} agregado a la Lista Doble")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un valor")

    def remove_from_doble(self):
        valor = self.lista_doble.eliminar_ultimo()
        if valor is not None:
            self.draw_elements()
            messagebox.showinfo("Éxito", f"Valor {valor} eliminado de la Lista Doble")
        else:
            messagebox.showwarning("Advertencia", "La Lista Doble está vacía")

    def show_doble(self):
        elementos = []
        actual = self.lista_doble.cabeza
        while actual is not None:
            elementos.append(actual.obtener_dato())
            actual = actual.siguiente
        messagebox.showinfo("Lista Doble", " <-> ".join(map(str, elementos)))

    def add_to_tree(self):
        valor = self.entry.get()
        if valor:
            self.arbol.insertarNodo(int(valor))
            self.entry.delete(0, tk.END)
            self.draw_elements()
            messagebox.showinfo("Éxito", f"Valor {valor} agregado al Árbol")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un valor")

    def remove_from_tree(self):
        valor = self.entry.get()
        if valor:
            self.arbol.eliminarNodo(int(valor))
            self.entry.delete(0, tk.END)
            self.draw_elements()
            messagebox.showinfo("Éxito", f"Valor {valor} eliminado del Árbol")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un valor")

    def show_tree_inorder(self):
        elementos = []
        self.arbol.recorridoInorden(elementos)
        messagebox.showinfo("Árbol (Inorden)", " -> ".join(map(str, elementos)))

    def add_to_graph(self):
        valor = self.entry.get()
        if valor:
            self.grafo.agregarNodo(valor)
            self.entry.delete(0, tk.END)
            self.draw_elements()
            messagebox.showinfo("Éxito", f"Valor {valor} agregado al Grafo")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un valor")

    def add_edge_to_graph(self):
        nodo1 = self.entry.get()
        nodo2 = self.entry.get()
        if nodo1 and nodo2:
            self.grafo.agregarArista(nodo1, nodo2)
            self.entry.delete(0, tk.END)
            self.draw_elements()
            messagebox.showinfo("Éxito", f"Arista entre {nodo1} y {nodo2} agregada al Grafo")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese dos valores")

    def remove_from_graph(self):
        valor = self.entry.get()
        if valor:
            self.grafo.eliminarNodo(valor)
            self.entry.delete(0, tk.END)
            self.draw_elements()
            messagebox.showinfo("Éxito", f"Valor {valor} eliminado del Grafo")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un valor")

    def remove_edge_from_graph(self):
        nodo1 = self.entry.get()
        nodo2 = self.entry.get()
        if nodo1 and nodo2:
            self.grafo.eliminarArista(nodo1, nodo2)
            self.entry.delete(0, tk.END)
            self.draw_elements()
            messagebox.showinfo("Éxito", f"Arista entre {nodo1} y {nodo2} eliminada del Grafo")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese dos valores")

    def show_graph(self):
        elementos = []
        for nodo in self.grafo.nodos:
            adyacentes = [adyacente.dato for adyacente in self.grafo.nodos[nodo].adyacentes]
            elementos.append(f"{nodo}: {', '.join(adyacentes)}")
        messagebox.showinfo("Grafo", "\n".join(elementos))
