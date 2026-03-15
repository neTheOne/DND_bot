"""Модуль с клавиатурами"""
from telebot import types
import databases


back_button = types.InlineKeyboardButton(text="Назад", callback_data='back')
forward_button = types.InlineKeyboardButton(text="Продолжить создание", callback_data='forward')
info_button = types.InlineKeyboardButton(text="Вывести подробную информацию", callback_data='full_info')


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


def class_review_button():
    """
    Вывод inline клавиатуры со всему классами
    :param class_names: имена классов
    :return: inline клавиатура
    """
    class_names = databases.get_class_info()
    keyboard = types.InlineKeyboardMarkup()
    for class_data in class_names:
        class_id = class_data[0]
        class_name = class_data[1]
        class_button = types.InlineKeyboardButton(text=class_name,
                                                     callback_data=f"class_{class_id}")
        keyboard.add(class_button)

    return keyboard


def class_info_button():
    """
    Вывод клавиатуры с выбором дальнейших действий
    :return: inline клавиатура
    """
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(back_button, forward_button, info_button)


def back_button():
    """
    Кнопка возвращения на шаг назад
    :return: inline клавиатура
    """
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(back_button)