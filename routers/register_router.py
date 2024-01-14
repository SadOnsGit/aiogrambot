from aiogram import Router, types, F
from aiogram.filters import Command
from database.check_user import check_user
from database.register_user import add_user_db
from keyboards.kb_main import mkp_main

start_router = Router()

@start_router.message(Command('start'))
async def register_user(msg: types.Message):
    find = await check_user(msg.from_user.id)
    if find == False:
        username = msg.from_user.username
        await msg.answer(f'<b>Добро пожаловать {username}, мы рады приветствовать тебя в нашем телеграм боте.'
                         '\nБот создан для учёта прочитанных книг.'
                         '\nУспешно зарегистрированы, желаем удачи!</b>', parse_mode='html')
        await add_user_db(msg.from_user.id, 0)
    else:
        await msg.answer('<b>Основное меню</b>', parse_mode='html', reply_markup=mkp_main)