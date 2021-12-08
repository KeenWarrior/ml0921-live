from flask import Flask, request, render_template
import json

app = Flask("myappname")

users = ["anuj", "vasu", "mahima", "shlok"]

@app.route("/")
def hello_world():
    return 'Hello from Code for Cause!'




@app.route("/users/<user>")
def hello_users(user):
    print(user)
    return json.dumps(users)


@app.route("/search")
def search():
    print(request.args.get("q"))
    return request.args.get("q")

@app.route("/temp")
def rederer():
    return render_template("hello.html", users=users)


app.run()