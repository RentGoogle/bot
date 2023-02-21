import io
import qrcode
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor

# Вказуємо токен вашого бота
TOKEN = '5640232171:AAFgCbazixwq0if2eYZM7cW9KpVTQDPYoUk'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обробка команди /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привіт! Відправ мені посилання та я створю QR-код для нього.")

# Обробка повідомлення з посиланням
@dp.message_handler(content_types=['text'])
async def process_link(message: types.Message):
    # Генеруємо QR-код з посиланням
    img = qrcode.make(message.text)
    
    # Відправляємо зображення з QR-кодом
    with io.BytesIO() as output:
        img.save(output, 'PNG')
        output.seek(0)
        await bot.send_photo(message.chat.id, output, caption='QR-код для посилання:\n{}'.format(message.text), parse_mode=ParseMode.HTML)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)