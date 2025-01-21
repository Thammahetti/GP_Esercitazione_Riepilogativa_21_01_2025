from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required,current_user
from flask_bcrypt import Bcrypt
from models import db
app = Flask(__name__)
app.secret_key = 'key_sessione_user' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
bcrypt = Bcrypt(app)


db.init_app(app)
login_manager = LoginManager() 
login_manager.init_app(app) 
login_manager.login_view = 'login'
@login_manager.user_loader


def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET','POST'])
def login():
   return render_template('Login.html', error=None)

if __name__ == '__main__': 
    app.run(debug=True)
