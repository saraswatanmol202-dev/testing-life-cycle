# Epic Title: Implement Secure Login Mechanism

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from backend.authentication.mfa import mfa_blueprint
from backend.views.login import login_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/banking'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'username'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
mail = Mail(app)

app.register_blueprint(mfa_blueprint)
app.register_blueprint(login_blueprint)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)