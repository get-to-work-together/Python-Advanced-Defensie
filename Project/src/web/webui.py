import flask
from Project.src.database import persistence


app = flask.Flask(__name__,
                  template_folder='templates',
                  static_url_path='',
                  static_folder='static')


@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/list')
def applications_list():
    applications = persistence.get_all_application_records()
    return flask.render_template('list.html', applications = applications)


def start_webui():
    app.run(host='0.0.0.0', port=8080, debug=True)
