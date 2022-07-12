from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullabel=False)
    intro = db.Column(db.String(300), nullabel=False)
    text = db.Column(db.Text, nullabel=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r' %self.id

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page: ' + name + ' - ' + str(id)


@app.route('/homework')
def homework():
    return render_template('home_page.html')


if __name__ == '__main__':
    app.run(debug=True)
