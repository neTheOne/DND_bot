import time

import telebot
import logging

from pyexpat.errors import messages

import logs
import configs
import keyboards
import databases
from telebot import apihelper


logs.log_init()

apihelper.proxy = {configs.PROTOCOL : configs.ADDRESS}

bot = telebot.TeleBot(configs.TOKEN)

def choise_class(chat_id):
    bot.send_message(chat_id=chat_id,
                     text='Выберите класс',
                     reply_markup=keyboards.class_review_keyboard())


def choise_race(chat_id):
    bot.send_message(chat_id=chat_id,
                     text='Выберите рассу',
                     reply_markup=keyboards.race_review_keyboard())

@bot.message_handler(commands=['start'])
def text(message):
    user_first_name = message.from_user.first_name
    bot.send_message(chat_id=message.chat.id,
                     text=f'Hello {user_first_name}!!!!', reply_markup=keyboards.main_menu())
    logging.info("Succses")


@bot.message_handler(content_types=["text"])
def new_pers_func(message):
    if message.text == "Создать персонажа":
        choise_class(message.chat.id)
    elif message.text == "Мои персонажи":
        bot.send_message(chat_id=message.chat.id,
                         text='Иди-ка пока нахуй', reply_markup=keyboards.back_keyboard())
    elif message.text == "Открыть Wiki":
        bot.send_message(chat_id=message.chat.id,
                         reply_markup=keyboards.back_keyboard())
    elif "Инфорамация о классе" in message.text:
        time.sleep(10)
        bot.delete_message(chat_id=message.chat.id,
                           message_id=message.message_id)


@bot.callback_query_handler()
def call_info(call):
    callback_info = call.data
    chat_id = call.message.chat.id
     # Временная переменная использующаяся для хранения id класса до его подтверждения
    logging.debug(f"callback_info: {callback_info}")
    if "choise" in callback_info:
        if "choise_class" in callback_info:
            if "choise_class_confirm" in callback_info:
                call_split = callback_info.split("_")
                class_id_temp = int(call_split[-1])      # Временная переменная использующаяся для хранения id класса до его подтверждения
                logging.debug(f"В переменную class_id_temp записано значение {class_id_temp}")
        #        recommend_stats, spells, class_name, class_description, class_skills, hp_dice = databases.get_class_info(class_id)
                _, _, class_name, _, _, _ = databases.get_class_info(class_id_temp)
                bot.send_message(chat_id=call.message.chat.id,
                                 text=f"Вы выбрали класс {class_name}. Подтверждаете свой выбор?",
                                 reply_markup=keyboards.class_choise_keyboard(class_id_temp))
            elif "choise_class_review" in callback_info:
                choise_class(chat_id)
        elif "choise_race" in callback_info:
            if "choise_race_confirm" in callback_info:
                call_split = callback_info.split("_")
                race_id = int(call_split[-1])
                _, _, _, race_name = databases.get_race_info(race_id)
                bot.send_message(chat_id=call.message.chat.id,
                                 text=f"Вы выбрали расу {race_name}. Подтверждаете свой выбор?",
                                 reply_markup=keyboards.race_choise_keyboard(race_id))
    elif "confirm" in callback_info:
        if "confirm_class" in callback_info:
            if "confirm_class_yes" == callback_info:
                choise_race(chat_id)
            elif "confirm_class_no" == callback_info:
                choise_class(chat_id)
            elif "confirm_class_info" in callback_info:
                call_split = callback_info.split("_")
                class_id_temp = int(call_split[-1])  # Временная переменная использующаяся для хранения id класса до его подтверждения
                recommend_stats, spells, class_name, class_description, class_skills, hp_dice = databases.get_class_info(class_id_temp)
                info_class = bot.send_message(chat_id=chat_id,
                                 text=f"Инфорамация о классе {class_name}\n"
                                 "Тут будет информация о классах")
                time.sleep(2)
                bot.delete_message(chat_id=chat_id,
                                   message_id=info_class.message_id)

        elif "confirm_race" in callback_info:
            if "confirm_race_yes" == callback_info:
                pass
            elif "confirm_race_no" == callback_info:
                choise_race(chat_id)
            elif "confirm_race_info" == callback_info:
                pass


@bot.message_handler(content_types=['sticker'])
def text(message):
    print(message)
    bot.send_message(chat_id=message.chat.id,
                     text='О, Это стикер, Скебоб')

bot.polling()

# TODO: Создать директорию для хранения тестовых данных (Выполенно)
# TODO: Имена переменных бд в конфиге конченные. (Выполенно)
# TODO: Добавить подтверждение выбора класса (Выполенно)
"""
1. В подвтерждение доабвить кнопку с выводом информации о классе
2. Если пользователь подтверждает, переходить к выбору расы 
3. Если пользователь откзаался, показывать список классов
"""
# TODO: В подвтерждение доабвить кнопку с выводом информации о классе, без клавиатуры (Выполенно)
# TODO: Добавить логику выбора расы (аналогично классу) (Выполенно)
# TODO: Прочитать как удалять сообщения и удалить сообщения с информацией через 10 секунд (Выполенно)