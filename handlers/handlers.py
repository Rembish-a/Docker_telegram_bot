from aiogram import types
from main import bot, dp
from settings import admin_id
from src.database.create_table import execute_query
from zoneinfo import ZoneInfo
from datetime import datetime



async def send_to_admin(dp):
    " Функція відправки повідомлення адміну"
    await bot.send_message(chat_id=admin_id, text="Бот активований")
    await bot.send_message(chat_id=admin_id, text="Натисніть   /start")



@dp.message_handler(commands=["/start", "/help"])
async def start_handler(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_full_name = message.from_user.full_name
    # create_profile(id=user_id, f_name=first_name, l_name=last_name, info_i=user_full_name)
    timestamp_now = datetime.now(tz=ZoneInfo("UTC")).isoformat(" ")
    insert_query = (f"INSERT INTO message (message, userid, message_time) "
                    f"VALUES ({message.text}, {message.from_user['id']}, {timestamp_now})")
    execute_query(insert_query)
    await bot.send_message(user_id, text="Hi!\nI'm EchoBot!")

# @dispatcher.message_handler(commands=["start", "help"])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     timestamp_now = datetime.now(tz=ZoneInfo("UTC")).isoformat(" ")
#     insert_query = (f"INSERT INTO message (message, userid, message_time) "
#                     f"VALUES ({message.text}, {message.from_user['id']}, {timestamp_now})")
#     execute_query(insert_query)
#     await message.reply("Hi!\nI'm EchoBot!")




@dp.message_handler()
async def echo(message: types.Message):
    " Функція відправки ехо-повідомлення"
    user_id = message.from_user.id
    timestamp_now = datetime.now(tz=ZoneInfo("UTC")).isoformat(" ")
    insert_query = (f"INSERT INTO message (message, userid, message_time) "
                    f"VALUES ('{message.text}', {message.from_user['id']}, '{timestamp_now}')")
    execute_query(insert_query)
    await bot.send_message(user_id, text=f"ви написали {message.text}")

# @dispatcher.message_handler()
# async def echo(message: types.Message):
#     """
#     This handler accepts any message and sends it back unchanged.
#     """
#     timestamp_now = datetime.now(tz=ZoneInfo("UTC")).isoformat(" ")
#     insert_query = (f"INSERT INTO message (message, userid, message_time) "
#                     f"VALUES ('{message.text}', {message.from_user['id']}, '{timestamp_now}')")
#     execute_query(insert_query)
#     await message.answer(message.text)















