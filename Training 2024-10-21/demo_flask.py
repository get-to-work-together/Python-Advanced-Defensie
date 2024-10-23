from flask import Flask, request, render_template

app = Flask(__name__,
            template_folder='templates')



@app.route('/')
def home():
    html = '''\
<html>
<head>
    <title>My Web Page</title>
</head>
<body>
    <h1>Welkom home ...</h1>
</body>
</html>'''
    return html



@app.route('/hello')
def hello_with_name():
    name = request.args.get('name')   # from querystring
    if name:
        return f'<h1>Hello {name}!</h1>'
    else:
        return f'<h1>Hello!</h1>'



@app.route('/template')
def template():
    return render_template('message.html', title='KOFFIE', message='Bijna koffie!!!')



app.run()
