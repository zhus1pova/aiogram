from main import bot, dp

from aiogram.types import Message
from config import my_id

async def send_to_admin(dp):
    await bot.send_message(chat_id=my_id, text="Hi Patrick")

@dp.message_handler()
async def echo(message):
    text = f"Salem sen osyny '{message.text}' jazdyn ba?"
    await bot.send_message(chat_id=message.from_user.id, text=text)


