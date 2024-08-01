import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.filters import Command

from gen_message import generate_messange

# Открываем файл в режиме чтения
with open('senior/tg_api.txt', 'r') as file:
    # Читаем содержимое файла
    TOKEN = file.read()

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    greeting = '''🚀 Приветствуем тебя в нашей команде на хаккатоне! 🌟

Я твой виртуальный ассистент, готовый помочь тебе на этом захватывающем пути к созданию инновационных решений. 🛠️

🔍 Чем могу помочь? Вот несколько вещей, которые ты можешь узнать или сделать прямо сейчас:

/start - Начать общение с ботом
/help - Получить помощь и список доступных команд
/schedule - Узнать расписание мероприятий
/team - Информация о твоей команде
/resources - Получить полезные ресурсы и ссылки

Также я могу еще и кодить!

Не стесняйся использовать эти команды, чтобы максимально эффективно использовать время на хаккатоне. Давай вместе создадим что-то удивительное! 🌈

Удачи и отличного кодинга! 💻🎉'''
    await message.answer(greeting)

# Обработчики команд
@dp.message(Command("help"))
async def cmd_help(message: Message):
    help_message = '''/start - Начать общение с ботом
/help - Получить помощь и список доступных команд
/schedule - Узнать расписание мероприятий
/team - Информация о твоей команде
/resources - Получить полезные ресурсы и ссылки
/ask - Задать вопрос организаторам
'''
    await message.reply(help_message)

@dp.message(Command("schedule"))
async def cmd_schedule(message: Message):
    schedule = '''📌 Даты проведения:  
➡️ с 5 августа 2024 г. по 16 августа 2024 г. (до 23:59 часов 00 минут по московскому времени) проведение хакатона и прием решений;  
➡️ с 17 августа по 20 августа 2024 г. - определение победителей и призеров. 
'''
    await message.reply(schedule)

@dp.message(Command("team"))
async def cmd_team(message: Message):
    team_answer = 'В команде моего создателя Dungeon masters🙃 2 человека - Нурсултан и Дима '
    await message.reply(team_answer)

@dp.message(Command("resources"))
async def cmd_resources(message: Message):
    resources = 'https://ai-arrow-camp.com/'
    await message.reply(resources)

@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        print(message.text)
        await message.reply(await generate_messange(message.text))
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())