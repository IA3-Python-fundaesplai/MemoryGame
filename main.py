# Juego MemoryCards
# Creado por Aitor & Jon
# GitHub: https://www.github.com/aitorias | https://www.github.com/jonfdz
# Fecha creación: 2023/09/29
# Última actualización: 2023/10/09
# Versión: 1.0

from game import *
import scoreboard
import art
import time

def cls() -> None:
    """
    Limpia la pantalla de la consola.
    """
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":

    while True:
        cls()
        print(art.welcome)
        choice = input(
            "Seleccione una opción: \n \
            1. Jugar \n \
            2. Clasificación \n \
            3. Salir \n"
        )
        if choice == "3":
            break
        elif choice == "1":
            app = Game()
        elif choice == "2":
            cls()
            scoreboard = Scoreboard()
            scoreboard.print_scoreboard()
        else:
            print("Opcion no permitida.")
            time.sleep(2)
            cls()
