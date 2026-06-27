import customtkinter as ctk
from tkinter import messagebox

from excel_manager import ExcelManager


class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("⚽ Cracks Control")
        self.geometry("900x700")
        self.resizable(False, False)

        self.excel = ExcelManager()

        self.asistentes = []

        self.crear_interfaz()


    # ==========================================

    def crear_interfaz(self):

        titulo = ctk.CTkLabel(
            self,
            text="⚽ CRACKS CONTROL",
            font=("Arial",32,"bold")
        )

        titulo.pack(pady=20)


        subtitulo = ctk.CTkLabel(
            self,
            text="Escuela Malaquías Concha",
            font=("Arial",18)
        )

        subtitulo.pack(pady=5)


        self.entry_nombre = ctk.CTkEntry(
            self,
            width=450,
            height=40,
            placeholder_text="Escriba el nombre..."
        )

        self.entry_nombre.pack(pady=20)

        self.entry_nombre.bind(
            "<Return>",
            lambda e:self.registrar()
        )


        boton = ctk.CTkButton(
            self,
            text="Registrar",
            width=220,
            height=45,
            command=self.registrar
        )

        boton.pack(pady=10)


        self.lbl_total = ctk.CTkLabel(
            self,
            text="Asistentes: 0",
            font=("Arial",18,"bold")
        )

        self.lbl_total.pack(pady=15)


        self.lista = ctk.CTkTextbox(
            self,
            width=600,
            height=300,
            font=("Consolas",16)
        )

        self.lista.pack(pady=20)


    # ==========================================

    def registrar(self):

        nombre = self.entry_nombre.get()

        if nombre == "":
            return

        ok,mensaje = self.excel.registrar(nombre)

        if not ok:

            messagebox.showwarning(
                "Aviso",
                mensaje
            )

            return

        self.asistentes.append(mensaje)

        self.actualizar_lista()

        self.entry_nombre.delete(0,"end")


    # ==========================================

    def actualizar_lista(self):

        self.lista.delete("1.0","end")

        for jugador in self.asistentes:

            self.lista.insert(
                "end",
                "✓ "+jugador+"\n"
            )

        self.lbl_total.configure(
            text=f"Asistentes: {len(self.asistentes)}"
        )