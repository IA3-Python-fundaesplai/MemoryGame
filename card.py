# Clase Card para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/29
# Última actualización: 2023/09/29
# Versión: 1.0

class Card():
    """
    Clase Card
    """
    SUITS = ["Corazones", "Diamantes", "Picas", "Tréboles"]
    VALUES = ["2", "3", "4", "5", "6", "7", "8",
              "9", "10", "Jota", "Reina", "Rey", "As"]

    def __init__(self, suit, value):
        """
        Constructor de la clase Card
        """
        if suit in self.SUITS and value in self.VALUES:
            self.suit = suit
            self.value = value
        else:
            raise ValueError("Error en el palo o valor de la carta")

    def __str__(self):
        """
        Representación de una instancia de la clase Scoreboard
        """
        return f'Carta: {self.value} de {self.suit}\n'

    @classmethod
    def generate_all_cards(cards):
        """
        Función para generar todas las cartas
        """
        deck = [cards(suit, value)
                for suit in cards.SUITS for value in cards.VALUES]
        return deck
