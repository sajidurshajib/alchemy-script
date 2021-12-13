from main import User, engine, Session

local_session = Session(bind=engine)

all_users = local_session.query(User).all()


for user in all_users:
    print(f"User - {user.name} > {user.alter}")
