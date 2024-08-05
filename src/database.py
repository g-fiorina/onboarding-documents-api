import os
from dotenv import load_dotenv
from peewee import PostgresqlDatabase, Model, CharField, TextField

load_dotenv()

db = PostgresqlDatabase(
    os.getenv("DATABASE_NAME"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    port=int(os.getenv("DATABASE_PORT")),
)


class Document(Model):
    title = CharField(max_length=255, null=False)
    content = TextField(null=False)
    url = CharField(max_length=2048, unique=True, null=False)

    class Meta:
        database = db
        table_name = "document"


def initialize_database():
    with db.connection_context():
        db.create_tables([Document])
