import asyncio
import sys
import random

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


bot_token = '8025972966:AAHaUFQxaH-7Uu1XHQGhp5t23WpWk63Cps0'



greeting = ''

something_else = [

    'у тебя все получится',
    'твоя боль оправдана',
    'ты сможешь',
    'у тебя все будет хорошо',
    'ты хороший человек',
    'что бы ни случилось, знай - ты сможешь',
    'я ценю то, что ты говоришь',
    'твои старания обязательно приведут тебя к желаемому',
    'твои мечты исполнятся',
    'ты точно достигнешь своих целей',
    'я верю в тебя'

]


def something ():

    return random.choice (something_else)




dp = Dispatcher ()


@dp.message (CommandStart ())
async def command_start_handler (message: Message):

    await message.answer (f'Привет. Если тебе очень плохо, можешь дать сигнал и я тебя поддержу. Также можешь попросить меня периодически писать, и я постараюсь сделать хоть что-то. Но я не знаю, насколько это может именить что-либо.')


@dp.message ()
async def got_language (message: Message):

    if message.text == 'помогите':

        await message.answer (something ())

    else:

        0
        # await message.answer (':[')




async def main ():

    bot = Bot (token = bot_token, default = DefaultBotProperties (parse_mode = ParseMode.HTML))

    await dp.start_polling (bot)


if __name__ == '__main__':

    asyncio.run (main ())