# Clase MemoryCards para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/29
# Última actualización: 2023/10/07
# Versión: 1.0

import copy
import random
from typing import List

# Importamos la clase Card
from card import Card


class MemoryCards(Card):
    """
    Representa una carta con propieades y métodos para el juego de memorizar.
    Hereda atributos y métodos de la clase Card.

    Atributos:
        matched (bool): Indica si la carta ha sido emparejada en el juego.

    Métodos:
        __init__(self, suit: str, value: str) -> None: Inicializa una carta con un palo y un valor dados.
        is_same_as(card: 'MemoryCards', other_card: 'MemoryCards') -> bool: Comprueba si dos cartas son iguales.
        is_matched(self) -> bool: Comprueba si la carta ha sido emparejada en el juego.
        get_flipped_cards(random_memory_cards: List['MemoryCards']) -> List['MemoryCards']: Devuelve las cartas volteadas.
        shuffle_pairs(cls, number_of_pairs: int) -> List['MemoryCards']: Baraja pares de cartas para el juego de memoria.
    """

    def __init__(self, suit: str, value: str):
        """
        Inicializa una carta con un palo y un valor.
        Establece el atributo coincidente en False.

        Args:
            suit (str): El palo de la carta.
            value (str): El valor de la carta.
        """
        super().__init__(suit, value)
        self.matched = False

    @staticmethod
    def is_same_as(card: "MemoryCards", other_card: "MemoryCards") -> bool:
        """
        Comprueba si dos cartas son iguales comparando sus valores y palos.

        Args:
            card (MemoryCards): La primera carta.
            other_card (MemoryCards): La segunda carta.

        Devuelve:
            bool: True si las cartas son iguales, False en caso contrario.
        """
        return card.value == other_card.value and card.suit == other_card.suit

    def is_matched(self) -> bool:
        """
        Comprueba si la carta coincide comprobando el atributo matched.

        Devuelve:
            bool: True si la carta coincide, False en caso contrario.
        """
        return self.matched

    @staticmethod
    def get_flipped_cards(
        random_memory_cards: List["MemoryCards"],
    ) -> List["MemoryCards"]:
        """
        Devuelve una lista de cartas volteadas a partir de una lista de cartas aleatoria.

        Args:
            random_memory_cards (Lista['MemoryCards']): La lista de cartas aleatorias.

        Devuelve:
            List['MemoryCards']: La lista de cartas aleatorias.
        """
        return [card for card in random_memory_cards if card.flipped]

    @classmethod
    def shuffle_pairs(cls, number_of_pairs: int) -> List["MemoryCards"]:
        """
        Método de clase que baraja pares de cartas.
        Genera una lista de pares de cartas seleccionando aleatoriamente cartas de entre todas las posibles y luego barajando la lista.

        Args:
            number_of_pairs (int): El número de pares de cartas a generar.

        Devuelve:
            List['MemoryCards']: Una lista de pares de cartas barajadas.
        """
        all_cards = cls.generate_all_cards()
        random_pairs = random.sample(all_cards, number_of_pairs)

        random_cards = [copy.deepcopy(card) for card in random_pairs] + [
            copy.deepcopy(card) for card in random_pairs
        ]

        random.shuffle(random_cards)

        return random_cards
