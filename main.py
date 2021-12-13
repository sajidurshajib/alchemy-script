from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

connection = "mysql+pymysql://root:@localhost:3306/alchemy"

Base = declarative_base()

engine = create_engine(connection, echo=True)

Session = sessionmaker()


class User(Base):
    __tablename__ = "ninja"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    alter = Column(String(80), nullable=False)


# new_user = User(name="Sajidur", alter="Lol")
# print(new_user)
