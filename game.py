# Clase MemoryCards para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/29
# Última actualización: 2023/09/30
# Versión: 1.0

from memory_cards import MemoryCards
from scoreboard import Scoreboard


class Game(MemoryCards):
    def __init__(self):
        """
        Constructor de la clase Game
        """
        self.scoreboard = Scoreboard()

    def calculate_turns(self, number_of_cards):
        """
        Método para calcular los turnos para completar una ronda
        """
        num_pairs = number_of_cards // 2
        minimum_turns = num_pairs + 2

        return minimum_turns

    def calculate_score(self, turns_left, max_turns, max_score):
        """
        Método para calcular la puntuación del usuario basada en los turnos restantes.
        """
        # Instanciamos una variable para calcular los turnos restantes del usuario
        turns_left = max(0, min(turns_left, max_turns))

        # Calculamos al puntuación del usuario según los turnos
        score = max_score * (turns_left / max_turns)

        # Retornamos la puntuación
        return round(score)

    def play_game(self, num_cards, max_rounds):
        """
        Método para la lógica del juego de memoria
        """
        current_round = 1

        # Repetimos el juego por el máximo número de rondas seleccionadas
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

            # Si el jugador a acertado todas las parejas, pasa a la siguiente ronda
            if matched_pairs == num_cards_round // 2:
                current_round += 1
            # Si el jugador se queda sin turnos, pero ha acertado alguna pareja, guardamos su puntuación
            elif user_turns == 0 and matched_pairs > 0:
                # Guardamos la puntuación del usuario
                self.scoreboard.add_score(user_score)
                break
            # Si el jugador se ha quedado sin turnos y no ha acertado ni una sola pareja
            elif user_turns == 0 and matched_pairs == 0:
                user_score = 0
                # Guardamos la puntuación del usuario
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
