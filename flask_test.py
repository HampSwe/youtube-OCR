from flask import Flask, abort
from markupsafe import escape

# https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3
# https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application
# https://www.digitalocean.com/community/tutorial_series/how-to-build-a-website-with-html


app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


@app.route("/about/")
def about():
    return "<h1>Detta är en enkel hemsida</h1>"

@app.route("/capitalize/<word>/")
def capitalize(word):
    return "<h1>{}</h1>".format(escape(word.capitalize()))

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)


@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
