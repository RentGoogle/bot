from telebot import types
import telebot
from telebot.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup


# створення бота з токеном
bot = telebot.TeleBot('5554002160:AAFHjdJVHqBKniUToLzWA8RuhWXxv8n_Dww')


@bot.message_handler(commands=['start'])
def send_welcome(message):
  name = message.from_user.first_name
  # створення inline-клавіатури
  keyboard = types.InlineKeyboardMarkup(row_width=2)
  text = f"Щире вітання, {name}! \nБот наразі знаходиться в розробці v0.0.9\nЗгодом в боті з'являться нові функції\n\nА поки що ось які функції є:\n\nЩоб залишити заявку на перевірку Google акаунта, перейдіть на наш веб-сайт ⬇️"
  # створення кнопок і додавання їх до клавіатури
  button1 = types.InlineKeyboardButton(
    text="Веб-сайт",
    web_app=WebAppInfo('https://rentgoogle.github.io/rent-google1/'))
  button2 = types.InlineKeyboardButton(text="Контакти менеджера",
                                       callback_data='button2')
  button4 = types.InlineKeyboardButton(text="Умови до Google",
                                       callback_data='button4')
  button3 = types.InlineKeyboardButton(text="Доступні команди",
                                       callback_data='button3')
  keyboard.add(button1)
  keyboard.add(button2, button4)
  keyboard.add(button3)

  # відправлення повідомлення з клавіатурою")
  bot.send_message(message.chat.id, "👋")
  bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def send_welcome(message):
  markup = types.InlineKeyboardMarkup()
  markup.add(
    types.InlineKeyboardButton(
      "Наш Instagram",
      url=('https://instagram.com/orenda_gmail_fb?igshid=YmMyMTA2M2Y=')))
  bot.send_message(
    message.chat.id,
    "Бот наразі знаходиться в розробці v0.0.9 \nДоступні команди: \n\n/start - початок роботи з ботом; \n/info - Дізнатися Умови/Оплату за Google акаунт \n/help - довідка про доступні команди;\n\n/google - Здати Google акаунт на перевірку \n/facebook - Здати Facebook акаунт на перевірку\n\n",
    reply_markup=markup)


@bot.message_handler(commands=['google'])
def send_welcome(message):
  markup = types.InlineKeyboardMarkup()
  markup.add(
    types.InlineKeyboardButton(
      "Веб-сайт",
      web_app=WebAppInfo('https://rentgoogle.github.io/rent-google1/')))
  bot.send_message(
    message.chat.id,
    "Веб-сайт: Щоб залишити заявку на перевірку Google акаунта\n\nНатисніть кнопку нижче ⬇️",
    reply_markup=markup)


@bot.message_handler(commands=['info'])
def send_welcome(message):
  markup = types.InlineKeyboardMarkup()
  markup.add(
    types.InlineKeyboardButton(
      "Веб-сайт",
      web_app=WebAppInfo('https://rentgoogle.github.io/rent-google1/')))
  bot.send_message(
    message.chat.id,
    "Дізнатися про Умови та Оплату Google акаунта, можете переглянути на нашому Веб-сайті",
    reply_markup=markup)


@bot.message_handler(commands=['facebook'])
def send_welcome(message):
  markup = types.InlineKeyboardMarkup()
  markup.add(
    types.InlineKeyboardButton(
      "Веб-сайт Facebook",
      web_app=WebAppInfo('https://rentgoogle.github.io/facebook/')))
  bot.send_message(
    message.chat.id,
    "Веб-сайт: Щоб залишити заявку на перевірку Facebook акаунта\n\nНатисніть кнопку нижче ⬇️",
    reply_markup=markup)


@bot.message_handler(commands=['instagram'])
def send_welcome(message):
  markup = types.InlineKeyboardMarkup()
  markup.add(
    types.InlineKeyboardButton("Наш Instagram",
                               url=('https://bit.ly/3xYNWFM/')))
  bot.send_message(message.chat.id,
                   "Наш Instagram - https://bit.ly/3xYNWFM",
                   reply_markup=markup)




@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  if call.data == 'button1':
    bot.send_message(call.message.chat.id, 'Вы нажали на кнопку 1')

  if call.data == 'button4':
    markup = types.InlineKeyboardMarkup()
    markup.add(
    types.InlineKeyboardButton("Веб-сайт",  web_app=WebAppInfo('https://rentgoogle.github.io/rent-google1/')))
    bot.send_message(call.message.chat.id, '«Умови до Google»\n\n✅ Вашому Gmail понад 6 місяців (власнику сторінки вже є 18).\n\n✅ Раніше не здавалася в оренду, жодного разу, нікому.\n\n✅ Є понад 500 листів (спам, розсилка, відповіді від онлайн магазинів та сервісів, або будь-які інші).\n\n✅ Активне користування YouTube.\n\nЩоб залишити заявку на перевірку Google акаунта\n\nНатисніть кнопку нижче ⬇️',  reply_markup=markup)

  if call.data == 'button2':
    bot.send_message(call.message.chat.id,
                     'Telegram: @Max_Rent \n\nViber: +380688430553')
  if call.data == 'button3':
    markup = types.InlineKeyboardMarkup()
    markup.add(
      types.InlineKeyboardButton(
        "Наш Instagram",
        url=('https://instagram.com/orenda_gmail_fb?igshid=YmMyMTA2M2Y=')))
    bot.send_message(
      call.message.chat.id,
      'Бот наразі знаходиться в розробці v0.0.9 \nДоступні команди: \n\n/start - початок роботи з ботом; \n/info - Дізнатися Умови/Оплату за Google акаунт \n/help - довідка про доступні команди;\n\n/google - Здати Google акаунт на перевірку \n/facebook - Здати Facebook акаунт на перевірку',
      reply_markup=markup)


# Обробник некомандного повідомлення
@bot.message_handler(func=lambda message: True)
def handle_message(message):
  # Відправлення повідомлення про помилку
  bot.send_message(message.chat.id, 'Це не команда. Використайте /start')


# запуск бо

bot.polling()
