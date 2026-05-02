from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# engine = create_engine('sqlite:///mydatabase.db', echo=True)
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/satutorialdatabase', echo=True)

meta = MetaData()

people = Table(
    "people",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer)
)

meta.create_all(engine)
