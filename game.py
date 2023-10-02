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

    def play_game(self, num_cards):
        """
        Método para la lógica del juego de memoria
        """
        random_memory_cards, minimum_turns = MemoryCards.generate_random_memory_cards(
            num_cards)
        print(
            f'El número mínimo de turnos para finalizar el juego con {num_cards} cartas es: {minimum_turns}')

        # Inicializamos la puntuación inicial del usuario y el número mínimo de turnos
        user_score = 0
        user_turns = minimum_turns
        matched_pairs = 0

        while user_turns > 0:
            # TODO: Implementar la lógica para el flip de cartas
            # Disminuir los turnos a medida que el usuario juega
            user_turns -= 1

            # Verificamos si el juego ha finalizado
            if MemoryCards.is_game_over(random_memory_cards):
                # Calculamos la puntuación final del usuario
                user_score += MemoryCards.calculate_score(
                    user_turns, minimum_turns, 100)
                print('El juego ha finalizado.')
                break

            flipped_cards = MemoryCards.get_flipped_cards(random_memory_cards)
            if len(flipped_cards) == 2 and flipped_cards[0].is_same_as(flipped_cards[1]):
                flipped_cards[0].matched = True
                flipped_cards[1].matched = True

        # Si el jugador se queda sin turnos, pero ha acertado alguna pareja, guardamos su puntuación
        if user_turns == 0 and matched_pairs > 0:
            print(
                f'El juego ha finalizado. Tu puntuación ha sido de: {user_score}')
            # Guardamos la puntuación del usuario
            self.scoreboard.add_score(user_score)
        # Si el jugador se ha quedado sin turnos y no ha acertado ni una sola pareja
        elif user_turns == 0 and matched_pairs == 0:
            user_score = 0
            print(
                f'El juego ha finalizado. Tu puntuación ha sido {user_score}. ¡No te desanimes e inténtalo de nuevo!')
            self.scoreboard.add_score(user_score)


# Prueba de juego
num_cards = 8
game = Game()
game.play_game(num_cards)
