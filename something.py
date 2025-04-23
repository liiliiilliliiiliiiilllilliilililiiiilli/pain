import asyncio
import sys
import random
import redis

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import types
from aiogram.types import Message


db = redis.Redis (host = 'localhost', port = 6379, db = 0)


bot_token = '8025972966:AAHaUFQxaH-7Uu1XHQGhp5t23WpWk63Cps0'


texts_russian = {

    'from_bot': {

        'greeting': 'Привет. Если тебе очень плохо, можешь дать сигнал и я тебя поддержу. Я постараюсь сделать хоть что-то, но я не знаю, насколько это может изменить что-либо.',

        'i_could_try_to_help_you': 'Я постараюсь поддержать, если тебе больно. Просто попроси.',

        'what_is_this_bot_about': 'Я стараюсь, как могу, чтобы хоть в какой-то степени поддержать тех, кому больно. Напиши, и я отвечу. ',

        'i_could_try_to_help_you': 'Поддержу',

        'settings_choose_a_button': 'Выберите пункт',

        'i_could_try_to_help_you_if_you_ask': 'Я всегда здесь. Просто попроси помощи, и я отвечу.',

        'help_normal_letters': [

            'У тебя все получится',
            'Твоя боль оправдана',
            'Ты сможешь',
            'У тебя все будет хорошо',
            'Ты хороший человек',
            'Что бы ни случилось, знай - ты сможешь',
            'Я ценю то, что ты говоришь',
            'Твои старания обязательно приведут тебя к желаемому',
            'Твои мечты исполнятся',
            'Ты достигнешь своих целей',
            'Я верю в тебя',
            'Я люблю тебя',
            'Мне нравится проводить с тобой время',
            'Как хорошо иметь такого друга, как ты',
            'Ты лучшее, что было в моей жизни',
            'Мне нравится вспоминать время, проведенное с тобой',
            'Ты мне нравишься'

        ],

        'help_low_letters': [

            'у тебя все получится',
            'твоя боль оправдана',
            'ты сможешь',
            'у тебя все будет хорошо',
            'ты хороший человек',
            'что бы ни случилось, знай - ты сможешь',
            'я ценю то, что ты говоришь',
            'твои старания обязательно приведут тебя к желаемому',
            'твои мечты исполнятся',
            'ты достигнешь своих целей',
            'я верю в тебя',
            'я люблю тебя',
            'мне нравится проводить с тобой время',
            'как хорошо иметь такого друга, как ты',
            'ты лучшее, что было в моей жизни',
            'мне навится вспоминать время, проведенное с тобой',
            'ты мне нравишься'

        ]

    },

    'from_user': {

        'commands': {

            'about_this_bot': '/about_this_bot',
            'settings': '/settings'

        },

        'help_me_please': 'Помогите',

        'choose_bot_language': 'Выбрать язык бота',

        'go_back': 'Назад'

    }

}


texts_english = {

    'from_bot': {

        'greeting': 'Hi. If you\'re feeling really bad, you can give me a signal and I\'ll support you. I\'ll try to do at least something, but I don\'t know how much it can change anything.',

        'i_could_try_to_help_you': 'I\'ll try to support you if you\'re in pain. Just ask.',

        'what_is_this_bot_about': 'I try my best to at least support those who are hurting. Write and I will answer.',

        'i_could_try_to_help_you': 'I will support',

        'settings_choose_a_button': 'Choose button',

        'i_could_try_to_help_you_if_you_ask': 'I\'m always here. Just ask for help and I will answer.',

        'help_normal_letters': [

            'You can do it',
            'Your pain is justified',
            'You will succeed',
            'You will be fine.',
            'You are a good person',
            'Whatever happens, know that you can do it.',
            'I appreciate what you say.',
            'Your efforts will definitely lead you to what you want.',
            'Your dreams will come true',
            'You will achieve your goals',
            'I believe in you',
            'I love you',
            'I enjoy spending time with you',
            'How nice to have a friend like you',
            'You are the best thing that has ever happened to me in my life',
            'I like to remember the time spent with you',
            'I like you'

        ],

        'help_low_letters': [
            
            'you can do it',
            'your pain is justified',
            'you will succeed',
            'you will be fine.',
            'you are a good person',
            'whatever happens, know that you can do it.',
            'i appreciate what you say.',
            'your efforts will definitely lead you to what you want.',
            'your dreams will come true',
            'you will achieve your goals',
            'i believe in you',
            'i love you',
            'i enjoy spending time with you',
            'how nice to have a friend like you',
            'you are the best thing that has ever happened to me in my life',
            'i like to remember the time spent with you',
            'i like you'
            
        ]

    },

    'from_user': {

        'commands': {

            'about_this_bot': '/about_this_bot',
            'settings': '/settings'

        },

        'help_me_please': 'help',
        'choose_bot_language': 'Choose bot language',
        'go_back': 'Go back'

    }

}


texts_chinese = {

    'from_bot': {

        'greeting': '你好。如果你感觉真的很糟糕，你可以给我一个信号，我会支持你。我会尝试做至少一些事情，但我不知道这能改变多少事情。',

        'i_could_try_to_help_you': '如果你感到疼痛，我会尽力支持你。尽管说。',

        'what_is_this_bot_about': '我尽力去支持那些正在受伤的人。写下来，我会回复。',

        'i_could_try_to_help_you': '我会支持',

        'settings_choose_a_button': '选择按钮',

        'i_could_try_to_help_you_if_you_ask': '我一直在这里。只要你寻求帮助，我就会解答。',

        'help_normal_letters': [

            '你能做到',
            '你的痛苦是合理的',
            '谢谢你',
            '你会没事的',
            '你是个好人',
            '无论发生什么，你要相信自己可以做到',
            '我很感激你所说的话',
            '你的努力一定会让你得到你想要的',
            '你的梦想将会实现',
            '你会实现你的目标',
            '我相信你',
            '我爱你',
            '我爱你',
            '有你这样的朋友真好',
            '你是我一生中遇到的最美好的事',
            '我喜欢回忆和你在一起的时光',
            '我喜欢你'

        ]

    },

    'from_user': {

        'commands': {

            'about_this_bot': '/about_this_bot',
            'settings': '/settings'

        },

        'help_me_please': '帮助',
        'choose_bot_language': '选择机器人语言',
        'go_back': '回去'

    }

}


texts = texts_russian




def something ():

    return random.choice (texts['from_bot']['help_normal_letters'])



keyboard_markup_main = types.ReplyKeyboardMarkup (

    keyboard = [
        [types.KeyboardButton (text = texts['from_user']['help_me_please'])]
    ],
    resize_keyboard = True,
    input_field_placeholder = texts['from_bot']['i_could_try_to_help_you']

)


keyboard_markup_settings = types.ReplyKeyboardMarkup (

    keyboard = [
        [types.KeyboardButton (text = texts['from_user']['choose_bot_language'])],
        [types.KeyboardButton (text = texts['from_user']['go_back'])]
    ],
    resize_keyboard = True,
    input_field_placeholder = texts['from_bot']['set_up_this_bot']

)



bot = Bot (token = bot_token, default = DefaultBotProperties (parse_mode = ParseMode.HTML))

dp = Dispatcher ()


@dp.message (CommandStart ())
async def command_start_handler (message: Message):

    await message.answer (texts['from_bot']['greeting'], reply_markup = keyboard_markup_main)


@dp.message ()
async def got_message (message: Message):

    if message.text == texts['from_user']['help_me_please']:

        await message.answer (something ())

    elif message.text == texts['from_user']['commands']['about_this_bot']:

        await message.answer (texts['from_bot']['what_is_this_bot_about'])
        
    elif message.text == texts['from_user']['commands']['settings']:

        await message.answer (texts['from_bot']['settings_choose_a_button'], reply_markup = keyboard_markup_main)

    else:

        await message.answer (texts['from_bot']['i_could_try_to_help_you_if_you_ask'])




async def main ():

    bot_commands = [

        types.BotCommand (command = '/about_this_bot', description = 'Об этом боте'),
        types.BotCommand (command = '/settings', description = 'настройки бота')
        # types.BotCommand (command = '/wipe_chat', description = 'удалить все и начать заново')

    ]

    await bot.set_my_commands (bot_commands)


    await dp.start_polling (bot)


if __name__ == '__main__':

    asyncio.run (main ())
