from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    insert,
    select,
    update,
    delete,
)

engine = create_engine('sqlite:///mydatabase.db', echo=True)

meta = MetaData()

people = Table(
    "people",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer)
)

meta.create_all(engine)


with engine.begin() as conn:
    conn.execute(delete(people))

    conn.execute(
        insert(people),
        [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 40},
        ],
    )

with engine.connect() as conn:
    print("\n--- Todas las personas ---")
    for row in conn.execute(select(people)):
        print(row)

    print("\n--- Personas mayores de 28 ---")
    stmt = select(people).where(people.c.age > 28).order_by(people.c.age)
    for row in conn.execute(stmt):
        print(row)

with engine.begin() as conn:
    conn.execute(
        update(people).where(people.c.name == "Bob").values(age=26)
    )

    conn.execute(delete(people).where(people.c.name == "Charlie"))

with engine.connect() as conn:
    print("\n--- Estado final ---")
    for row in conn.execute(select(people)):
        print(row)
