import time

import telebot
import logging

import logs
import configs
import keyboards
import databases
from telebot import apihelper


logs.log_init()

apihelper.proxy = {configs.PROTOCOL : configs.ADDRESS} # инициализация прокси

bot = telebot.TeleBot(configs.TOKEN)

def choise_class(chat_id: int):
    """
    Функция для вывода клавиатуры для выбора класса
    :param chat_id: id чата в который надо отправить клавиатуру
    :return: процедура
    """
    bot.send_message(chat_id=chat_id,
                     text='Выберите класс',
                     reply_markup=keyboards.class_review_keyboard())


def choise_race(chat_id: int):
    """
    Функция для вывода клавиатуры для выбора расы
    :param chat_id: id чата в который надо отправить клавиатуру
    :return: процедура
    """
    bot.send_message(chat_id=chat_id,
                     text='Выберите рассу',
                     reply_markup=keyboards.race_review_keyboard())


def choise_background(chat_id: int):
    """
    Функция для вывода клавиатуры для выбора предыстории
    :param chat_id: id чата в который надо отправить клавиатуру
    :return: процедура
    """
    bot.send_message(chat_id=chat_id,
                     text='Выберите предысторию',
                     reply_markup=keyboards.background_review_keyboard())

@bot.message_handler(commands=['start'])
def text(message):
    user_first_name = message.from_user.first_name
    bot.send_message(chat_id=message.chat.id,
                     text=f'Hello {user_first_name}!!!!', reply_markup=keyboards.main_menu())
    logging.info("Succses")


@bot.message_handler(content_types=["text"])
def new_pers_func(message: tuple):
    """
    Функция для обработки текстового ввода пользователя
    :param message: картеж передающийся при обработке сообщения и содержащий информацию о сообщении
    :return: процедура
    """
    if message.text == "Создать персонажа":
        choise_class(message.chat.id)
    elif message.text == "Мои персонажи":
        bot.send_message(chat_id=message.chat.id,
                         text='Иди-ка пока нахуй', reply_markup=keyboards.back_keyboard())
    elif message.text == "Открыть Wiki":
        bot.send_message(chat_id=message.chat.id,
                         reply_markup=keyboards.back_keyboard())


@bot.callback_query_handler()
def call_info(call: tuple):
    """
    Функция обработки коллбеков
    :param call: картеж передающийся при обработке callback и содержащий информацию о callback
    :return: процедура
    """
    callback_info = call.data
    chat_id = call.message.chat.id
    logging.debug(f"callback_info: {callback_info}")

    if "choise" in callback_info:
        if "choise_class" == callback_info:
            choise_class(chat_id)
        elif "choise_race" == callback_info:
            choise_race(chat_id)
        elif "choise_background" == callback_info:
            choise_background(chat_id)

        elif "choise_class" in callback_info:
            if "choise_class_confirm" in callback_info:
                call_split = callback_info.split("_")
                class_id_temp = int(call_split[-1])      # Временная переменная испольpycзующаяся для хранения id класса до его подтверждения
                logging.debug(f"В переменную class_id_temp записано значение {class_id_temp}")
        #        recommend_stats, spells, class_name, class_description, class_skills, hp_dice = databases.get_class_info(class_id)
                _, _, class_name, _, _, _ = databases.get_class_info(class_id_temp)
                bot.send_photo(chat_id=call.message.chat.id,
                               photo=open(f'media/сlass_media/pers_img{class_id_temp}.jpg', 'rb'),
                               caption=f"Вы выбрали класс {class_name}. Подтверждаете свой выбор?",
                               reply_markup=keyboards.class_choise_keyboard(class_id_temp))
        elif "choise_race" in callback_info:
            if "choise_race_confirm" in callback_info:
                call_split = callback_info.split("_")
                race_id = int(call_split[-1])
                logging.debug(f"В переменную race_id записано значение {race_id}")
                _, _, _, race_name = databases.get_race_info(race_id)
                bot.send_message(chat_id=call.message.chat.id,
                                 text=f"Вы выбрали расу {race_name}. Подтверждаете свой выбор?",
                                 reply_markup=keyboards.race_choise_keyboard(race_id))
        elif "choise_background" in callback_info:
            if "choise_background_confirm" in callback_info:
                call_split = callback_info.split("_")
                background_id = int(call_split[-1])
                logging.debug(f"В переменную background_id записано значение {background_id}")
                background_name, _, _, _ = databases.get_background_info(background_id)
                bot.send_message(chat_id=call.message.chat.id,
                                 text=f"Вы выбрали предысторию {background_name}. Подтверждаете свой выбор?",
                                 reply_markup=keyboards.background_choise_keyboard(background_id))

    elif "confirm" in callback_info:
        if "confirm_class_info" in callback_info:
            call_split = callback_info.split("_")
            class_id_temp = int(call_split[-1])  # Временная переменная использующаяся для хранения id класса до его подтверждения
            recommend_stats, spells, class_name, class_description, class_skills, hp_dice = databases.get_class_info(class_id_temp)
            info_class = bot.send_message(chat_id=chat_id,
                            text=f"Информация о классе {class_name}\n"
                            f"Ключевая характеристика: {recommend_stats}\n"
                            f"Описание класса: {class_description}")
            time.sleep(15)
            bot.delete_message(chat_id=chat_id,
                                message_id=info_class.message_id)
        elif "confirm_race_info" == callback_info:
            pass

bot.polling()

# TODO: Реализовать пункт 6.5 
# TODO: Во всем проекте должна быть написана документация, докстринги, аннотация и типизация
# TODO: Провести рефакторинг кода (Перенести все изменяемые данные в конфиг)
# TODO: Додавить в таблицу предысторий подходящие ID класса
# TODO: Добавить картинку класса паладина (ВЫПОЛНЕННО)
# TODO: отсавить одну инициализацию логов в мейн (ВЫПОЛНЕННО)
# TODO: Закончить с выбором аспектов классов
# TODO: Поменять пароль у бд (ВЫПОЛНЕННО)
# TODO: Перенести чувствительнные данные в перемененные окружения (ВЫПОЛНЕННО)
# TODO: В бд поменять id не с нуля, а с единицы (ВЫПОЛНЕННО)
# TODO: В папке медиа создать подпапки (ВЫПОЛНЕННО)
# TODO: Моя приехзать из убекситан, моя плохо понимать русский язык, но моя стараться и првоерить все на орфографию