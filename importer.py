'''Модуль для импорта данных'''
import json

def read_js(filepath) -> tuple:
    """
    Функция чтения json-файла
    :param filepath: путь к файлу
    :return: данные передаваемого json
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data

