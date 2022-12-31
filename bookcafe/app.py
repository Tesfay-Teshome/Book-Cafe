from flask import Flask
from flask import render_template, request
from .extentions import db, migrate,ma
from . import db, ma
from .api.api import api
from .api.view import view
from .api.auth import auth
from bookcafe.model.users import User
from flask_login import LoginManager

app = Flask(__name__)
@app.route('/login')
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)