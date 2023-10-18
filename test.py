import customtkinter as ctk
from tkinter import PhotoImage, Button

# Constants
BACKGROUND_COLOR = "#B1DDC6"


class App(ctk.CTk):
    def __init__(self):
        # Setup principal
        super().__init__()
        self.title("Memory Game")
        self.geometry("1250x850")

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for Frame in (Menu, Game):
            frame = Frame(container, controller=self)
            frame.grid(row=0, column=0, sticky="NEWS")
            self.frames.update({Frame.__name__: frame})
        self.show_frame("Menu")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Menu(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color=BACKGROUND_COLOR)
        self.pack(expand=True)

        self.bg_img = PhotoImage(file="images/assets/fondo_menu.png")
        self.bg_canvas = ctk.CTkCanvas(self)
        self.bg_canvas.pack(expand=True, fill="both")
        self.bg_canvas.create_image(0, 0, image=self.bg_img, anchor="nw")

        # self.score_frame = ctk.CTkFrame(master=self.bg_canvas, bg_color="transparent")
        # self.score_frame.pack(expand=True, padx=50, pady=50, fill="both", side="left")

        self.score_label = ctk.CTkLabel(
            master=self.bg_canvas,
            text="1. JON 45p",
        )
        self.score_label.place(x=300, y=350)

        self.button_play_img = PhotoImage(file="images/assets/boton_jugar.png")
        self.button_play = Button(
            master=self.bg_canvas,
            image=self.button_play_img,
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="black",
            command=lambda: controller.show_frame("Game"),
        )
        self.button_play.place(x=840, y=150)
        # self.button_play.grid(row=0, column=1, padx=50, pady=50, sticky="e")
        self.button_help_img = PhotoImage(file="images/assets/boton_reglas.png")
        self.button_help = Button(
            master=self.bg_canvas,
            image=self.button_help_img,
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="black",
            command=lambda: controller.show_frame("Game"),
        )
        self.button_help.place(x=840, y=350)
        # self.button_help.grid(row=1, column=1, padx=50, pady=50)
        self.button_exit_img = PhotoImage(file="images/assets/boton_salir.png")
        self.button_exit = Button(
            master=self.bg_canvas,
            image=self.button_exit_img,
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="black",
            command=lambda: controller.show_frame("Game"),
        )
        self.button_exit.place(x=840, y=550)
        # self.button_score.grid(row=2, column=1, ipadx=70, ipady=20, padx=50, pady=50)


class Game(ctk.CTkFrame):
    """Clase Game que se encargara de gestionar todas las funcionalidades del juego."""

    def __init__(self, master, controller) -> None:
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color=BACKGROUND_COLOR)

        self.bg_img = PhotoImage(file="images/assets/fondo.png")
        self.bg_canvas = ctk.CTkCanvas(self)
        self.bg_canvas.pack(expand=True, fill="both")
        self.bg_canvas.create_image(0, 0, image=self.bg_img, anchor="nw")

        self.back_img = PhotoImage(file="images/cards/back_card.png")
        self.card_front_img = PhotoImage(file="images/cards/ace_of_hearts.png")
        self.card_list = []
        self.count = 0
        self.choice = []

        self.list_cards(0, 8),


    def generate_card(self, index, image):
        """Funcion que genera un boton que representa una carta."""
        return ctk.CTkButton(
            master=self.bg_canvas,
            image=image,
            fg_color="#B1DDC6",
            text="",
            command=lambda: self.choice_card(index),
        )

    def list_cards(self, x, y):
        """Funcion que genera una lista de botones que representa las cartas."""
        for widget in self.bg_canvas.winfo_children():
            widget.destroy()
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
        self.after(3000, self.flip_cards)

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

    def flip_cards(self):
        """Funcion para esconder las cartas."""
        for card in range(0, 8):
            self.cards_list[card].configure(image=self.back_img)

    def destroy_cards(self):
        """Funcion para detruir las cartas de la ventana."""
        for index in range(0, len(self.cards_list)):
            if isinstance(self.cards_list[index], ctk.CTkButton):
                self.cards_list[index].destroy()
