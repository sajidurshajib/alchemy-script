from main import User, engine, Session

local_session = Session(bind=engine)

new_user = User(name="Shajib", alter="Boom")

local_session.add(new_user)
local_session.commit()
