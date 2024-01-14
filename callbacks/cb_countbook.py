from aiogram.types import CallbackQuery
from aiogram import Router, F
from database.get_count import get_count_book

countbook = Router()

@countbook.callback_query(F.data.startswith('count.'))
async def cb_count(call: CallbackQuery):
    list_books = await get_count_book(call.message.chat.id)
    s = '\n'.join(list_books)
    await call.message.answer(f'<b>Ваши прочитанные книги: \n{s}</b>', parse_mode='html')
    await call.answer()