import configparser


config = configparser.ConfigParser()
config.read("config.ini")

USER = config["DB_INFO"]["USER"]
PASSWORD = config["DB_INFO"]["PASSWORD"]
HOST = config["DB_INFO"]["HOST"]
PORT = config["DB_INFO"]["PORT"]
DB_INFO_NAME = config["DB_INFO"]["DB_INFO_NAME"]
DB_MAIN_INFO = config["DB_INFO"]["DB_MAIN_NAME"]

TOKEN = config["DB_INFO"]["TOKEN"]

PROTOCOL = config["DB_INFO"]["PROTOCOL"]
ADDRESS = config["DB_INFO"]["ADDRESS"]