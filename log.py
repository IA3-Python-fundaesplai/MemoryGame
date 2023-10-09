# Clase Log para guardar registros de partidas de los usuarios
# Creado por: Aitor & Jon
# GitHub: https://www.github.com/aitorias | https://www.github.com/jonfdz
# Fecha creación: 2023/09/20
# Última actualización: 2023/09/29
# Versión: 1.0

import datetime
import locale
import logging
import os


class Log:
    def __init__(self):
        """
        Constructor de la clase Log
        """
        user = self.get_player_username()
        self.user = user
        self.language = locale.getdefaultlocale()[0]
        self.log_file = f'{self.user}-log.log'
        logging.basicConfig(filename=self.log_file, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def __str__(self):
        """
        Representación de una instancia de la clase Log
        """
        return f'Jugador: {self.user}'

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
            username = input("Introduzca su nombre:")
        return f'{username}'

    def get_actual_date(self):
        """
        Función que retorna la fecha actual formatada según el idioma del sistema
        """
        try:
            # Formatear la fecha para sistemas en inglés
            if self.language in ['en_GB', 'en_US']:
                date_format = '%A %d %B %Y'
            elif self.language == 'es_ES':  # Formatear la fecha para sistemas en español
                date_format = '%A %d de %B de %Y'
            else:  # Formato de fecha para cualquier otro idioma
                date_format = '%A %d %B %Y'
            locale.setlocale(locale.LC_TIME, self.language)
        except locale.Error as error:
            logging.error(f'Locale error occurred: {error}')
        return datetime.datetime.now().strftime(date_format)

    def generate_file(self):
        """
        Función que genera el archivo donde se guardan las puntuaciones del usuario
        """
        # Instanciamos la fecha actual con su respectivo formato
        date = self.get_actual_date()

        # Abrimos el archivo y actualizamos el contenido
        with open(self.log_file, 'a') as file:
            logging.info(f'Log file generated for {self.user} on {date}')

    def log(self, message):
        """
        Función para guardar los logs
        """
        logging.info(message)
