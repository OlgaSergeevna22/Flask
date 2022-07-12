from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'About me'


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page: ' + name + ' - ' + str(id)


@app.route('/homework/<day>/<data>')
def homework(day, data):
    return 'My homework:' + day + ' - ' + data


if __name__ == '__main__':
    app.run(debug=True)
