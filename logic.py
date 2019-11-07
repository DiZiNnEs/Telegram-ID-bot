from config import bot
from telebot import types


@bot.message_handler(commands=['start'])
def handle_start(message):
    #bot.send_message(message.chat.id, '👋Hello, ' + message.from_user.username)
    user_markup = types.ReplyKeyboardMarkup(True,True)
    user_markup.row('👤Profile', '⚙️Help')
    user_markup.row('👨‍👨‍👧‍👧Information about chat')
    user_markup.row('🚫Hide menu')
    user_markup.row('🛠 Bot Information')
    bot.send_message(message.from_user.id, '👋Hello, ' + message.from_user.username, reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    #Handler for profile
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

    # Handler for help
    elif message.text == '⚙️Help':
        bot.send_message(message.chat.id, f'''
⚙️Help
💾In this section, all the commands with which you can control the bot will be presented:

/start - Main menu
/help - Help
/me - Profile
/chat_info - Information about chat
        ''')
    # Handler for information about chat
    elif message.text == '👨‍👨‍👧‍👧Information about chat':
        bot.send_message(message.chat.id, f'''
👨‍👨‍👧‍👧Information about chat:

id chat: {message.chat.id}
Chat type: {message.chat.type}
        ''')
    # Handler for bot information
    elif message.text == '🛠 Bot Information':
        bot.send_message(message.chat.id, f'''
The bot is designed for people and other developers.
Please do not scold!
Developer of this bot: @dizzinnes
GitHub: https://github.com/DiZiNnEs
''')
    # Handler for hide menu
    elif message.text == '🚫Hide menu':
        bot.send_message(message.chat.id, f'''
The menu is hidden so that the menu appears again write /start
        ''')
    # Handler for /help command
    elif message.text == '/help':
        bot.send_message(message.chat.id, f'''
⚙️ Help

📍 In this section, all the commands with which you can control the bot will be presented.

/start - Main menu
/help - Help
/me - Profile
/chat_info - Chat information
''')
    # Handler for /me command
    elif message.text == '/me':
        bot.send_message(message.chat.id, f'''\
        👤 Profile:

Your ID: {message.chat.id}
This is a bot: {message.from_user.is_bot} 
Name: {message.from_user.first_name}
Surname: {message.from_user.last_name}
Username : @{message.from_user.username}
Country code: {message.from_user.language_code}
                ''')
    # Handler for /chat_info command
    elif message.text == '/chat_info':
        bot.send_message(message.chat.id, f'''
  👨‍👨‍👧‍👧Information about chat:

id chat: {message.chat.id}
Chat type: {message.chat.type}
                ''')
    else:
        bot.send_message(message.chat.id, "Sorry, i don't understand you! Write /help ")

@bot.message_handler(content_types=['sticker'])
def handler_sticker(message):
    bot.send_message(message.chat.id, 'Sticker ID: ' + message.sticker.file_id)


bot.polling(interval=0, none_stop=())