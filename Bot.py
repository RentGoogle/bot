import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Enter your bot's API token here
TOKEN = '6156324948:AAFKs74NA_QIBWMS6l4mgjNK1R0EY3zKZ3Q'

# Create a new bot instance
bot = telebot.TeleBot(TOKEN)

# Define the button and its label
button_label = 'Click me!'
button = KeyboardButton(button_label)

# Create the reply markup with the button
reply_markup = ReplyKeyboardMarkup(one_time_keyboard=True)
reply_markup.add(button)

# Define the handler for the /start command
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(chat_id=message.chat.id,
                     text='Welcome to my bot! Click the button below to continue:',
                     reply_markup=reply_markup)

# Define the handler for the button click
@bot.message_handler(func=lambda message: message.text == button_label)
def button_handler(message):
    bot.send_message(chat_id=message.chat.id,
                     text='You clicked the button!')

# Start the bot
bot.polling()
