from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return '''
    Hello World!
    <ul>
    <li><a href="/hello/">Hello</a></li>
    <li><a href="/addition/">Addition</a></li>
    <li><a href="/subtraction/">Subtraction</a></li>
    <li><a href="/multiplication/">Multiplication</a></li>
    <li><a href="/division/">Division</a></li>
    </ul>
    '''


@app.route('/hello/')
def hello_setup():
    return '''
    <p>
    Hello!
    <br>
    Put you name behind for personalized reply!
    </p>
    '''


@app.route('/hello/<name>/')
def hello(name):
    return 'Hello ' + name.title() + '!'


@app.route('/addition/')
def add_setup():
    return '''
    <p>
    Put a number then put ' / ' and another number for addition!
    <br>
    Will return first number plus second.
    </p>
    '''


@app.route('/addition/<a>/<b>/')
def add(a, b):
    a = float(a)
    b = float(b)
    c = a + b
    c = str(c)
    return c


@app.route('/subtraction/')
def minus_setup():
    return '''
    <p>
    Put a number then put ' / ' and another number for subtraction!
    <br>
    Note: Will return first number minus the second.
    </p>
    '''


@app.route('/subtraction/<a>/<b>/')
def minus(a, b):
    a = float(a)
    b = float(b)
    c = a - b
    c = str(c)
    return c


@app.route('/multiplication/')
def times_setup():
    return '''
    <p>
    Put a number then put ' / ' and another number for multiplication!
    <br>
    Note: Will return first number times the second.
    </p>
    '''


@app.route('/multiplication/<a>/<b>/')
def times(a, b):
    a = float(a)
    b = float(b)
    c = a * b
    c = str(c)
    return c


@app.route('/division/')
def divide_setup():
    return '''
    <p>
    Put a number then put ' / ' and another number for division!
    <br>
    Note: Will return first number divided by the second.
    </p>
    '''


@app.route('/division/<a>/<b>/')
def divide(a, b):
    a = float(a)
    b = float(b)
    c = a / b
    c = str(c)
    return c


@app.route('/admin/')
def admin_page():
    return '''
    Hi if you are not admin, have fun!
    Type: username/password
    '''

#
# @app.route('/admin/<name>/<password>')
# def login_admin(name, password):
#     admins = {'yanganyi': 'Yay20071201', 'admin': 'admin'}
#     if admins.get('1') != None:
# #   TO-DO:
# #   check password

if __name__ == '__main__':
    app.run(debug=True)
