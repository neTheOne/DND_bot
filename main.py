import telebot
import logging
import logs
import configs
import keyboards
import databases
from telebot import apihelper


logs.log_init()

apihelper.proxy = {configs.PROTOCOL : configs.ADDRESS}

bot = telebot.TeleBot(configs.TOKEN)

def choise_class(message):
    bot.send_message(chat_id=message.chat.id,
                     text='Выберите класс',
                     reply_markup=keyboards.class_review_keyboard())

@bot.message_handler(commands=['start'])
def text(message):
    user_first_name = message.from_user.first_name
    bot.send_message(chat_id=message.chat.id,
                     text=f'Hello {user_first_name}!!!!', reply_markup=keyboards.main_menu())
    logging.info("Succses")


@bot.message_handler(content_types=["text"])
def new_pers_func(message):
    if message.text == "Создать персонажа":
        choise_class(message)
    elif message.text == "Мои персонажи":
        bot.send_message(chat_id=message.chat.id,
                         text='Иди-ка пока нахуй', reply_markup=keyboards.back_keyboard())
    elif message.text == "Открыть Wiki":
        bot.send_message(chat_id=message.chat.id,
                         reply_markup=keyboards.back_keyboard())


@bot.callback_query_handler()
def call_info(call):
    callback_info = call.data
    if "choise_class_yes" == callback_info:
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Выберите расу",
                         reply_markup=keyboards.race_review_keyboard())
    if "class" in callback_info:
        call_split = callback_info.split("_")
        class_id = int(call_split[1])
#        recommend_stats, spells, class_name, class_description, class_skills, hp_dice = databases.get_class_info(class_id)
        _, _, class_name, _, _, _ = databases.get_class_info(class_id)
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Вы выбрали класс {class_name}. Подтверждаете свой выбор?",
                         reply_markup=keyboards.class_choise_keyboard())
    elif 'Test' in callback_info:
        bot.send_message(chat_id=call.message.chat.id,
                         text="Бро, пока не работает, не обесуть. Глянь вниз и выбри что ты хочешь")


@bot.message_handler(content_types=['sticker'])
def text(message):
    print(message)
    bot.send_message(chat_id=message.chat.id,
                     text='О, Это стикер, Скебоб')

bot.polling()

# TODO: Создать директорию для хранения тестовых данных (Выполенно)
# TODO: Имена переменных бд в конфиге конченные. (Выполенно)
# TODO: Добавить подтверждение выбора класса
"""
1. В подвтерждение доабвить кнопку с выводом информации о классе
2. Если пользователь подтверждает, переходить к выбору расы 
3. Если пользователь откзаался, показывать список классов
"""
# TODO: В подвтерждение доабвить кнопку с выводом информации о классе, без клавиатуры
# TODO: Добавить логику выбора расы (аналогично классу)
# TODO: Прочитать как удалять сообщения и удалить сообщения с информацией через 10 секунд