from flask import Flask
from flask import request

app = Flask('some_name')


@app.route('/')
def hello_world():
    return '<b><a href="http://www.google.com">Hello, world!</a></b>'


@app.route('/name')
def fullname():
    surname = request.args.get('surname')
    given_name = request.args.get('givenname')
    return 'Hello, ' + surname + ' ' + given_name + '!'






app.run()