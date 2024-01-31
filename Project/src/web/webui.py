import flask

app = flask.Flask(__name__,
                  template_folder='templates',
                  static_url_path='',
                  static_folder='static')


@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/list')
def applications_list():
    applications = [('Kibana', 7, 19, None),
                    ('Confluence', 17, 1, 23)]
    return flask.render_template('list.html', applications = applications)


def start_webui():
    app.run(host='0.0.0.0', port=8080, debug=True)
