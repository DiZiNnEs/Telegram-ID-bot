from config import bot

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types

@bot.message_handler(commands=['start'])
def handle_start(message):
    #bot.send_message(message.chat.id, '👋Hello, ' + message.from_user.username)
    user_markup = types.ReplyKeyboardMarkup(True,True)
    user_markup.row('👤Profile', '⚙️Help')
    user_markup.row('👨‍👨‍👧‍👧Information about chat')
    user_markup.row('🚫Hide menu')
    bot.send_message(message.from_user.id, '👋Hello, ' + message.from_user.username, reply_markup=user_markup)


# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup()
#     profile = types.KeyboardButton(text='👤Information about your profile')
#     help = types.KeyboardButton(text='Help')
#     markup.add(profile, help)
#     msg = bot.send_message(message.chat.id, 'The bot started successfully', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text == '👤Profile':
        #bot.send_message(message.chat.id, 'Your profile ID: ' + str(message.chat.id),)
        bot.send_message(message.chat.id, f'''\
👤 Profile:

Your ID: {message.chat.id}
This is a bot: {message.from_user.is_bot} 
Name: {message.from_user.first_name}
Surname: {message.from_user.last_name}
Username : @{message.from_user.username}
Country code: {message.from_user.language_code}
        ''')
    elif message.text == '⚙️Help':
        bot.send_message(message.chat.id, f'''
⚙️Help
💾In this section, all the commands with which you can control the bot will be presented:

/start - Main menu
/help - Help
/me - Profile
/chat_info - Information about chat
        ''')
    elif message.text == '👨‍👨‍👧‍👧Information about chat':
        bot.send_message(message.chat.id, f'''
👨‍👨‍👧‍👧Information about chat:

id chat: {message.chat.id}
Chat type: {message.chat.type}
        ''')
    elif message.text == '🚫Hide menu':
        pass
    #else:
        #bot.send_message(message.chat.id, "Sorry, i don't understand you! Write /help ") # Выводит лишь ошибку

@bot.message_handler(commands=['help'])
def handler_help(message):
    bot.send_message(message.chat.id, f'''
📍 В этом разделе будут представленны все команды, с помощью которых вы сможете управлять ботом.

/start - Главное меню
/help - Помощь
/me - Профиль
/chat_info - Информация о чате
    ''')

@bot.message_handler(commands=['me'])
def handler_me(message):
    bot.send_message(message.chat.id, f'''
   Profile:

Your ID: {message.chat.id}
This is a bot: {message.from_user.is_bot} 
Name: {message.from_user.first_name}
Surname: {message.from_user.last_name}
Username : @{message.from_user.username}
Country code: {message.from_user.language_code} 
    ''')
# @bot.message_handler(commands=['my_id'])
# def my_id(message):
#     bot.send_message(message.chat.id, 'Your ID in telegram: ' + str(message.chat.id))
#
#
# @bot.message_handler(content_types=['sticker'])
# def sticker(message):
#     bot.send_message(message.chat.id, 'Sticker ID: ' + str(message.sticker.file_id))


bot.polling(interval=0, none_stop=())