import asyncio
import sys
import random
import redis

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram import types
from aiogram.types import Message
from aiogram.types import CallbackQuery


db = redis.Redis (host = 'localhost', port = 6379, db = 0)


bot_token = '8025972966:AAHaUFQxaH-7Uu1XHQGhp5t23WpWk63Cps0'




texts_russian = {

    'from_bot': {

        'greeting_first': 'Привет... Если тебе очень плохо, подай сигнал, и я тебя поддержу. Я постараюсь сделать хоть что-то, чтобы помочь, но не знаю, может ли это что-либо изменить.',
        'greeting_regular': 'Если тебе очень плохо, подай сигнал, и я тебя поддержу. Я постараюсь сделать хоть что-то, чтобы помочь, но не знаю, может ли это что-либо изменить.',
        'what_is_this_bot_about': 'Я стараюсь, как могу, чтобы хоть в какой-то степени поддержать тех, кому больно. Напиши, и я отвечу.',

        'choose_a_language': '🌐 Выберите язык:',

        'russian': '🇷🇺 Русский',
        'english': '🇬🇧 Английский',
        'chinese': '🇨🇳 Китайский',

        'chosen_language_russian': '🇷🇺 Выбран язык: Русский.',
        'chosen_language_english': '🇬🇧 Выбран язык: Английский.',
        'chosen_language_chinese': '🇨🇳 Выбран язык: Китайский.',

        'our_channel': 'Наш канал',

        'i_could_try_to_help_you': 'Поддержу',

        'settings': '⚙️ Настройки бота:',

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
            'Ты мне нравишься',
            'Твоя усердная работа не останется незамеченной.',
            'Не теряй надежду, впереди светлое будущее.',
            'Ты достоин лучшего. Поверь в себя.',
            'Каждый шаг приближает тебя к цели. Ты на верном пути.',
            'Скоро настанет момент, когда ты почувствуешь радость успеха.',
            'Твоя уверенность и решимость вдохновляют окружающих.',
            'Ты важен и ценен, не сомневайся в себе.',
            'Любая неудача - это урок на пути к успеху.',
            'Ты заслуживаешь любви и уважения.',
            'День за днем ты делаешь прогресс, не сдавайся!',
            'Ты уникален и способен на великие дела.',
            'Все проходящее урок, из которого можно извлечь силу и мощь.',
            'Верь в себя - это первый шаг к достижению мечты.',
            'Каждое усилие приближает тебя к желаемому результату.',
            'Твоя целеустремленность и усердие не останутся незамеченными.',
            'Самое важное - не соперничать с другими, а превзойти самого себя.',
            'Не теряй веру, у тебя всё получится.',
            'Ты сильнее, чем кажется. Держись!',
            'Твоя упорство и мудрость не останутся незамеченными.',
            'Каждый день - это шаг вперёд. Ты идешь в правильном направлении.',
            'Помни, что ты не одинок. Я здесь, чтобы тебя поддержать.',
            'Твоя доброта и целеустремленность ценны как золото.',
            'Всегда помни, что ты заслуживаешь счастья и успеха.',
            'Твоя сила и решимость вдохновляют окружающих на лучшее.',
            'Я всегда здесь.',
            'Твои чувства важны и они должры быть услышаны.',
            'Сейчас тяжело, но это не навсегда — ты сильнее, чем думаешь.',
            'Ты заслуживаешь заботы и тепла, даже в самые тёмные дни.',
            'Каждый твой шаг, даже маленький, приближает к свету.',
            'Ты имеешь право на боль, но помни — и на исцеление тоже.',
            'Иногда просто пережить день — уже победа. Гордись собой.',
            'Ты важен для этого мира, даже если сейчас не веришь.',
            'Твоя история еще не закончена, и в ней будет много хорошего.',
            'Ты достоин любви, даже когда кажется, что её нет.',
            'Твоя сила — в умении чувствовать. Это не слабость.',
            'Ты не обязан быть идеальным — достаточно быть собой.',
            'Даже в тишине твоя жизнь имеет огромное значение.',
            'Слезы — это язык души. Дай им говорить.',
            'Ты уже пережил столько — я верю, ты справишься и сейчас.',
            'Иногда достаточно просто быть, а не делать.',
            'Ты — целая вселенная, и в тебе есть свет, который не гаснет.',
            'Твои мечты не забыты — они ждут своего часа.',
            'Ты нужен этому миру именно таким, какой ты есть.',
            'Боль не вечна, а твоё мужество останется с тобой.',
            'Даже если кажется, что всё рушится — ты можешь начать заново.',
            'Твоя ценность не в том, чтобы нравится всем.',
            'Иногда достаточно просто выдохнуть.',
            'Твоё сердце знает путь, даже если разум заблудился.',
            'Ты уже делаешь всё возможное — и это достаточно.',
            'Даже в темноте можно найти звёзды. Нужно просто посмотреть наверх.',
            'Ты не слабый из-за боли — ты живой человек.',
            'Каждое «плохо» когда-нибудь станет воспоминанием. Держись.',
            'Ты можешь чувствовать себя потерянным сейчас, но это не значит, что ты сбился с пути. Иногда самые важные дороги начинаются в темноте. Я верю, что ты найдешь свой свет.',
            'Боль не делает тебя слабым — она показывает, как многое ты можешь пережить. Ты уже выдержал столько, и это доказывает, что внутри есть сила, которой ты можешь доверять.',
            'Даже если кажется, что никто не понимает твоих чувств, помни: твои эмоции — это часть твоей истории. Они важны, и ты имеешь право на них, не оправдываясь.',
            'Иногда мир становится тяжелым, как камень, но тебе не обязательно нести его в одиночку. Позволь себе сделать паузу — даже горы отдыхают под облаками.',
            'Ты думаешь, что это конец, но я вижу начало. Каждое испытание — это невидимая дверь. Когда-нибудь ты оглянешься и поймешь, какой был пройден далекий путь.',
            'Не кори себя за слезы или усталость. Иногда дождь нужен, чтобы земля дала ростки. Ты заслуживаешь времени, чтобы залечить раны.',
            'Ты можешь не верить в себя сегодня, но знай: где-то в тебе живет то, что всегда верило в мечты. Я буду помнить о нем, пока ты не вспомнишь.',
            'Даже если ты не видишь смысла, твое существование меняет мир. Как звезды, которые светят, даже когда их не замечают.',
            'Быть сильным не обязательно каждую секунду. Иногда достаточно просто дышать и ждать, пока шторм утихнет.',
            'Жизнь — это не гонка, где нужно спешить. Ты можешь идти медленно, останавливаться, даже ползти — главное, что ты продолжаешь. И это уже победа.',
            'Твоя боль — не вечность. Когда-нибудь ты расскажешь эту историю и удивишься, как много в ней было мужества.',
            'Ты не ошибка. Ты — человек, который учится, падает и встает. И каждый раз, когда ты встаешь, мир становится чуть добрее.',
            'Даже если ты чувствуешь себя разбитым человеком, помни: осколки могут стать мозаикой. Ты еще создашь что-то прекрасное из того, что кажется бесполезным.',
            'Не бойся своих слез — они поливают почву души. То, что растет после, будет крепче и мудрее. Я горжусь тобой за то, что ты позволяешь себе чувствовать.'

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

            'about_this_bot': '/about',
            'settings': '/settings'

        },

        'help_me_please': 'Помогите',

        'choose_bot_language': 'Язык интерфейса (Русский)',

        'go_back': 'Назад',

        'cancel': 'Отмена',

        'go_home': 'На главную'

    },

    'menu': {

        'about': 'О боте',
        'settings': 'Настройки'

    }

}


texts_english = {

    'from_bot': {

        'greeting': 'Hi. If you\'re feeling really bad, you can give me a signal and I\'ll support you. I\'ll try to do at least something, but I don\'t know how much it can change anything.',
        'i_could_try_to_help_you': 'I\'ll try to support you if you\'re in pain. Just ask.',
        'what_is_this_bot_about': 'I try my best to at least support those who are hurting. Write and I will answer.',
        'choose_a_language': 'Choose a language',

        'settings': 'chosen_language_english',

        'russian': 'Russian',
        'english': 'English',
        'chinese': 'Chinese',

        'our_channel': 'Our channel',

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
            'I like you',
            'Your hard work will not go unnoticed.',
            'Don\'t lose hope, there is a bright future ahead.',
            'You deserve the best. Believe in yourself.',
            'Every step brings you closer to your goal. You are on the right track.',
            'Soon there will come a time when you will feel the joy of success.',
            'Your confidence and determination inspire others.',
            'You are important and valuable, do not doubt yourself.',
            'Any failure is a lesson on the path to success.',
            'You deserve love and respect.',
            'Day after day you make progress, do not give up!',
            'You are unique and capable of great things.',
            'Everything that happens is a lesson from which you can draw strength and power.',
            'Believe in yourself - this is the first step to achieving your dreams.',
            'Every effort brings you closer to the desired result.',
            'Your determination and diligence will not go unnoticed.',
            'The most important thing is not to compete with others, but to surpass yourself.',
            'Don\'t lose faith, you will succeed.',
            'You are stronger than you seem. Hold on!',
            'Your tenacity and wisdom will not go unnoticed.',
            'Every day is a step forward. You are going in the right direction.',
            'Remember that you are not alone. I am here to support you.',
            'Your kindness and determination are as valuable as gold.',
            'Always remember that you deserve happiness and success.',
            'Your strength and determination inspire others to do better.',
            'I am always here.',
            'Your feelings are important and they should be heard.',
            'It is hard now, but it will not be forever - you are stronger than you think.',
            'You deserve care and warmth, even on the darkest days.',
            'Every step you take, no matter how small, brings you closer to the light.',
            'You have the right to pain, but remember - and to healing too.',
            'Sometimes just surviving a day is already a victory. Be proud of yourself.',
            'You are important to this world, even if you do not believe it now.',
            'Your story is not over yet, and there will be a lot of good in it.',
            'You deserve love, even when it seems that there is none.',
            'Your strength is in the ability to feel. This is not weakness.',
            'You do not have to be perfect - it is enough to be yourself.',
            'Even in silence, your life has great meaning.',
            'Tears are the language of the soul. Let them speak.',
            'You\'ve been through so much already - I believe you can handle it now.',
            'Sometimes it\'s enough to just be, not to do.',
            'You are a whole universe, and there is a light inside you that never goes out.',
            'Your dreams are not forgotten - they are waiting for their time.',
            'This world needs you exactly as you are.',
            'Pain is not eternal, and your courage will remain with you.',
            'Even if it seems like everything is falling apart - you can start over.',
            'Your value is not in being liked by everyone.',
            'Sometimes it\'s enough to just exhale.',
            'Your heart knows the way, even if your mind is lost.',
            'You are already doing everything you can - and that\'s enough.',
            'Even in the darkness you can find the stars. You just need to look up.',
            'You are not weak because of pain - you are a living person.',
            'Every "bad" will one day become a memory. Hold on.',
            'You may feel lost right now, but that doesn’t mean you’ve lost your way. Sometimes the most important roads start in the dark. I believe you’ll find your light.',
            'Pain doesn’t make you weak, it shows how much you can handle. You’ve endured so much already, and that proves that there’s a strength inside you that you can trust.',
            'Even if it seems like no one understands your feelings, remember: your emotions are part of your story. They’re important, and you have a right to them without making excuses.',
            'Sometimes the world feels heavy as a stone, but you don’t have to carry it alone. Allow yourself to pause, even the mountains rest under the clouds.',
            'You think this is the end, but I see a beginning. Every trial is an invisible door. Someday you’ll look back and realize how far you’ve come.',
            'Don’t beat yourself up for crying or being tired. Sometimes it takes rain to make the earth grow. You deserve time to heal.',
            'You may not believe in yourself today, but know that somewhere inside you lives something that always believed in dreams. I will remember it until you do.',
            'Even if you don’t see the point, your existence changes the world. Like the stars that shine even when no one notices them.',
            'You don’t have to be strong every second. Sometimes it’s enough to just breathe and wait for the storm to pass.',
            'Life is not a race where you have to hurry. You can go slowly, stop, even crawl - the main thing is that you continue. And that’s already a victory.', 
            'Your pain is not eternity. Someday you will tell this story and be surprised at how much courage there was in it.',
            'You are not a mistake. You are a person who learns, falls and gets up. And every time you get up, the world becomes a little kinder.',
            'Even if you feel like a broken person, remember: the shards can become a mosaic.  You will still create something beautiful from what seems useless.',
            'Don\'t be afraid of your tears - they water the soil of the soul. What grows after will be stronger and wiser. I am proud of you for allowing yourself to feel.'

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

            'about_this_bot': '/about',
            'settings': '/settings'

        },

        'help_me_please': 'help',
        'choose_bot_language': 'Choose bot language',
        'go_back': 'Go back'

    },

    'menu': {

        'about': 'About this bot',
        'settings': 'Settings'
    }

}


texts_chinese = {

    'from_bot': {

        'greeting': '你好。如果你感觉真的很糟糕，你可以给我一个信号，我会支持你。我会尝试做至少一些事情，但我不知道这能改变多少事情。',
        'i_could_try_to_help_you': '如果你感到疼痛，我会尽力支持你。尽管说。',
        'what_is_this_bot_about': '我尽力去支持那些正在受伤的人。写下来，我会回复。',

        'i_could_try_to_help_you': '我会支持',

        'choose_a_language': '选择语言',

        'russian': '俄语',
        'english': '英语',
        'chinese': '中国',

        'our_channel': '我们的频道',

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
            '我喜欢你',
            '您的辛勤工作不会被忽视。',
            '不要失去希望，前面有光明的未来。',
            '你值得更好的。相信你自己。',
            '每一步都让你更接近目标。你走在正确的道路上。',
            '您感受到成功的喜悦的时刻很快就会到来。',
            '您的自信和决心激励了其他人。',
            '你很重要，很有价值，不要怀疑自己。',
            '每一次失败都是成功道路上的一次教训。',
            '你值得被爱和尊重。',
            '你每天都在进步，不要放弃！',
            '您是独一无二的，并且有能力成就伟大的事情。',
            '发生的每件事都是一个教训，人们可以从中汲取力量和动力。',
            '相信自己——这是实现梦想的第一步。',
            '每一次努力都会让你更接近期望的结果。',
            '您的奉献和努力不会被忽视。',
            '最重要的不是与别人竞争，而是超越自己。',
            '不要失去信心，你可以做到。',
            '你比看上去的更强大。坚持，稍等！',
            '您的毅力和智慧不会被忽视。',
            '每天都是向前迈出的一步。你正朝着正确的方向前进。',
            '请记住，你并不孤单。我在这里支持你。',
            '您的善良和决心就像黄金一样宝贵。',
            '永远记住，你值得拥有幸福和成功。',
            '您的力量和决心激励他人做得更好。',
            '我一直在这里。',
            '您的感受很重要，应该被倾听。',
            '现在很艰难，但不会永远如此——你比你想象的更强大。',
            '即使在最黑暗的日子里，你也值得关心和温暖。',
            '你迈出的每一步，即使是很小的一步，也会让你更接近光明。',
            '您有权利承受痛苦，但请记住，您也有权利获得治愈。',
            '有时，只要活下来就是一种胜利。为自己感到骄傲。',
            '你对这个世界很重要，即使你现在不相信。',
            '你的故事还没有结束，其中还会有很多精彩内容。',
            '你值得被爱，即使看似没有。',
            '你的力量在于你的感受能力。这并不是软弱。',
            '你不必完美，只要做你自己就行。',
            '即使沉默不语，你的生命也意义非凡。',
            '眼泪是灵魂的语言。让他们说话。',
            '你已经经历了这么多——我相信你现在也能应付。',
            '有时候，只要存在就足够了，不需要做任何事情。',
            '你就是整个宇宙，你内心有一道永不熄灭的光芒。',
            '你的梦想并没有被遗忘——它们正在等待时机。',
            '这个世界需要你本来的样子。',
            '痛苦不是永恒的，但勇气会伴随你。',
            '即使看起来一切都崩溃了，你也可以重新开始。',
            '你的价值并不在于被所有人喜欢。',
            '有时只需呼气就足够了。',
            '即使你的思想迷失了，你的心也知道路。',
            '你已经尽力了——这就足够了。',
            '即使在黑暗中你也能找到星星。你只需要抬头看看。',
            '你不会因为痛苦而变得软弱——你是一个活生生的人。',
            '每件“坏”事最终都会成为记忆。坚持，稍等。',
            '您现在可能会感到迷茫，但这并不意味着您偏离了轨道。有时最重要的道路始于黑暗。我相信你一定会找到属于你的光芒。',
            '痛苦并不会让你变得软弱——它表明你能忍受多少。你已经承受了这么多，这证明你内心拥有值得信赖的力量。',
            '即使似乎没有人理解你的感受，请记住：你的情绪是你故事的一部分。它们很重要，您有权利获得它们，无需找借口。',
            '有时你会感觉世界像石头一样沉重，但你不必独自承受。让自己休息一下——就连群山也在云层下休息。',
            '你以为这是结束，但我看到的却是开始。每一次考验都是一扇看不见的门。有一天，当你回首往事时，你会意识到你已经走了多远。',
            '不要因为眼泪或疲劳而责怪自己。有时，土地要雨水才能发芽。你需要时间来治愈。',
            '今天你也许不相信自己，但要知道，在你内心深处，总有一些东西一直相信梦想。我会记住他，直到你记住为止。',
            '即使你不明白这一点，你的存在也会改变世界。就像星星，即使你没有注意到它们，它们也会闪耀。',
            '你不必每时每刻都坚强。有时，只要深呼吸并等待暴风雨过去就足够了。',
            '生活并不是一场需要你加快速度的比赛。你可以慢慢走，停下来，甚至爬行——最重要的是你要坚持下去。这已经是一场胜利。',
            '你的痛苦不会是永远的。有一天，你会讲述这个故事，并惊叹于其中蕴含的勇气。',
            '你不是一个错误。你是一个不断学习、跌倒并重新站起来的人。每次你站起来，世界就会变得更友善一点。',
            '即使你感觉自己像一个破碎的人，请记住：碎片可以变成马赛克。你仍然会用看似无用的东西创造出美丽的东西。',
            '不要害怕你的眼泪——它滋润心灵的土壤。之后成长起来的东西将会更加强大和聪明。我为你允许自己去感受而感到骄傲。'

        ]

    },

    'from_user': {

        'commands': {

            'about_this_bot': '/about',
            'settings': '/settings'

        },

        'help_me_please': '帮助',
        'choose_bot_language': '选择机器人语言',
        'go_back': '回去'

    },

    'menu': {

        'about': '关于这个机器人',
        'settings': '设置'
    }

}


async def texts (get_texts, user_id):
    
    return get_texts (texts_russian)




async def something (message):

    return random.choice (await texts (lambda texts: texts['from_bot']['help_normal_letters'], message.from_user.id))




class Form (StatesGroup):

    page_main = State ()
    page_settings = State ()
    page_settings_languages = State ()


async def bot_menu (message):
    
    return [

        types.BotCommand (
            command = '/about',
            description = await texts (lambda texts: texts['menu']['about'], message.from_user.id)),
        types.BotCommand (
            command = '/settings',
            description = await texts (lambda texts: texts['menu']['settings'], message.from_user.id))

    ]


async def keyboard_markup_main (message):
    
    return types.ReplyKeyboardMarkup (

        keyboard = [[
            types.KeyboardButton (text = await texts (lambda texts: texts['from_user']['help_me_please'], message.from_user.id))]
        ],
        resize_keyboard = True

)


async def keyboard_markup_settings (message):
    
    return types.ReplyKeyboardMarkup (

        keyboard = [[
            types.KeyboardButton (text = await texts (lambda texts: texts['from_user']['choose_bot_language'], message.from_user.id))],
        [
            types.KeyboardButton (text = await texts (lambda texts: texts['from_user']['go_home'], message.from_user.id))]
        ],
        resize_keyboard = True,
        # input_field_placeholder = texts['from_bot']['settings_choose_a_button']

)


async def inline_keyboard_markup_about (message):
    
    return types.InlineKeyboardMarkup (

        inline_keyboard = [[
            types.InlineKeyboardButton (
                texts = await texts (lambda texts: texts['from_bot']['our_channel'], message.from_user.id),
                url = 'https://t.me/li_ta_mi')]
        ]

)


async def keyboard_markup_settings_language (message):
    
    return types.ReplyKeyboardMarkup (

        keyboard = [[
            types.KeyboardButton (text = await texts (lambda texts: texts['from_bot']['russian'], message.from_user.id)),
            types.KeyboardButton (text = await texts (lambda texts: texts['from_bot']['english'], message.from_user.id)),
            types.KeyboardButton (text = await texts (lambda texts: texts['from_bot']['chinese'], message.from_user.id))],
        [
            types.KeyboardButton (text = await texts (lambda texts: texts['from_user']['go_back'], message.from_user.id)),
            types.KeyboardButton (text = await texts (lambda texts: texts['from_user']['go_home'], message.from_user.id))]
        ],
        resize_keyboard = True,
        # input_field_placeholder = texts['from_bot']['settings_choose_a_button']

)




bot = Bot (token = bot_token, default = DefaultBotProperties (parse_mode = ParseMode.HTML))

dp = Dispatcher ()




@dp.message (Command ('start'))
async def command_start (message: Message, state: FSMContext):

    await state.set_state (Form.page_main)

    await bot.set_my_commands (await bot_menu (message))
    await message.answer (

        await texts (lambda texts: texts['from_bot']['greeting_first' if message.text == '/start' else 'greeting_regular' if message.text in [texts['from_user']['go_home'], texts['from_user']['go_back']] else 'i_could_try_to_help_you_if_you_ask'], message.from_user.id),
        reply_markup = await keyboard_markup_main (message)

    )


@dp.message (Command ('about'))
async def command_about (message: Message, state: FSMContext):

    await state.set_state (Form.page_main)

    await message.answer (
        
        await texts (lambda texts: texts['from_bot']['what_is_this_bot_about'], message.from_user.id),
        reply_markup = await inline_keyboard_markup_about (message)
        
    )


@dp.message (Command ('settings'))
async def command_settings (message: Message, state: FSMContext):

    await state.set_state (Form.page_settings)

    await message.answer (

        await texts (lambda texts: texts['from_bot']['settings'], message.from_user.id),
        reply_markup = await keyboard_markup_settings (message)

    )




# await bot.delete_messages (chat_id = call.message.chat.id, message_ids = [
#     call.message.message_id,
#     call.message.message_id - 1
# ])




@dp.message (Form.page_main)
async def got_message (message: Message, state: FSMContext):

    if message.text == await texts (lambda texts: texts['from_user']['help_me_please'], message.from_user.id):

        await state.set_state (Form.page_main)
        await message.answer (await something (message))

    elif message.text == await texts (lambda texts: texts['from_user']['commands']['about_this_bot'], message.from_user.id):

        await state.set_state (Form.page_main)
        await message.answer (await texts (lambda texts: texts['from_bot']['what_is_this_bot_about'], message.from_user.id))
        
    elif message.text == await texts (lambda texts: texts['from_user']['commands']['settings'], message.from_user.id):

        await state.set_state (Form.page_settings)

        await message.answer (

            await texts (lambda texts: texts['from_bot']['settings'], message.from_user.id),
            reply_markup = await keyboard_markup_settings (message)

        )

    elif (message.text != '/start' and message.text != '/about' and message.text != '/settings'):

        await state.set_state (Form.page_main)
        await message.answer (await texts (lambda texts: texts['from_bot']['i_could_try_to_help_you_if_you_ask'], message.from_user.id))


@dp.message (Form.page_settings)
async def settings_page_handler (message: Message, state: FSMContext):

    if message.text == await texts (lambda texts: texts['from_user']['choose_bot_language'], message.from_user.id):

        await state.set_state (Form.page_settings_languages)
        await message.answer (

            await texts (lambda texts: texts['from_bot']['choose_a_language'], message.from_user.id),
            reply_markup = await keyboard_markup_settings_language (message)

        )

    elif message.text == await texts (lambda texts: texts['from_user']['go_home'], message.from_user.id):

        await command_start (message, state)

    elif (message.text != '/start' and message.text != '/about' and message.text != '/settings'):

        await command_start (message, state)
        # await message.answer (texts['from_bot']['i_could_try_to_help_you_if_you_ask'])


@dp.message (Form.page_settings_languages)
async def settings_language_page_handler (message: Message, state: FSMContext):

    if message.text == texts['from_bot']['russian']:

        setLanguageUser (message.from_user.id, 'russian')

        await state.set_state (Form.page_settings)

        await message.answer (await texts (lambda texts: texts['from_bot']['chosen_language_russian'], message.from_user.id))

        await message.answer (

            await texts (lambda texts: texts['from_bot']['settings'], message.from_user.id),
            reply_markup = await keyboard_markup_settings (message)

        )

    elif message.text == texts['from_bot']['english']:

        setLanguageUser (message.from_user.id, 'english')

        await state.set_state (Form.page_settings)

        await message.answer (await texts (lambda texts: texts['from_bot']['chosen_language_english'], message.from_user.id))

        await message.answer (

            texts['from_bot']['settings'],
            reply_markup = await keyboard_markup_settings (message)
        
        )

    elif message.text == texts['from_bot']['chinese']:

        setLanguageUser (message.from_user.id, 'chinese')

        await state.set_state (Form.page_settings)

        await message.answer (await texts (lambda texts: texts['from_bot']['chosen_language_chinese']), message.from_user.id)

        await message.answer (

            await texts (lambda texts: texts['from_bot']['settings'], message.from_user.id),
            reply_markup = await keyboard_markup_settings (message)

        )

    elif message.text == await texts (lambda texts: texts['from_user']['go_home'], message.from_user.id):

        await command_start (message, state)

    elif message.text == await texts (lambda texts: texts['from_user']['go_back'], message.from_user.id):

        await state.set_state (Form.page_settings)

        await message.answer (

            await texts (lambda texts: texts['from_bot']['settings'], message.from_user.id),
            reply_markup = await keyboard_markup_settings (message)

        )

    elif (message.text != '/start' and message.text != '/about' and message.text != '/settings'):

        await command_start (message, state)
        # await message.answer (texts['from_bot']['i_could_try_to_help_you_if_you_ask'])




async def main ():

    # await bot.set_my_commands (await bot_menu ())

    await dp.start_polling (bot)




if __name__ == '__main__':

    asyncio.run (main ())