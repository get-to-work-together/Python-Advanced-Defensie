from flask import Flask, render_template, request

from src.models.scrabble_helper import get_matches


def main():

    app = Flask(__name__)

    @app.route('/')
    def home():
        return '<h1>HOME</h1>'


    @app.route('/hello')
    def hello():
        return """\
    <html>
    <head>
        <title>Scrabble Helper</title>
    </head>
    <body>
        <h1>Hello world!!!</h1>
    </body>
    </html>
    """


    @app.route('/base')
    def base():
        return render_template('base.html')


    @app.route('/content')
    def content():
        name = request.args.get('name')
        return render_template('content.html', name=name)


    @app.route('/scrabble_helper', methods=['GET', 'POST'])
    def scrabble_helper():

        words = []
        if request.method == 'POST':
            if request.form['regex']:
                regex = '^' + request.form['regex'] + '$'
            else:
                regex = '.*'
            letters = request.form['letters']

            words = get_matches(regex, letters)

        return render_template('scrabble_helper.html', words=words)


    app.run()


if __name__ == '__main__':
    main()
