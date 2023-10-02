# Clase Cards que se encarga de gestionar las cartas del juego.
# Creado por JonFdz
# GitHub: https://www.github.com/jonfdz
# Versión: 1.0

import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Constants
BACKGROUND_COLOR = "#B1DDC6"


class App(ctk.CTk):
    def __init__(self, size):
        # Setup principal
        super().__init__()
        self.title("Memory Game")
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.configure(padx=50, pady=50, fg_color=BACKGROUND_COLOR)

        frame = ctk.CTkFrame(self)
        frame.pack()

        self.frames = {}
        for Frame in (Menu, Cards):
            frame = Frame(frame, controller=self)
            frame.grid(row=0, column=0, sticky="NEWS")
            self.frames.update({Frame.__name__: frame})
        self.show_frame("Menu")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        # self.frame = None

        # self.button_play = ctk.CTkButton(master=self, text="Jugar", width=200, height=100, command=self.change_frame)
        # self.button_play.pack(ipadx=70, ipady=20, padx=100, pady=50, expand=True)
        # self.button_help = ctk.CTkButton(master=self, text="Instrucciones", width=200, height=100)
        # self.button_help.pack(ipadx=70, ipady=20, padx=100, pady=50, expand=True)
        # self.button_score = ctk.CTkButton(master=self, text="Clasificaciones", width=200, height=100)
        # self.button_score.pack(ipadx=70, ipady=20, padx=100, pady=50, expand=True)

        # self.mainloop()

    # def change_frame(self):
    #     for widget in self.winfo_children():
    #         widget.destroy()
    #     self.frame = Cards(self)
    #     self.frame.tkraise()


class Menu(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.configure(fg_color=self.BACKGROUND_COLOR)
        self.pack(expand=True)
        self.button_play = ctk.CTkButton(master=self, text="Jugar", width=200, height=100, command=lambda: controller.show_frame("Cards"))
        self.button_play.pack(ipadx=70, ipady=20, padx=100, pady=50, expand=True)
        self.button_help = ctk.CTkButton(master=self, text="Instrucciones", width=200, height=100)
        self.button_help.pack(ipadx=70, ipady=20, padx=100, pady=50, expand=True)
        self.button_score = ctk.CTkButton(master=self, text="Clasificaciones", width=200, height=100)
        self.button_score.pack(ipadx=70, ipady=20, padx=100, pady=50, expand=True)

    def change_frame():
        pass
            


class Cards(ctk.CTkFrame):
    """Clase Cards que se encargara de gestionar todas las funcionalidades de las cartas."""

    def __init__(self, master, controller) -> None:
        super().__init__(master)
        self.controller = controller
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.back_img = PhotoImage(file="images/back_card.png")
        self.card_front_img = PhotoImage(file="images/ace_of_hearts.png")
        self.cards_list = self.list_cards(0, 8)
        self.count = 0
        self.choice = []
        self.grid(row=0, column=0)
        self.configure(
            width=1200, height=900, fg_color=self.BACKGROUND_COLOR, border_width=0
        )
        self.button = ctk.CTkButton(
            master=self,
            text="Go back",
            command=lambda: self_hide,
        )

    def self_hide(self):
        self.controller.show_frames("Menu")

    def choice_card(self, index):
        """Funcion que gestiona la seleccion de la carta. Determina que carta se pulsa, cambia el color por parejas y añade la seleccion por orden a la lista choice"""
        self.choice.append(index)
        if self.count < 2:
            self.count += 1
            return self.cards_list[index].configure(
                image=self.card_front_img,
                border_width=5,
                border_color="red",
            )
        elif self.count < 4:
            self.count += 1
            return self.cards_list[index].configure(
                image=self.card_front_img,
                border_width=5,
                border_color="blue",
            )
        elif self.count < 6:
            self.count += 1
            return self.cards_list[index].configure(
                image=self.card_front_img,
                border_width=5,
                border_color="yellow",
            )
        else:
            self.count += 1
            return self.cards_list[index].configure(
                image=self.card_front_img,
                border_width=5,
                border_color="green",
            )

    def generate_card(self, index, image):
        """Funcion que genera un boton que representa una carta."""
        return ctk.CTkButton(
            master=self,
            image=image,
            fg_color="#B1DDC6",
            text="",
            command=lambda: self.choice_card(index),
        )

    def list_cards(self, x, y):
        """Funcion que genera una lista de botones que representa las cartas."""
        list_cards = []
        for number in range(x, y):
            if number < 4:
                list_cards.append(self.generate_card(number, self.card_front_img))
                list_cards[number].grid(
                    row=0, column=number, rowspan=2, pady=20, padx=20
                )
            else:
                list_cards.append(self.generate_card(number, self.card_front_img))
                list_cards[number].grid(
                    row=3, column=number - 4, rowspan=2, pady=20, padx=20
                )
        self.cards_list = list_cards

    def flip_cards(self):
        """Funcion para esconder las cartas."""
        for card in range(0, 8):
            self.cards_list[card].configure(image=self.back_img)

    def destroy_cards(self):
        """Funcion para detruir las cartas de la ventana."""
        for index in range(0, len(self.cards_list)):
            if isinstance(self.cards_list[index], ctk.CTkButton):
                self.cards_list[index].destroy()
