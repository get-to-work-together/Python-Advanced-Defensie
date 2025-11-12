from flask import Flask, render_template, request

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


app.run()
