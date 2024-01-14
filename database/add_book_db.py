from config import host, user, password, db_name
import asyncpg

async def add_book_to_db(id, bookname):
    sql = await asyncpg.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    await sql.execute('UPDATE bot_users SET count = (count + 1) WHERE userid = $1', id)
    await sql.execute('UPDATE bot_users SET books = array_append(books, $1) WHERE userid = $2', bookname, id)
    await sql.close()