from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_fontawesome import FontAwesome

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'ca5ceda1d0fe49f2f384944f'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
fa = FontAwesome(app)
login_manager = LoginManager(app)
from market import routes