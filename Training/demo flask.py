import flask

app = flask.Flask(__name__)


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



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
