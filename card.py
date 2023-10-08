# Clase Card para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/29
# Última actualización: 2023/10/07
# Versión: 1.0

from typing import List


class Card:
    """
    Clase que representa una carta con un palo y un valor.

    Atributos:
        SUITS (tuple): Una tupla que contiene los posibles palos de una carta.
        VALUES (tuple): Una tupla que contiene los posibles valores de una carta.
        suit (str): El palo de la carta.
        value (str): El valor de la carta.
        flipped (bool): Indica si la carta está boca arriba o boca abajo.


    Métodos:
        __init__(self, suit: str, value: str) -> None: Inicializa una carta con un palo y un valor dados.
        __repr__(self) -> str: Devuelve una representación de texto de una instancia de carta.
        generate_all_cards(cls) -> List['Card']: Genera una lista de todas las cartas posibles.
        flip(self) -> None: Voltea la carta para cambiar su estado boca arriba o boca abajo.
    """

    SUITS = ("♥️", "♦️", "♠", "♣️")
    VALUES = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self, suit: str, value: str) -> None:
        """
        Inicializa una carta con un palo y un valor dados.

        Args:
            suit (str): El palo de la carta.
            value (str): El valor de la carta.

        Se produce:
            ValueError: Si el palo o el valor no son válidos.
        """
        if suit not in self.SUITS:
            raise ValueError("El palo de la carta no es válido.")
        elif value not in self.VALUES:
            raise ValueError("El valor de la carta no es válido")

        self.suit = suit
        self.value = value
        self.flipped = True

    def __repr__(self) -> str:
        """
        Devuelve una representación de texto de una instancia de carta.

        Devuelve
            str: La representación en texto de la carta.
        """
        if self.flipped:
            return f"| {self.value}{self.suit} |"
        else:
            return "| <> |"

    def flip(self) -> None:
        """
        Voltea la carta para cambiar su estado boca arriba o boca abajo.
        """
        self.flipped = not self.flipped

    @classmethod
    def generate_all_cards(cls) -> List["Card"]:
        """
        Genera una lista de todas las cartas posibles.

        Devuelve:
            List['Card']: Una lista de todas las cartas posibles.
        """
        return [cls(suit, value) for suit in cls.SUITS for value in cls.VALUES]
