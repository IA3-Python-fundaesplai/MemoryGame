# Clase Scoreboard gestionar las puntuaciones del usuario.
# Creado por Aitor & Jon
# GitHub: https://www.github.com/aitorias | https://www.github.com/jonfdz
# Fecha creación: 2023/09/22
# Última actualización: 2023/10/09
# Versión: 1.0

from functools import reduce
import datetime
import json
import locale
import logging
import os
import art


class Scoreboard:
    def __init__(self):
        """
        Constructor de la clase Scoreboard
        """
        user_loggin = self.get_player_loggin()
        self.user = ""
        self.language = locale.getdefaultlocale()[0]
        self.scores = {}

    def __str__(self):
        """
        Representación de una instancia de la clase Scoreboard
        """
        return f"Jugador: {self.user} | Puntuaciones: {self.scores}"

    def get_player_loggin(self):
        """
        Función que retorna el nombre de usuario de inicio de sesión del sistema
        para utilizarlo como username del juego.
        """
        # Obtenemos el usuario del sistema
        try:
            username_loggin = os.getlogin()
        except OSError:
            """
            Si se usa una máquina virtual o WSL en Windows, os.getlogin() da error.
            Para ello, usamos el módulo de Python pwd para obtener el nombre del usuario de la máquina.
            """
            username_loggin = input("Introduzca su nombre: ")
        return f"{username_loggin}"

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
            logging.error(f"Locale error occurred: {error}")
        return datetime.datetime.now().strftime(date_format)

    def get_scores(self):
        """
        Función que carga las puntuaciones desde el archivo JSON y si no existe lo crea
        """
        try:
            with open("scores.json", "r") as file:
                scores = json.load(file)
        except json.decoder.JSONDecodeError as error:
            scores = {}
            logging.error(f"File not found error: creating file.")
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

            for key in scores.items():
                username = key[0]
                score, date = reduce(lambda a, b: a if a[0] > b[0] else b, key[1])
                parsed_scores.append([username, score, date])

            parsed_scores.sort(key=lambda x: x[1], reverse=True)

            for user in parsed_scores:
                print(f"{count}.- {user[0]} consiguio {user[1]} puntos el {user[2]}")
                count += 1

            quit = input("Pulse enter para volver al menu.")
            break
