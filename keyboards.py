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
                                                     callback_data=f"choise_class_confirm_{class_id}")
        button_list.append(class_button)

    keyboard.add(*button_list)
    return keyboard


def class_choise_keyboard(class_id: int):
    """
    :param class_id: class_id - id класса
    Вывод клавиатуры с выбором дальнейших действий выбора класса
    :return: inline клавиатура
    """
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton(text="Назад",
                                             callback_data=f'choise_class')
    forward_button = types.InlineKeyboardButton(text="Подтверждаю. Продолжить создание",
                                                callback_data=f'choise_race')
    info_button = types.InlineKeyboardButton(text="Вывести подробную информацию",
                                             callback_data=f'confirm_class_info_{class_id}')

    button_list = [back_button, forward_button, info_button]
    keyboard.add(*button_list)

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
                                                     callback_data=f"choise_race_confirm_{race_id}")
        button_list.append(race_button)

    keyboard.add(*button_list)
    return keyboard


def race_choise_keyboard(race_id: int):
    """
    :param race_id: race_id - id расы
    Вывод клавиатуры с выбором дальнейших действий выбора расы
    :return: inline клавиатура
    """
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton(text="Назад",
                                             callback_data=f'choise_race')
    forward_button = types.InlineKeyboardButton(text="Подтверждаю. Продолжить создание",
                                                callback_data=f'choise_background')
    info_button = types.InlineKeyboardButton(text="Вывести подробную информацию",
                                             callback_data=f'confirm_race_info_{race_id}')
    button_list = [back_button, forward_button, info_button]
    keyboard.add(*button_list)

    return keyboard


def background_review_keyboard():
    """
    Вывод inline клавиатуры со всеми предысториями
    :return: inline клавиатура
    """
    background_data_info = databases.get_background_id()
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button_list = []

    for race_data in background_data_info:
        background_id = race_data[0]
        background_name = race_data[1]
        background_button = types.InlineKeyboardButton(text=background_name,
                                                     callback_data=f"choise_background_confirm_{background_id}")
        button_list.append(background_button)

    keyboard.add(*button_list)
    return keyboard


def background_choise_keyboard(background_id: int):
    """
    :param background_id: background_id - id предыстории
    Вывод клавиатуры с выбором дальнейших действий выбора предыстории
    :return: inline клавиатура
    """
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton(text="Назад",
                                             callback_data=f'choise_background')
    forward_button = types.InlineKeyboardButton(text="Подтверждаю. Продолжить создание",
                                                callback_data=f'choise_background')
    info_button = types.InlineKeyboardButton(text="Вывести подробную информацию",
                                             callback_data=f'confirm_background_info_{background_id}')
    button_list = [back_button, forward_button, info_button]
    keyboard.add(*button_list)

    return keyboard
