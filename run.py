import os
import base64
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)


def encode_item_info(self, item_info):
    if (isinstance(item_info, str)):
        base64_item_output = base64.b64encode(item_info)
        return base64_item_output
    else:
        return("Invalid data")


def store_item_set(self, item_set, item_set_id):
    runtime_item_set = {}
    for item in item_set:
        runtime_item_set.update = {}
    return()


def fetch_item_set(self, data_set_id):
    return()


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
