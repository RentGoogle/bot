
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = '5554002160:AAGx3jDKh5XG8agHiZdYoJ355Y90WM54zkA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

async def button1_handler(query: types.CallbackQuery):
    await query.answer()
    await query.message.answer("Сайт для здачи Google акаунта на перевірку \n- https://rentgoogle.github.io/rent-google/ -")

async def button2_handler(query: types.CallbackQuery):
    await query.answer()
    await query.message.answer("Telegram: @Max_Rent \nViber: +380688430553")

async def button3_handler(query: types.CallbackQuery):
    await query.answer()
    await query.message.answer("https://instagram.com/orenda_gmail_fb?igshid=YmMyMTA2M2Y=")
    
markup = types.InlineKeyboardMarkup()
markup.row(
    types.InlineKeyboardButton("Сайт", url="https://rentgoogle.github.io/rent-google/", callback_data="button1"),
    types.InlineKeyboardButton("Контакти менеджера", callback_data="button2"),
    types.InlineKeyboardButton("", callback_data="button3"),
)

@dp.message_handler(commands=['instagram'])
async def send_help(message: types.Message):
    help_text = "Instagram - https://instagram.com/orenda_gmail_fb?igshid=YmMyMTA2M2Y="
    await message.reply(help_text, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['site'])
async def send_help(message: types.Message):
    help_text = "Сайт для здачи Google акаунта на перевірку \n- https://rentgoogle.github.io/rent-google/ -"
    await message.reply(help_text, parse_mode=ParseMode.MARKDOWN)


# команда /help
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    help_text = "Це тестовий бот. Доступні команди: \n/start - початок роботи з ботом; \n/site - Сайт для здачі Google акаунт на перевірку: \n/instagram - Наш Instagram: \n/help - довідка про доступні команди;"
    await message.reply(help_text, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Щиро вітаю! Наразі бот працює в обмеженому функціоналі. Щоб передати свій Google акаунт на перевірку, перейдіть на наш веб-сайт ⬇️", reply_markup=markup)

@dp.message_handler()
async def text_handler(message: types.Message):
  await message.reply('Це не є командою /start')

@dp.callback_query_handler(text="button1")
async def button1(query: types.CallbackQuery):
    await button1_handler(query)

@dp.callback_query_handler(text="button2")
async def button2(query: types.CallbackQuery):
    await button2_handler(query)

@dp.callback_query_handler(text="button3")
async def button3(query: types.CallbackQuery):
    await button3_handler(query)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
