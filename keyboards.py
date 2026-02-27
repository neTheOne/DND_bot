"""Модуль с клавиатурами"""
from telebot import types

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