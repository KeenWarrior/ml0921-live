from flask import Flask, request, render_template
import json
from pyfacebook import GraphAPI
import requests


app = Flask("myappname")

token = "EAAIh4a0LDFsBAGZB00wBpwEWaDlsTwKc2R8LpQunwEW4AHud6oibs1XKWHYj95fgJCZCn2DbuhqKm0XcWn7WvTtX97xJ7sbvcHLZCSaKA2hSc04wsxHd3hoUD5MkjEg4G4swdbhkXAvsFo5jlB4IE9aEMioSsuw6qDK14jfs6RtzZB6oVUap"

url = "https://graph.facebook.com/v12.0/me/messages?access_token="+token
api = GraphAPI(access_token="token")


@app.route("/verify", methods=["GET"])
def verify():
    print(request.args)
    if "hub.challenge" in request.args:
        return request.args.get("hub.challenge")
    return "error"


@app.route("/verify", methods=["POST"])
def hook():

    data = request.json

    if "entry" in data:
        entries = data.get("entry")
        for entry in entries:
            if "messaging" in entry:
                messaging_list = entry.get("messaging")
                for messaging in messaging_list:
                    data = response(messaging.get("sender").get("id"))
                    print(data)
                    requests.post(url, json.dumps(data))

    return "ok"


def response(recipient):
    data = {
        "recipient": {
            "id": recipient
        },
        "message": {
            "text": "hello, world!"
        }
    }

    return data

app.run()