from sqlalchemy import create_engine

engine = create_engine(
    'mysql+mysqlconnector://andre:rsp@localhost/sistemadeva', echo=True)

engine.connect()
print(engine)
