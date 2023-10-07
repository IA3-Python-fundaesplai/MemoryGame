# Clase Card para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/10/07
# Última actualización: 2023/10/07
# Versión: 1.0

import unittest
from card import Card


class TestCard(unittest.TestCase):
    def test_card_creation(self):
        # Prueba de creación de cartas con palo y valor válidos
        card = Card("Corazones", "2")
        self.assertEqual(card.suit, "Corazones")
        self.assertEqual(card.value, "2")

        # Prueba de creación de carta con palo no válido
        with self.assertRaises(ValueError):
            Card("InvalidSuit", "2")

        # Prueba de creación de carta con valor no válido
        with self.assertRaises(ValueError):
            Card("Corazones", "InvalidValue")

    def test_card_representation(self):
        card = Card("Diamantes", "Rey")
        self.assertEqual(repr(card), "Carta: Rey de Diamantes")

    def test_generate_all_cards(self):
        all_cards = Card.generate_all_cards()
        self.assertEqual(len(all_cards), 52)

    def test_shuffle_pairs(self):
        number_of_pairs = 5
        shuffled_pairs = Card.shuffle_pairs(number_of_pairs)
        self.assertEqual(len(shuffled_pairs), number_of_pairs * 2)


if __name__ == '__main__':
    unittest.main()
