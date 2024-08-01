import json
from peewee import PostgresqlDatabase, Model, CharField, TextField

with open("config/config.json") as f:
    config = json.load(f)
    DATABASE = config["DATABASE"]

with open("config/secrets.json") as f:
    secrets = json.load(f)
    DATABASE["password"] = secrets["DATABASE_PASSWORD"]

db = PostgresqlDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    password=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)


class Document(Model):
    title = CharField(max_length=255, null=False)
    content = TextField(null=False)

    class Meta:
        database = db
        table_name = "documents"


def initialize_database():
    db.connect()
    db.create_tables([Document])
