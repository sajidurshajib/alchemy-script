from sqlalchemy.sql.functions import user
from main import User, engine, Session

local_session = Session(bind=engine)

user_to_delete = local_session.query(User).filter(User.id == 2).first()

local_session.delete(user_to_delete)

local_session.commit()
