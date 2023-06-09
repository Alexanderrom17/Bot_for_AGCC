#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item3 = types.KeyboardButton("Кнопка 1")
#     item4 = types.KeyboardButton("Кнопка 2")
#     item5 = types.KeyboardButton("Кнопка 3")
#
#     markup.add(item3, item4, item5)
#     user_name = message.from_user.first_name
#     sticker = open("Hello.tgs", 'rb')
#     bot.send_sticker(message.chat.id, sticker)
#     markup = types.InlineKeyboardMarkup(row_width=2)
#     item1 = types.InlineKeyboardButton("1251", callback_data='1251')
#     item2 = types.InlineKeyboardButton("1354", callback_data='1354')
#     markup.add(item1, item2)
#     bot.send_message(message.chat.id, f'Добро пожаловать {user_name}, Я - бот помощник АГХК \n' 'Выберите номер титула',
#                      reply_markup=markup)





# @bot.message_handler(func=lambda message: True)
# def send_file(message):
#     if message.text == '1251':
#         file_name = 'Романов Александр Юрьевич.docx'
#         with open(file_name, 'rb') as file:
#             bot.send_document(message.chat.id, file)