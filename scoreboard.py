# Clase Scoreboard para guardar el registro de puntuaciones del usuario.
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha: 2023/09/22
# Versión: 1.0

import datetime
import locale
import os
import pwd


class Scoreboard:
    def __init__(self, scores, language='en_US'):
        """
        Constructor de la clase Scoreboard
        """
        user = self.get_player_username()
        self.user = user
        self.scores = scores
        self.language = language

    def __str__(self):
        """
        Representación de una instancia de la clase Scoreboard
        """
        return f'Jugador: {self.user} | Puntuaciones: {self.scores}'

    def get_player_username(self):
        """
        Función que retorna el nombre de usuario de inicio de sesión del sistema 
        para utilizarlo como username del juego.
        """
        # Obtenemos el usuario del sistema
        try:
            username = os.getlogin()
        except OSError:
            '''
            Si se usa una máquina virtual o WSL en Windows, os.getlogin() da error.
            Para ello, usamos el módulo de Python pwd para obtener el nombre del usuario de la máquina.
            '''
            username = pwd.getpwuid(os.getuid()).pw_name
        return f'{username}'

    def get_actual_date(self):
        """
        Función que retorna la fecha actual formatada según el idioma del sistema
        """
        try:
            # Formatear la fecha para sistemas en inglés
            if self.language in ['en_UK', 'en_US']:
                date_format = '%A %d %B %Y'
            elif self.language == 'es_ES':  # Formatear la fecha para sistemas en español
                date_format = '%A %d de %B de %Y'
            else:  # Formato de fecha para cualquier otro idioma
                date_format = '%A %d %B %Y'
            locale.setlocale(locale.LC_TIME, self.language)
        except locale.Error:
            pass
        return datetime.datetime.now().strftime(date_format)

    def get_scores(self, user, scores):
        pass

    def save_scores(self, user, scores):
        pass


# Instanciamos el objeto de la clase Scoreboard
scoreboard = Scoreboard()
