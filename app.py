from flask import Flask, render_template, request, session
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rahul@localhost:3307/loginpage'
db = SQLAlchemy(app)
app.config.from_object(__name__)
mysql = MySQL(app)


class Login(db.Model):
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    id = db.Column(db.Integer, primary_key=True)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        record = Login.query.filter_by(username=name, password=password).all()
        if len(record) > 1:
            return render_template('welcome.html')
        else:
            return render_template('login.html')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
