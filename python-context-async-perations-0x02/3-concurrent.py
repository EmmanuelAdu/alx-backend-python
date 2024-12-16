import aiosqlite
import asyncio



# Initializing database with sample data
async def setup_database(db_name):
    async with aiosqlite.connect(db_name) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255),
                age INTEGER,
                email VARCHAR(255)
            )
        """)

    await db.execute("INSERT INTO users (name, age, email) VALUES ('Alice', 30, 'alice@example.com')")
    await db.execute("INSERT INTO users (name, age, email) VALUES ('Bob', 50, 'bob@example.com')")
    await db.execute("INSERT INTO users (name, age, email) VALUES ('Charlie', 45, 'charlie@example.com')")
    await db.execute("INSERT INTO users (name, age, email) VALUES ('Diana', 20, 'diana@example.com')")
    await db.commit()


# Async function to fetch all users
async def async_fetch_users(db_name):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("All Users:")
            for user in users:
                print(user)
            return users

# Async function to fetch users older than 40
async def async_fetch_older_users(db_name):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            older_users = await cursor.fetchall()
            print("All Users:")
            for user in older_users:
                print(user)
            return older_users


# Main function to run function concurrently
async def fetch_concurrently(db_name):
    await setup_database(db_name)
    results = await asyncio.gather(
        async_fetch_users(db_name),
        async_fetch_older_users(db_name)
    )
    return results


if __name__ == "__main__":
    db_name = "users.db"
    asyncio.run(fetch_concurrently(db_name))

