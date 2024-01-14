from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

mkp_main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Список прочитанных книг', callback_data='count.book')
    ],
    [
        InlineKeyboardButton(text = 'Добавить книгу', callback_data='add.book')
    ]
])