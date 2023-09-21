# Clase Cards se encarga de gestionar las cartas del juego.
# Creado por JonFdz
# GitHub: https://www.github.com/jonfdz
# Versión: 1.0

from tkinter import *

class Cards:
    """Clase Cards que se encargara de gestionar todas las funcionalidades de las cartas."""
    def __init__(self) -> None:
        self.back_img = PhotoImage(file="images/back_card.png")
        self.card_front_img = PhotoImage(file="images/ace_of_hearts.png")
        self.cards_list = self.list_cards(0, 8, self.back_img)
        self.count = 0

    def choice_card(self, index):
        """Funcion que gestiona la seleccion de la carta. Determina que carta se pulsa y el color que la sobresalta para formar las parejas."""
        if self.count < 2:
            self.count += 1
            return self.cards_list[index].configure(
                image=self.card_front_img, highlightthickness=5, highlightbackground="red"
            )
        elif self.count < 4:
            self.count += 1
            return self.cards_list[index].configure(
                image=self.card_front_img, highlightthickness=5, highlightbackground="blue"
            )
        elif self.count < 6:
            self.count += 1
            return self.cards_list[index].configure(
                image=self.card_front_img, highlightthickness=5, highlightbackground="yellow"
            )
        else:
            self.count += 1
            return self.cards_list[index].configure(
                image=self.card_front_img, highlightthickness=5, highlightbackground="green"
            )

    def generate_card(self, index, image):
        """Funcion que genera un boton que representa una carta."""
        return Button(
            image=image,
            highlightthickness=5,
            highlightbackground="#B1DDC6",
            command=lambda: self.choice_card(index),
        )

    def list_cards(self, x, y, image):
        """Funcion que genera una lista de botones que representa las cartas."""
        list_cards = []
        for number in range(x, y):
            if number < 4:
                list_cards.append(self.generate_card(number, image))
                list_cards[number].grid(
                    row=0, column=number, rowspan=2, pady=20, padx=20
                )
            else:
                list_cards.append(self.generate_card(number, image))
                list_cards[number].grid(
                    row=3, column=number - 4, rowspan=2, pady=20, padx=20
                )
        return list_cards
