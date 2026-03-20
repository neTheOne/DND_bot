"""Модуль с клавиатурами"""
from telebot import types
import databases


def main_menu():
    '''
    Функция для создания клавиатуры главного меню
    :return: клавиатура
    '''
    menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    add_pers = types.KeyboardButton(text="Создать персонажа")
    view_pers = types.KeyboardButton(text="Мои персонажи")
    menu_keyboard.add(add_pers, view_pers)

    return menu_keyboard


def class_review_keyboard():
    """
    Вывод inline клавиатуры со всему классами
    :return: inline клавиатура
    """
    class_data_info = databases.get_class_id()
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button_list = []

    for class_data in class_data_info:
        class_id = class_data[0]
        class_name = class_data[1]
        class_button = types.InlineKeyboardButton(text=class_name,
                                                     callback_data=f"class_{class_id}")
        button_list.append(class_button)

    keyboard.add(*button_list)
    return keyboard


def class_choise_keyboard():
    """
    Вывод клавиатуры с выбором дальнейших действий выбора класса
    :return: inline клавиатура
    """
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="Назад",
                                             callback_data='back_choise_class')
    forward_button = types.InlineKeyboardButton(text="Подтверждаю. Продолжить создание",
                                                callback_data='choise_class_yes')
    info_button = types.InlineKeyboardButton(text="Вывести подробную информацию",
                                             callback_data='show_class_info')
    keyboard.add(back_button, forward_button, info_button)

    return keyboard

def race_review_keyboard():
    """
    Вывод inline клавиатуры со всеми расами
    :return: inline клавиатура
    """
    race_data_info = databases.get_race_id()
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button_list = []

    for race_data in race_data_info:
        race_id = race_data[0]
        race_name = race_data[1]
        race_button = types.InlineKeyboardButton(text=race_name,
                                                     callback_data=f"race_{race_id}")
        button_list.append(race_button)

    keyboard.add(*button_list)
    return keyboard
