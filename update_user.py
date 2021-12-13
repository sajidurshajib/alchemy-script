from main import User, engine, Session

local_session = Session(bind=engine)

user_to_update = local_session.query(User).filter(User.id == 2).first()

user_to_update.name = "Jonathan"
user_to_update.alter = "rambo"

local_session.commit()
