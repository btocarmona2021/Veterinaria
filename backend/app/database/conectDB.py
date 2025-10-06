import mysql.connector
from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path, override=True)


class conectarDB:
    @staticmethod
    def conectar():
        try:
            conn = mysql.connector.connect(
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
            )
            print("Conectado correctamente a la base de datos")
            return conn

        except Exception as ex:
            print(f"Error al conectar con la base de datos{ex}")
