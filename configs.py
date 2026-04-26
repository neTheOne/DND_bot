import os

import configparser


config = configparser.ConfigParser()
config.read("configs/config.ini")

USER = os.getenv('USER_POSTGRES_DATABASE')
PASSWORD = os.getenv('PASSWORD_POSTGRES_DATABASE')
HOST = config["DB_INFO"]["HOST"]
PORT = config["DB_INFO"]["PORT"]
DB_INFO = config["DB_INFO"]["DB_INFO_NAME"]
DB_MAIN = config["DB_INFO"]["DB_MAIN_NAME"]

TOKEN = os.getenv('TG_CLIST_DND_BOT_TOKEN')

PROTOCOL = config["PROXY"]["PROTOCOL"]
ADDRESS = config["PROXY"]["ADDRESS"]