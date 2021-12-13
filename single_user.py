from main import User, engine, Session

local_session = Session(bind=engine)

# jona = local_session.query(User).filter(User.username == "jona").first()

single_user = local_session.query(User).filter(User.id == 2).first()

print(f"{single_user.name} -> {single_user.alter}")

# for user in single_user:
#     print(f"User - {user.name} > {user.alter}")
