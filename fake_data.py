from datetime import datetime
from faker import Faker
from models import Base, Comment, Post
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from database import create_all_tables, get_async_session

fake = Faker()


def create_random_posts():
    Session = sessionmaker(bind=engine)
    session = Session()
    for _ in range(10):
        post = Post(publication_date=datetime.now(), title=fake.sentence(), content=fake.paragraph())
        session.add(post)
    session.commit()


def create_random_comments():
    Session = sessionmaker(bind=engine)
    session = Session()
    for _ in range(20):
        post = session.query(Post).order_by(func.random()).first()
        comment = Comment(post=post, publication_date=datetime.now(), content=fake.paragraph())
        session.add(comment)
    session.commit()


def main():
    create_random_posts()
    create_random_comments()


if __name__ == "__main__":
    DATABASE_URL = "sqlite:///sqlalchemy.db"
    engine = create_engine(DATABASE_URL)
    main()
