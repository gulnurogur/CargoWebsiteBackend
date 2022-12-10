import os

from dotenv import load_dotenv
from flask import Flask

from db.baglanti import db, migrate

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")

db.init_app(app)
migrate.init_app(app, db)

if __name__ == '__main__':
    app.run()
