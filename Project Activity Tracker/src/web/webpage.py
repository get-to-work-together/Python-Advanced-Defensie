from ..data_store.as_sqlite import retrieve_repository
from ..models.activity import field_names

from flask import Flask, render_template, request, redirect, Response, make_response, jsonify

app = Flask(__name__,
            template_folder = 'templates',
            static_url_path = '',
            static_folder = 'static')


@app.route("/")
def home():
    return 'Hallo web user!'


@app.route("/users")
def user():
    name = request.args.get('name')         # from querystring
    return f'User page for ... {name}'


@app.route("/users/<name>")
def get_user_by_name(name:str):             # url parameter
    payload = f'User page for ... {name}'
    return Response(payload, status = 200)


@app.route("/activities", methods=['GET'])
def get_activities():
    repository = retrieve_repository()
    activities = repository.to_json()
    return render_template('activities.html', status = 200, activities = activities, field_names = field_names)


@app.route("/activities", methods=['PUT'])
def update_activities():
    repository = retrieve_repository()
    activities = repository.to_json()
    return render_template('activities.html', status = 200, activities = activities, field_names = field_names)


@app.route("/activities", methods=['DELETE'])
def delete_activities():
    repository = retrieve_repository()
    activities = repository.to_json()
    return render_template('activities.html', status = 200, activities = activities, field_names = field_names)


@app.route("/api/v1.0/activities", methods=['GET'])
def get_activities_as_json():
    repository = retrieve_repository()
    activities = repository.to_json()
    return jsonify({'activities': activities}), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

