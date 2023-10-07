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

    def __repr__(self) -> str:
        """
        Devuelve una representación de texto de una instancia de carta.

        Devuelve
            str: La representación en texto de la carta.
        """
        return f'Carta: {self.value} de {self.suit}'

    @classmethod
    def generate_all_cards(cls) -> List['Card']:
        """
        Genera una lista de todas las cartas posibles.

        Devuelve:
            List['Card']: Una lista de todas las cartas posibles.
        """
        return [cls(suit, value) for suit in cls.SUITS for value in cls.VALUES]

    @classmethod
    def shuffle_pairs(cls, number_of_cards: int) -> List['Card']:
        """
        Genera una lista de pares de cartas barajadas.

        Args:
            number_of_cards (int): El número de pares de cartas a generar.

        Devuelve:
            List['Card']: Una lista de pares de cartas barajadas.
        """
        random_cards = []
        all_suits = cls.SUITS
        all_values = cls.VALUES

        for _ in range(number_of_cards):
            suit = random.choice(all_suits)
            value = random.choice(all_values)
            card1 = cls(suit, value)
            card2 = cls(suit, value)
            random_cards.extend([card1, card2])

        random.shuffle(random_cards)

        return random_cards


card_1 = Card.shuffle_pairs(6)
print(card_1)
