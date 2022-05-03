from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key='f23e372d-d86c-478b-9735-b1265370675f'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import routes, models