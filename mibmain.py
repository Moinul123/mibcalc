import telebot
from telebot import types

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('7150044305:AAHwaCBBP798BwlEMoyZiXHKc0r6SqZLgqU')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f"Hello {user_name}! Welcome to the MIB calculator bot. Send your calculation question and get answer")

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        result = eval(message.text)
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text=str(result), callback_data=result))
        bot.reply_to(message, f"{message.text} = {result}", reply_markup=markup)
    except:
        bot.reply_to(message, "Sorry, I couldn't understand the calculation.")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    bot.send_message(call.message.chat.id, call.data)

bot.polling()
