import telebot
import logging
import logs
import configs
import keyboards
import databases
from telebot import apihelper

apihelper.proxy = {configs.PROTOCOL : configs.ADDRESS}

bot = telebot.TeleBot(configs.TOKEN)

logs.log_init()

@bot.message_handler(commands=['start'])
def text(message):
    user_first_name = message.from_user.first_name
    bot.send_message(chat_id=message.chat.id,
                     text=f'Hello {user_first_name}!!!!', reply_markup=keyboards.main_menu())
    logging.info("Succses")


@bot.message_handler(content_types=["text"])
def new_pers_func(message):
    if message.text == "Создать персонажа":
        bot.send_message(chat_id=message.chat.id,
                         text='Выберите класс', reply_markup=keyboards.class_review_keyboard())
    elif message.text == "Мои персонажи":
        bot.send_message(chat_id=message.chat.id,
                         text='Иди-ка пока нахуй', reply_markup=keyboards.back_keyboard())
    elif message.text == "Открыть Wiki":
        bot.send_message(chat_id=message.chat.id,
                         reply_markup=keyboards.back_keyboard())


@bot.callback_query_handler()
def back_btn(call):
    callback_info = call.data
    if "class" in callback_info:
        call_split = callback_info.split("_")
        class_id = int(call_split[1])
#       recommend_stats, spells, class_name, class_description, class_skills, hp_dice = databases.get_class_info(class_id)
        _, _, class_name, _, _, _ = databases.get_class_info(
            class_id)
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Вы выбрали класс {class_name}. Вывести информацию о нем?",
                         reply_markup=keyboards.class_info_keyboard())
    elif 'Test' in callback_info:
        bot.send_message(chat_id=call.message.chat.id,
                         text="Бро, пока не работает, не обесуть. Глянь вниз и выбри что ты хочешь")


@bot.message_handler(content_types=['sticker'])
def text(message):
    print(message)
    bot.send_message(chat_id=message.chat.id,
                     text='О, Это стикер, Скебоб')

bot.polling()
# TODO: Разобраться, как работает стандратная библеотека Logging, прописать логи разных уровней. (ВЫПОЛНЕННО)
'''
- Создать файл logs.py
- В нем создать функцию инициализатора лога
- В ней настроить лог
- В main.py вызвать функцию настройки
- Я великолепен 
'''

# TODO: Переименовать модули согласно, PEP8 (ВЫПОЛНЕННО)
# TODO: Дозаполнить базу данных (ВЫПОЛНЕННО)
# TODO: В разделе создать персонажа выполнить следующий скрипт !!!! (ВЫПОЛНЕННО)
"""
- Подключиться к БД
- Из таблицы достать все классы
- Сделать массив со всеми классам4
- Передать массив в клавиатуру и сдедать по кнопке с каждым классом
- Вывести nline клаввиатуру, где каждая кнопка имя класса, а collback формате class_42
- В декоратаре обработки callbackов
"""
# TODO: прочитатиь по ссылке ниже
"""
https://ru.wikipedia.org/wiki/%D0%9D%D1%83%D0%BC%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B9_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F
"""
# TODO: Создать отдельные переменные для рызных имен БД, явно указывать какую бд мы вызываем (ВЫПОЛНЕННО)
# TODO: configparser (заебать Кирилла). Изучить для хранения чувствительных данных, перенести все в config.ini (ВЫПОЛНЕННО)
# TODO: Дописать обработку callback, используя id класса обратится к бд и получить имя, написать пользователю какой класс он выбрал (ВЫПОЛНЕННО)