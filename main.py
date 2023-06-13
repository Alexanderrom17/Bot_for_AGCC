import telebot
from telebot import types

<<<<<<< HEAD
=======

>>>>>>> 5292486 (Сделал 1520)
token = "6148868274:AAGera4iHzE-P4cBIj830JbJ3Q3YRcgPnq0"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def welcome(message):
    user_name = message.from_user.first_name
<<<<<<< HEAD
    sticker = open("Hello.tgs", 'rb')
=======
    sticker = open("emoji\Hi_stckr.tgs", 'rb')
>>>>>>> 5292486 (Сделал 1520)
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.chat.id, f'Добро пожаловать {user_name}'
                                      f', Я - бот помощник АГХК\nДля начала работы введите "Привет"')


@bot.message_handler(content_types=['text'])
def user_text(message):
    if message.text.lower() == 'привет':
        markup = types.InlineKeyboardMarkup(row_width=7)
        item1 = types.InlineKeyboardButton(text="1520", callback_data='open_new_buttons_1520')
        item2 = types.InlineKeyboardButton(text="1354", callback_data='open_new_buttons_1354')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, f"Введи номер титула по которому хочешь получить инструкцию",
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Для начала работы введи "Привет"')


@bot.callback_query_handler(func=lambda call: call.data == 'open_new_buttons_1520')
def handle_button_click(call):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Включение насосов в ручном режиме', callback_data='button1_1520_clicked')
    button2 = types.InlineKeyboardButton(text='Кнопка 2 1520', callback_data='button2_1520_clicked')
    button3 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Перед проведением работ внимательно изучи инструкцию", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'button1_1520_clicked')
def handle_button1_click(call):
    bot.answer_callback_query(call.id, text='Вы выбрали артезианский водозабор')
    with open('doc\Включение насосов в ручном режиме.pdf', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    # with open('doc\Instruction.txt', 'rb') as file:
    #     bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Для начала работы введите Привет', reply_markup=None)


@bot.callback_query_handler(func=lambda call: call.data == 'button2_1520_clicked')
def handle_button2_click(call):
    bot.answer_callback_query(call.id, text='Нажата кнопка 2')


@bot.callback_query_handler(func=lambda call: call.data == 'open_new_buttons_1354')
def handle_button_click(call):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Кнопка 1 1354', callback_data='button1_1354_clicked')
    button2 = types.InlineKeyboardButton(text='Кнопка 2 1354', callback_data='button2_1354_clicked')
    button3 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Перед проведением работ внимательно изучи инструкцию", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'button1_1354_clicked')
def handle_button1_click(call):
    bot.answer_callback_query(call.id, text='Нажата кнопка 1')


@bot.callback_query_handler(func=lambda call: call.data == 'button2_1354_clicked')
def handle_button2_click(call):
    bot.answer_callback_query(call.id, text='Нажата кнопка 2')


@bot.callback_query_handler(func=lambda call: call.data == 'back')
def handle_button_back(call):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='1520', callback_data='open_new_buttons_1520')
    button2 = types.InlineKeyboardButton(text='1354', callback_data='open_new_buttons_1354')
    keyboard.add(button1, button2)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Перед проведением работ внимательно изучи инструкцию", reply_markup=keyboard)


# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     if call.message:
#         if call.data == '1251':
#             with open('Instruction.txt', 'rb') as file:
#                 bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
#                 bot.send_message(call.message.chat.id, 'Здесь будет инструкция')
<<<<<<< HEAD
                # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                #                       text="Перед проведением работ внимательно изучи инструкцию", reply_markup=None)
        # elif call.data == '1354':
        #     with open('Копия Проверка знаний ТЭСС.xlsx', 'rb') as file:
        #         bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
        #         bot.send_message(call.message.chat.id, 'Бывает')
                # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                #                       text="Перед проведением работ внимательно изучи инструкцию", reply_markup=None)
=======
# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                       text="Перед проведением работ внимательно изучи инструкцию", reply_markup=None)
# elif call.data == '1354':
#     with open('Копия Проверка знаний ТЭСС.xlsx', 'rb') as file:
#         bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
#         bot.send_message(call.message.chat.id, 'Бывает')
# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                       text="Перед проведением работ внимательно изучи инструкцию", reply_markup=None)
>>>>>>> 5292486 (Сделал 1520)
#


bot.polling(none_stop=True)
