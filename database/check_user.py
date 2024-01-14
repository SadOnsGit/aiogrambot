import asyncpg
from config import host, user, password, db_name

async def check_user(userid):
    sql = await asyncpg.connect(
        host=host,
        user=user,
        password=password,
        database=db_name)
    find_userid = await sql.fetch('SELECT * FROM bot_users WHERE userid = $1', userid)
    await sql.close()
    if find_userid:
        return True
    else:
        return False