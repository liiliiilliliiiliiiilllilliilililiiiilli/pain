import asyncio
import sys
import random

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import types
from aiogram.types import Message


bot_token = '8025972966:AAHaUFQxaH-7Uu1XHQGhp5t23WpWk63Cps0'



texts = {

    'from_bot': {

        'greeting': 'Привет. Если тебе очень плохо, можешь дать сигнал и я тебя поддержу. Еще можешь попросить меня периодически писать, и я постараюсь сделать хоть что-то. Но я не знаю, насколько это может именить что-либо.',

        'i_could_try_to_help_you': 'Я постараюсь поддержать, если тебе больно. Просто попроси.',

        'i_could_try_to_help_you': 'Постараюсь поддержать',

        'help__normal_letters': [

            'У тебя все получится',
            'Твоя боль оправдана',
            'Ты сможешь',
            'У тебя все будет хорошо',
            'Ты хороший человек',
            'Что бы ни случилось, знай - ты сможешь',
            'Я ценю то, что ты говоришь',
            'Твои старания обязательно приведут тебя к желаемому',
            'Твои мечты исполнятся',
            'Ты точно достигнешь своих целей',
            'Я верю в тебя'

        ],

        'help__low_letters': [

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

    },

    'from_user': {

        'commands': {

            'wipe_chat': '/wipe_chat',

        },

        'help_me_please': 'помогите'

    }

}


def something ():

    return random.choice (texts['from_bot']['help__normal_letters'])




dp = Dispatcher ()


@dp.message (CommandStart ())
async def command_start_handler (message: Message):

    keyboard_presses = [[types.KeyboardButton (text = texts['from_user']['help_me_please'])]]

    keyboard_markup = types.ReplyKeyboardMarkup (

        keyboard = keyboard_presses,
        resize_keyboard = True,
        input_field_placeholder = texts['from_bot']['i_could_try_to_help_you']

    )

    await message.answer (texts['from_bot']['greeting'], reply_markup = keyboard_markup)


@dp.message ()
async def got_help_me (message: Message):

    if message.text == texts['from_user']['help_me_please']:

        await message.answer (something ())

    elif message.text == texts['from_user']['commands']['wipe_chat']:

        await bot.delete_messages (message.chat.id, range (1, message.message_id))

    else:

        await message.answer (texts['from_bot']['i_could_try_to_help_you'])




async def main ():

    bot = Bot (token = bot_token, default = DefaultBotProperties (parse_mode = ParseMode.HTML))


    bot_commands = [

        types.BotCommand (command = '/settings', description = 'настройки бота'),
        types.BotCommand (command = '/wipe_chat', description = 'удалить все и начать заново')

    ]

    await bot.set_my_commands (bot_commands)



    await dp.start_polling (bot)


if __name__ == '__main__':

    asyncio.run (main ())