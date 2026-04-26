'''Модуль для импорта данных'''
import json

def read_js(filepath:str) -> tuple:
    """
    Функция чтения json-файла
    :param filepath: путь к файлу
    :return: данные передаваемого json
    """
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

