import asyncio
from bot_create import dp
from bot_create import bot
from routers.register_router import start_router
from callbacks.cb_addbook import addbook_router
from callbacks.cb_countbook import countbook
from database.connect_db import create_database


dp.include_router(start_router)
dp.include_router(countbook)
dp.include_router(addbook_router)

async def main():
    print('Bot successfully started')
    await create_database()
    await dp.start_polling(bot)

asyncio.run(main())