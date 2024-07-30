

import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from models import engine, Base, Session, User, Post
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_users(db: AsyncSession, users_data):
    for user in users_data:
        db_user = User(
            name=user['name'],
            username=user['username'],
            email=user['email']
        )
        db.add(db_user)
    await db.commit()


async def add_posts(db: AsyncSession, posts_data):
    for post in posts_data:
        db_post = Post(
            user_id=post['userId'],
            title=post['title'],
            body=post['body']
        )
        db.add(db_post)
    await db.commit()


async def async_main():
    async with Session() as session:
        await init_db()

        users_data, posts_data = await asyncio.gather(
            fetch_users_data(),
            fetch_posts_data()
        )

        await add_users(session, users_data)
        await add_posts(session, posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
