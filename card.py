# Clase Card para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/29
# Última actualización: 2023/10/07
# Versión: 1.0

from typing import List
import random


class Card:
    """
    Clase que representa una carta con un palo y un valor.

    Atributos:
        SUITS (tuple): Una tupla que contiene los posibles palos de una carta.
        VALUES (tuple): Una tupla que contiene los posibles valores de una carta.
        suit (str): El palo de la carta.
        value (str): El valor de la carta.

    Métodos:
        __init__(self, suit: str, value: str) -> None: Inicializa una carta con un palo y un valor dados.
        __repr__(self) -> str: Devuelve una representación de texto de una instancia de carta.
        generate_all_cards(cls) -> List['Card']: Genera una lista de todas las cartas posibles.
        shuffle_pairs(cls, number_of_cards: int) -> List['Card']: Genera una lista de pares de cartas barajadas.
    """

    SUITS = ("Corazones", "Diamantes", "Picas", "Tréboles")
    VALUES = ("2", "3", "4", "5", "6", "7", "8",
              "9", "10", "Jota", "Reina", "Rey", "As")

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
            return f'Carta: {self.value} de {self.suit}'
        else:
            return "Card: [Flipped Down]"

    @classmethod
    def generate_all_cards(cls) -> List['Card']:
        """
        Genera una lista de todas las cartas posibles.

        Devuelve:
            List['Card']: Una lista de todas las cartas posibles.
        """
        return [cls(suit, value) for suit in cls.SUITS for value in cls.VALUES]


    def flip(self):
        """
        Método para voltear la carta
        """
        self.flipped = not self.flipped
