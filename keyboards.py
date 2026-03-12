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
    wiki = types.KeyboardButton(text="Открыть Wiki")
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

def wiki_button():
    '''
    Функция для вывода кнопок меню wiki
    :return: кнопки
    '''
    keyboard = types.InlineKeyboardMarkup()
    class_wiki_button = types.InlineKeyboardButton(text="Инфорамция о классах",
                                                     callback_data='class_wiki')
    keyboard.add(class_wiki_button)