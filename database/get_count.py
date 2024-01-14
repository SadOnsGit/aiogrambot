from config import host, user, password, db_name
import asyncpg


async def get_count_book(id):
    sql = await asyncpg.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    count = await sql.fetch('SELECT books FROM bot_users WHERE userid = $1', id)
    return count[0][0]