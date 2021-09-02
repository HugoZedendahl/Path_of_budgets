import os
import base64
import urllib.request
import json
from pymongo import MongoClient
from flask import Flask

mongo_url = open("assets/mongo.txt")
client = pymongo.MongoClient(mongo_url)
db = client.test

app = Flask(__name__)


@app.route("/")
def index():
    return "started"


@app.route('/edit_build.html')
def edit_build():
    return "edit"


@app.route("/build_selector.html")
def select_build():
    return "started"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)


def encode_item_info(item_info, item_id, build_id):
    if (isinstance(item_info, item_id, build_id, str)):
        base64_item_output = base64.b64encode(item_info)
        https_get_url = "https://www.poeprices.info/api?l=Expedition&i="
        https_get_call = https_get_url + base64_item_output
        response = urllib.request.urlopen(https_get_call)
        price = json.load(response)
        db.builds.update_one({'_id': build_id}, {item_id: {item_info: price}})
        return
    else:
        return("Invalid data")


# sumbission needs to go
# grab item info -> encode base 64 -> obfuscate -> poeprices api ->
# obfuscate- > return -> return info will come out after as "number currency"
# any other return is a error, no information available or a timeout
# number is a float, currency is either "chaos orb" or "exalted orb"
# on return of every item needs to be assigned
# {itemtype:[base64encodedinfo, price info]}
# all items should be stored in a list together with a uniqe id in the database
# database should be reset on every in  game leauge
# (approximatly every 3 months)
