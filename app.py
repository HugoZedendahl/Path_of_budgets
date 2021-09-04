import base64
import urllib.request
import json
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = open("assets/mongo.txt", "r").read()
mongo = PyMongo(app)
db = mongo.db


@app.route("/store_build")
def store_build(runtime_item_set, build_id):
    run_dict = {}
    for item in runtime_item_set:
        item_bytes = item.encode('ascii')
        base64_bytes = base64.b64encode(item_bytes)
        base64_output = base64_bytes.decode('ascii')
        https_get_url = "https://www.poeprices.info/api?l=Expedition&i="
        https_get_call = https_get_url + base64_output
        response = urllib.request.urlopen(https_get_call)
        price = json.load(response)
        run_dict.update({item: price})
    db.builds.pob_data.set_one({"_id": build_id})
    db.builds.pob_data.update_one({"_id": build_id}, {"$set": run_dict})
    return "build added"


@app.route("/Edit_build")
def Edit_build(runtime_item_set, build_id):
    run_dict = {}
    for item in runtime_item_set:
        item_bytes = item.encode('ascii')
        base64_bytes = base64.b64encode(item_bytes)
        base64_output = base64_bytes.decode('ascii')
        https_get_url = "https://www.poeprices.info/api?l=Expedition&i="
        https_get_call = https_get_url + base64_output
        response = urllib.request.urlopen(https_get_call)
        price = json.load(response)
        run_dict.update({item: price})
    db.builds.pob_data.update_one({"_id": build_id}, {"$set": run_dict})
    return "build updated"


@app.route("/fetch_build")
def fetch_build(build_id):
    build = db.builds.pob_data.find_one({"_id": build_id})
    return build


@app.route("delete_build")
def delete_build(build_id):
    delete = db.builds.pob_data.delete_one({"_id": build_id})
    return delete


# sumbission needs to go
# grab item info and build id -> encode base 64 -> poeprices api ->
# store in db item info + price + build id
# any other return is a error, no information available or a timeout
# 
# database should be reset on every in  game leauge
# (approximatly every 3 months)
# this needs to be done manually
# "hambogbbrr" is the abbreviation for the item order
# helm amulet mainhand body offhand ring1 belt ring2
