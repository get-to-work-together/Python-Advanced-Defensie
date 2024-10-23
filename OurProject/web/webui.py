from flask import Flask, request, render_template

from database.db_sqlite import get_users, get_user

def main():
    app = Flask(__name__,
                template_folder='templates')


    @app.route('/')
    def home():
        html = '<h1>Home</h1>'
        return html


    @app.route('/users')
    def users():
        users = get_users()
        return render_template('users.html', title='Users', users=users)


    @app.route('/users/<id>')
    def user(id):
        user = get_user(id)
        return render_template('user.html', title='Users', user=user)


    app.run()
