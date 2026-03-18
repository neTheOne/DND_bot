import configparser


config = configparser.ConfigParser()
config.read("configs/config.ini")

USER = config["DB_INFO"]["USER"]
PASSWORD = config["DB_INFO"]["PASSWORD"]
HOST = config["DB_INFO"]["HOST"]
PORT = config["DB_INFO"]["PORT"]
DB_INFO_NAME = config["DB_INFO"]["DB_INFO_NAME"]
DB_MAIN_INFO = config["DB_INFO"]["DB_MAIN_NAME"]

TOKEN = config["TOKENS"]["TOKEN"]

PROTOCOL = config["PROXY"]["PROTOCOL"]
ADDRESS = config["PROXY"]["ADDRESS"]