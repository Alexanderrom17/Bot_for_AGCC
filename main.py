import telebot
from telebot import types

token = "6148868274:AAGera4iHzE-P4cBIj830JbJ3Q3YRcgPnq0"
bot = telebot.TeleBot(token)


# Обработка функции Start
@bot.message_handler(commands=['start'])
def welcome(message):
    user_name = message.from_user.first_name
    sticker = open("emoji\Hi_stckr.tgs", 'rb')
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.chat.id, f'Добро пожаловать {user_name}'
                                      f', Я - бот помощник АГХК\nДля начала работы введите "Привет"')


# Обработка "Привет". Является функцией, которая запускает виртуальные кнопки 1251, 1354, 1520
@bot.message_handler(content_types=['text'])
def user_text(message):
    if message.text.lower() == 'привет':
        markup = types.InlineKeyboardMarkup(row_width=7)
        item1 = types.InlineKeyboardButton(text="Артезианский водозабор", callback_data='open_new_buttons_1520')
        item2 = types.InlineKeyboardButton(text="Насосная станция тит. 1354", callback_data='open_new_buttons_1354')
        item3 = types.InlineKeyboardButton(text="УППВ 1251", callback_data='open_new_buttons_1251')
        item4 = types.InlineKeyboardButton(text="Насосная станция тит. 1079", callback_data='open_new_buttons_1079')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(message.chat.id, f"Выбери номер титула по которому хочешь получить информацию",
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Для начала работы введи "Привет"')


# Выбор 1520 и 1503
@bot.callback_query_handler(func=lambda call: call.data == 'open_new_buttons_1520')
def handle_button_click(call):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Подстанция тит. 1520', callback_data='button1_1520_clicked')
    button2 = types.InlineKeyboardButton(text='Павильон тит. 1503', callback_data='button2_1503_clicked')
    button3 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Артезианский водозабор", reply_markup=keyboard)


# Обработка нажатия кнопки 1520
@bot.callback_query_handler(func=lambda call: call.data == 'button1_1520_clicked')
def handle_button1_click(call):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='1520 Блокировки и разрешения', callback_data='1520_P&B')
    button2 = types.InlineKeyboardButton(text='1520 Включ. насосов в руч. режиме', callback_data='start_pump_hand_mode')
    button3 = types.InlineKeyboardButton(text='1520 Включ. насосов в авто режиме', callback_data='start_pump_auto_mode')
    button4 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)


# Обработка нажатия кнопки 1520 блокировки и разрешения
@bot.callback_query_handler(func=lambda call: call.data == '1520_P&B')
def permit_block(call):
    with open('doc\Блокировки и разрешения 1520 .pdf', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Блокировки и разрешения')


# Обработка нажатия кнопки 1520 пуск насоса в ручном режиме
@bot.callback_query_handler(func=lambda call: call.data == 'start_pump_hand_mode')
def start_pump_hand(call):
    with open('doc\Включение насосов в ручном режиме 1520.pdf', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Включение насосов в ручном режиме 1520')


# Обработка нажатия кнопки 1520 пуск насоса в авто режиме
@bot.callback_query_handler(func=lambda call: call.data == 'start_pump_auto_mode')
def start_pump_hand(call):
    with open('doc\Включение насосов в автоматическом режиме 1520.pdf', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Включение насосов в авто режиме 1520')


@bot.callback_query_handler(func=lambda call: call.data == 'button2_1503_clicked')
def handle_button1_click(call):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='1503 Режим работыЧРП', callback_data='Pump_drive')
    button2 = types.InlineKeyboardButton(text='1503 Насос Lowara', callback_data='lowara_pump')
    button3 = types.InlineKeyboardButton(text='1503 Пуск насоса после аварии', callback_data='Pump_start_error')
    button4 = types.InlineKeyboardButton(text='1503 ТИ Артезианская скважина', callback_data='TI_1354')
    button5 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)
    keyboard.add(button5)


@bot.callback_query_handler(func=lambda call: call.data == 'Pump_drive')
def start_pump_hand(call):
    with open('doc\Режимы работы ЧРП 1503 .pdf.pdf', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Режим работы ЧРП')


@bot.callback_query_handler(func=lambda call: call.data == 'lowara_pump')
def start_pump_hand(call):
    with open('doc\СОП насос LOWARA артезианский водозабор (вариант 4)1503.pdf', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Насос Lowara')


@bot.callback_query_handler(func=lambda call: call.data == 'Pump_start_error')
def start_pump_hand(call):
    with open('doc\СОП насос артезианского водозабора, запуск после аварии 1503.pdf', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Пуск насоса после аварии')


@bot.callback_query_handler(func=lambda call: call.data == 'TI_1354')
def start_pump_hand(call):
    with open('doc\ТИ_Артезианская скважина (вариант 3)1503 .doc', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Инструкция артезианские скважины')


# Обработка нажатия кнопки 1354
@bot.callback_query_handler(func=lambda call: call.data == 'open_new_buttons_1354')
def handle_button_click(call):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Пуск станции в работу', callback_data='start_station')
    button2 = types.InlineKeyboardButton(text='ТИ 1354', callback_data='TI_1354')
    button3 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Перед проведением работ внимательно изучи инструкцию", reply_markup=keyboard)


# Обработка нажатия кнопки 1354 кнопка 1
@bot.callback_query_handler(func=lambda call: call.data == 'start_station')
def handle_button1_click(call):
    with open('doc\СОП запуск в работу (вариант 2.1) 1354  .pdf', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Пуск станции')


# Обработка нажатия кнопки 1354 кнопка 2
@bot.callback_query_handler(func=lambda call: call.data == 'TI_1354')
def handle_button2_click(call):
    with open('doc/ТИ насосная станция тит. 1354 (вариант 1) 1354.doc', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Технологическая инструкция')


# Обработка нажатия кнопки 1251
@bot.callback_query_handler(func=lambda call: call.data == 'open_new_buttons_1251')
def handle_button_click(call):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='1251 Пуск станции', callback_data='start_station')
    button2 = types.InlineKeyboardButton(text='Приготовление реагентов', callback_data='reagent_ready')
    button3 = types.InlineKeyboardButton(text='Промывка фильтров', callback_data='filter_washer')
    button4 = types.InlineKeyboardButton(text='ТИ станции 1251', callback_data='TI_1251')
    button5 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)
    keyboard.add(button5)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Перед проведением работ внимательно изучи инструкцию", reply_markup=keyboard)


# Обработка нажатия кнопки 1251 кнопка 1
@bot.callback_query_handler(func=lambda call: call.data == 'start_station')
def handle_button1_click(call):
    with open('doc/СОП запуска СКПВ (вариант 1а) 1251.pdf', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Пуск станции')


# Обработка нажатия кнопки 1251 кнопка 2
@bot.callback_query_handler(func=lambda call: call.data == 'reagent_ready')
def handle_button2_click(call):
    with open('doc/СОП приготовление реагентов (вариант 1.0) 1251.pdf', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Приготовление реагентов')


# Обработка нажатия кнопки 1251 кнопка 2
@bot.callback_query_handler(func=lambda call: call.data == 'filter_washer')
def handle_button2_click(call):
    with open('doc/СОП промывка фильтров (вариант 1.0) 1251.pdf', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Промывка фильтров')


# Обработка нажатия кнопки 1251 кнопка 2
@bot.callback_query_handler(func=lambda call: call.data == 'TI_1251')
def handle_button2_click(call):
    with open('doc/Технологическая инструкция_СКПВ-500 крайний 13.09.22 1251.doc', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Технологическая инструкция 1251')


#     Обработка нажатия кнопки 1079
@bot.callback_query_handler(func=lambda call: call.data == 'open_new_buttons_1079')
def handle_button_click(call):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Кнопка 1 1079', callback_data='button1_1079_clicked')
    # button2 = types.InlineKeyboardButton(text='Кнопка 2 1079', callback_data='button2_1079_clicked')
    button3 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard.add(button1)
    # keyboard.add(button2)
    keyboard.add(button3)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Перед проведением работ внимательно изучи инструкцию", reply_markup=keyboard)


# Обработка нажатия кнопки 1079 кнопка 1
@bot.callback_query_handler(func=lambda call: call.data == 'button1_1079_clicked')
def handle_button1_click(call):
    with open('doc/ТИ_водоподающей станции тит.1079 (от 04.10.22)1079.doc', 'rb') as file:
        bot.send_document(chat_id=call.message.chat.id, data=file, document=file)
    bot.answer_callback_query(call.id, text='Нажата кнопка 1')


# Обработка нажатия кнопки 1079 кнопка 2
# @bot.callback_query_handler(func=lambda call: call.data == 'button2_1079_clicked')
# def handle_button2_click(call):
#     bot.answer_callback_query(call.id, text='Нажата кнопка 2')


# Обработка нажатия кнопки Назад
@bot.callback_query_handler(func=lambda call: call.data == 'back')
def handle_button_back(call):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Артезианский водозабор', callback_data='open_new_buttons_1520')
    button2 = types.InlineKeyboardButton(text='Насосная станция тит. 1354', callback_data='open_new_buttons_1354')
    button3 = types.InlineKeyboardButton(text='УППВ 1251', callback_data='open_new_buttons_1251')
    button4 = types.InlineKeyboardButton(text='Насосная станция тит. 1079', callback_data='open_new_buttons_1079')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Выбери номер титула по которому хочешь получить информацию", reply_markup=keyboard)


bot.polling(none_stop=True)
