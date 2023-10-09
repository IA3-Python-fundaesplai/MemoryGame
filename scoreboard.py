# Clase Scoreboard gestionar las puntuaciones del usuario.
# Creado por: Aitor & Jon
# GitHub: https://www.github.com/aitorias | https://www.github.com/jonfdz
# Fecha creación: 2023/09/22
# Última actualización: 2023/10/09
# Versión: 1.0

import art
import datetime
import json
import locale
from functools import reduce

from log import Log


class Scoreboard:
    def __init__(self):
        """
        Constructor de la clase Scoreboard
        """
        self.user = "player_1"
        self.language = locale.getdefaultlocale()[0]
        self.scores = {}

        self.log = Log(log_file=f'{self.user}-log.log')

    def __str__(self):
        """
        Representación de una instancia de la clase Scoreboard
        """
        return f"Jugador: {self.user} | Puntuaciones: {self.scores}"

    def get_actual_date(self):
        """
        Función que retorna la fecha actual formatada según el idioma del sistema
        """
        try:
            # Formatear la fecha para sistemas en inglés
            if self.language in ["en_GB", "en_US"]:
                date_format = "%A %d %B %Y"
            elif (
                self.language == "es_ES"
            ):  # Formatear la fecha para sistemas en español
                date_format = "%A %d de %B de %Y"
            else:  # Formato de fecha para cualquier otro idioma
                date_format = "%A %d %B %Y"
            locale.setlocale(locale.LC_TIME, self.language)
        except locale.Error as error:
            self.log.log_error(f"Locale error occurred: {error}")
        return datetime.datetime.now().strftime(date_format)

    def get_scores(self):
        """
        Función que carga las puntuaciones desde el archivo JSON y si no existe lo crea
        """
        try:
            with open("scores.json", "r") as file:
                scores = json.load(file)
        except FileNotFoundError:
            print(
                "No tienes puntuaciones previas. A partir de ahora guardaremos tus puntuaciones.")
            scores = {}
        except json.decoder.JSONDecodeError as error:
            scores = {}
            self.log.log_error(
                f"File not found error: creating file. Error: {error}")
        return scores

    def save_scores(self):
        """
        Función que guarda las puntuaciones en el archivo JSON
        """
        with open("scores.json", "w", encoding="UTF-8") as file:
            json.dump(self.scores, file, ensure_ascii=False)

    def add_score(self, score):
        """
        Función para añadir una nueva puntuación al scoreboard
        """
        date = self.get_actual_date()
        self.user = input("Introduzca su nombre: ").upper()
        self.scores = self.get_scores()

        if self.user in self.scores.keys():
            self.scores[self.user].append((score, date))
        else:
            self.scores[self.user] = [(score, date)]

        self.save_scores()

        log_message = f'Puntuación {score} para el jugador {self.user} en {date} añadida correctamente.'
        self.log.log_info(log_message)

    def parse_list(self, item):
        username = item[0]
        score, date = reduce(lambda a, b: a if a[0] > b[0] else b, item[1])
        return [username, score, date]

    def print_scoreboard(self):
        """
        Funcion para printear la clasificacion ordenada en pantalla
        """
        quit = ""

        while quit == "":
            print(art.scoreboard_art)
            print("\n\n")

            scores = self.get_scores()
            parsed_scores = []
            count = 1

            parsed_scores = list(map(self.parse_list, scores.items()))

            parsed_scores.sort(key=lambda x: x[1], reverse=True)

            for user in parsed_scores:
                print(
                    f"{count}.- {user[0]}: {user[1]} puntos | Fecha: {user[2]}")
                count += 1

            quit = input("\nPulse enter para volver al menu.")
            break
