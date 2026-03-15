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


def back_button():
    '''
    Функция для создания кнопки назад под сообщением
    :return: кнопка
    '''
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="Назад",
                                                     callback_data='back')
    keyboard.add(back_button)

    return keyboard


def class_button():
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