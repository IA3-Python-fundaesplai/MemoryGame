# Clase MemoryCards para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/29
# Última actualización: 2023/10/07
# Versión: 1.0

from memory_cards import MemoryCards
from scoreboard import Scoreboard


class Game(MemoryCards):
    """
    Clase que gestiona la lógica de un juego de tarjetas de memoria.

    Atributos:
        scoreboard (Scoreboard): Una instancia de la clase Scoreboard utilizada para gestionar las puntuaciones de los jugadores.
    """

    def __init__(self):
        """
        Constructor de la clase Game
        """
        self.scoreboard = Scoreboard()

    def calculate_turns(self, number_of_cards):
        """
        Calcula el número de turnos necesarios para completar una ronda en función del número de cartas.

        Args:
            number_of_cards (int): El número de cartas de la ronda.

        Return:
            int: El número de turnos necesarios para completar la ronda.
        """
        num_pairs = number_of_cards // 2
        minimum_turns = num_pairs + 2

        return minimum_turns

    def calculate_score(self, turns_left, max_turns, max_score):
        """
        Calcula la puntuación del jugador en función de los turnos restantes.

        Args:
            turns_left (int): El número de turnos restantes.
            max_turns (int): El número máximo de turnos permitidos.
            max_score (int): La puntuación máxima posible.

        Return:
            int: La puntuación calculada.
        """
        turns_left = max(0, min(turns_left, max_turns))
        score = max_score * (turns_left / max_turns)
        return round(score)

    def play_game(self, num_cards, max_rounds):
        """
        Gestiona la lógica del juego de cartas de memoria, incluyendo el número de rondas, turnos y puntuación.

        Args:
            num_cards (int): El número de cartas en el juego.
            max_rondas (int): El número máximo de rondas a jugar.
        """
        current_round = 1

        while current_round <= max_rounds:
            num_cards_round = num_cards + current_round - 1
            cards = MemoryCards.shuffle_pairs(num_cards_round)
            user_turns = self.calculate_turns(num_cards_round)
            matched_pairs = 0
            user_score = 0

            while user_turns > 0:
                if len(cards) == 2 and cards[0].is_same_as(cards[1]):
                    cards[0].matched = True
                    cards[1].matched = True
                    matched_pairs += 1
                    user_score = self.calculate_score(
                        user_turns, max_turns, 100)

                user_turns -= 1

            if matched_pairs == num_cards_round // 2:
                current_round += 1
            elif user_turns == 0 and matched_pairs > 0:
                self.scoreboard.add_score(user_score)
                break
            elif user_turns == 0 and matched_pairs == 0:
                user_score = 0
                self.scoreboard.add_score(user_score)
                break


# Prueba de juego
num_cards = 8
max_turns = 5
game = Game()
# turns = game.calculate_turns(num_cards)
# print(turns)
# score_test = game.calculate_score(5, turns, 100)
# print(score_test)
game.play_game(num_cards, max_turns)
