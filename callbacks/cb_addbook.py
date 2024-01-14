from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from database.add_book_db import add_book_to_db

addbook_router = Router()


class Addbook(StatesGroup):
    bookname = State()

@addbook_router.callback_query(F.data.startswith('add.'))
async def add_book(call: CallbackQuery, state: FSMContext):
    await call.message.answer('<b>Вы перешли в раздел добавления книги. Напишите название книги для добавления</b>', parse_mode='html')
    await state.set_state(Addbook.bookname)

@addbook_router.message(Addbook.bookname)
async def add_book_db(msg: Message, state: FSMContext):
    await state.update_data(bookname = msg.text)
    data = await state.get_data()
    bookname = data['bookname']
    await msg.answer(f'<b>Вы успешно добавили книгу {bookname} в полку прочитанных книг</b>', parse_mode='html')
    userid = msg.from_user.id
    await add_book_to_db(userid, bookname)