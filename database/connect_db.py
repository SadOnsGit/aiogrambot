import asyncpg
from config import host, user, password, db_name

async def create_database():
    try:
        sql = await asyncpg.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
        await sql.execute('''CREATE TABLE IF NOT EXISTS bot_users(
                        userid INT,
                        count INT,
                        books TEXT[]
        )
    ''')
    except Exception as _ex:
        print(f'Connect to PostgreSQL database failed. Error: {_ex}')
    finally:
        if sql:
            await sql.close()