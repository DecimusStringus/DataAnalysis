import telebot

# connect to the telegram bot
t_file = open(r'C:\Users\48885\Documents\Python Knowledge\ThiBaut_t.txt')
token_id = t_file.read()
t_file.close()
bot = telebot.TeleBot(token_id)
# Add start command /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

bot.polling(none_stop=True, interval=0)

# @bot.message_handler(content_types=['text'])
# #@bot.message_handler(content_types=['text', 'document', 'audio'])
# def get_text_messages(message):
#
#     if message.text == "Привет":
#         return bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         return bot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         return bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")