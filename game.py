# Clase Game para controlar la lógica del juego
# Creado por: Aitor & Jon
# GitHub: https://www.github.com/aitorias | https://www.github.com/jonfdz
# Fecha creación: 2023/09/29
# Última actualización: 2023/10/08
# Versión: 1.0

import art
import os
import time

# Improtamos las clases MemoryCards y Scoreboard
from memory_cards import MemoryCards
from scoreboard import Scoreboard


class Game(MemoryCards):
    """
    Clase que gestiona la lógica de un juego de tarjetas de memoria.

    Atributos:
        scoreboard (Scoreboard): Una instancia de la clase Scoreboard utilizada para gestionar las puntuaciones de los jugadores.
        num_cards (int): El número de cartas en el juego.
    """

    def __init__(self):
        """
        Constructor de la clase Game.

        Args:
            num_cards (int): El número de cartas en el juego.
        """
        self.scoreboard = Scoreboard()
        self.num_cards = 8
        self.card_pairs = self.num_cards // 2
        self.play_game()

    def calculate_turns(self):
        """
        Calcula el número de turnos necesarios para completar una ronda en función del número de cartas.

        Args:
            number_of_cards (int): El número de cartas de la ronda.

        Return:
            int: El número de turnos necesarios para completar la ronda.
        """
        total_turns = self.card_pairs * 2
        return total_turns

    def cls(self) -> None:
        """
        Limpia la pantalla de la consola.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def print_cards(self, cards):
        """
        Hace print del logo y las cartas
        """
        print(art.logo)
        print("\n")
        print(cards)

    def play_game(self):
        """
        Gestiona la lógica del juego de cartas de memoria, incluyendo el número de rondas, turnos y puntuación.

        Args:
            num_cards (int): El número de cartas en el juego.
        """
        current_round = 1
        matched_pairs = 0
        user_score = 0

        self.cls()

        game_on = True

        while game_on:
            cards = MemoryCards.shuffle_pairs(self.card_pairs)
            user_turns = self.calculate_turns()

            self.print_cards(cards)
            print(
                "\n------------------------------------\nMEMORIZA LAS PAREJAS\n------------------------------------\n"
            )
            time.sleep(2)
            self.cls()

            for card in cards:
                card.flipped = False
            self.print_cards(cards)
            print(
                "\n------------------------------------\nConseguirás puntos segun tus turnos\n------------------------------------\n"
            )

            while user_turns > 0:
                if user_turns == 1:
                    print(
                        f"Ronda {current_round} ---------- ¡Te queda {user_turns} turno! ---------- Puntuación: {user_score}"
                    )
                else:
                    print(
                        f"Ronda {current_round} ---------- Tienes {user_turns} turnos ---------- Puntuación: {user_score}"
                    )

                # Elección de la primera carta
                card_choice1 = int(input("Elige una carta: ")) - 1

                if cards[card_choice1].flipped:
                    self.cls()
                    self.print_cards(cards)
                    print(
                        "\n------------------------------------\nYa has descubierto esta carta. Elige otra pareja:\n------------------------------------\n"
                    )
                    continue

                cards[card_choice1].flip()
                print(cards[card_choice1])

                # Elección de la segunda carta
                card_choice2 = int(input("Elige otra carta: ")) - 1

                if cards[card_choice2].flipped:
                    self.cls()
                    cards[card_choice1].flip()
                    self.print_cards(cards)
                    print(
                        "\n------------------------------------\nYa has descubierto esta carta. Elige otra pareja:\n------------------------------------\n"
                    )
                    continue

                cards[card_choice2].flip()
                print(cards[card_choice2])
                time.sleep(1)

                # Comprobación de si la pareja es correcta o incorrecta
                if MemoryCards.is_same_as(cards[card_choice1], cards[card_choice2]):
                    matched_pairs += 1
                    user_score += user_turns
                    self.cls()
                    self.print_cards(cards)
                    print(
                        "\n------------------------------------\nCorrecto\n------------------------------------\n"
                    )
                else:
                    self.cls()
                    cards[card_choice1].flip()
                    cards[card_choice2].flip()
                    self.print_cards(cards)
                    print(
                        "\n------------------------------------\nIncorrecto\n------------------------------------\n"
                    )

                # Comprobación de si el jugador ha encontrado todas las parejas para pasar de ronda
                if matched_pairs == self.card_pairs:
                    # user_turns = self.calculate_turns() - current_round
                    current_round += 1
                    matched_pairs = 0
                    self.cls()
                    print(art.next_round)
                    time.sleep(3)
                    self.cls()
                    break
                user_turns -= 1

                # Comprueba si se han acabado los turnos para terminar el juego
                if user_turns == 0:
                    self.cls()
                    print(
                        "\n------------------------------------\n¡Te has quedado sin turnos!\n------------------------------------\n"
                    )
                    print(art.game_over)
                    print(
                        f"\n------------------------------------\nHas conseguido {user_score} puntos\n------------------------------------\n"
                    )
                    time.sleep(3)
                    self.cls()
                    game_on = False
                    continue

        # Guarda la puntuacion y vuelve al menu
        self.scoreboard.add_score(user_score)
        print("El juego ha finalizado.")
        time.sleep(3)
