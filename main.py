import telebot
from telebot import types

token = "6148868274:AAGera4iHzE-P4cBIj830JbJ3Q3YRcgPnq0"
bot = telebot.TeleBot(token)


@bot.message_handler(['start'])
def welcome(message):
    user_name = message.from_user.first_name
    sticker = open("Hello.tgs", 'rb')
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.chat.id, f'Добро пожаловать {user_name}'
                                      f', Я - бот помощник АГХК\nДля начала работы введите "Привет"')


@bot.message_handler(content_types=['text'])
def user_text(message):
    if message.text.lower() == 'привет':
        markup = types.InlineKeyboardMarkup(row_width=2,)
        item1 = types.InlineKeyboardButton(text="1251", callback_data='1251')
        item2 = types.InlineKeyboardButton(text="1354", callback_data='1354')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, f"Введи номер титула по которому хочешь получить СОП", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Для начала работы введи "Привет"')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == '1251':
            with open('Instruction.txt', 'rb') as file:
                bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
                # bot.send_message(call.message.chat.id, 'Здесь будет инструкция')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Перед проведением работ внимательно изучи инструкцию", reply_markup=None)
        elif call.data == '1354':
            with open('Копия Проверка знаний ТЭСС.xlsx', 'rb') as file:
                bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
                # bot.send_message(call.message.chat.id, 'Бывает')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Перед проведением работ внимательно изучи инструкцию", reply_markup=None)


bot.polling(none_stop=True)
