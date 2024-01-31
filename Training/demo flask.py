import flask

app = flask.Flask(__name__,
                  template_folder='templates',
                  static_url_path='',
                  static_folder='static')


@app.route('/')
def home():
    return 'Home page of our website'

@app.route('/info', methods=['get'])
def info():
    html = """\
    <h1>Information about our website.</h1>
    <p>Work in progress.</p>
    """
    return html

@app.route('/hello/<name>', methods=['get'])
def hello(name):
    return f'<h1>Hallo {name}!</h1>'

@app.route('/hello/<name>', methods=['delete'])
def delete(name):
    return f'<h1>DELETING RESOURCE {name}!</h1>'

@app.route('/names', methods=['get'])
def get_names():
    return f'''\
    <form method="post">
        <input type="text" name="name">
        <input type="submit">
    </form>
    '''
@app.route('/names', methods=['post'])
def add_name():
    name = flask.request.form['name']
    return f'<h1>ADDING RESOURCE {name}!</h1>'

@app.route('/index', methods=['get'])
def index():
    name = flask.request.args.get('name', 'unknown')
    return flask.render_template('index.html', name = name)

@app.route('/list')
def list_of_names():
    names = ['Gert','Jan','Timo','Bernd','Maarten','Maurice','Wesley','Lloyd','Egbert','Vincent']
    return flask.render_template('list.html', names = names)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
