from config import host, user, password, db_name
import asyncpg


async def add_user_db(id, count):
    sql = await asyncpg.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    await sql.execute('INSERT INTO bot_users (userid, count, books) VALUES ($1, $2, ARRAY[]::text[])', id, count)
    await sql.close()