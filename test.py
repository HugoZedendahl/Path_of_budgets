import base64
import urllib.request
import json
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = open("assets/mongo.txt", "r").read()
mongo = PyMongo(app)
db = mongo.db

helm = open("assets/sample_items/helm.txt").read()
amulet = open("assets/sample_items/amulet.txt").read()
mainhand = open("assets/sample_items/main_hand.txt").read()
offhand = open("assets/sample_items/off_hand.txt").read()
boots = open("assets/sample_items/boots.txt").read()
gloves = open("assets/sample_items/gloves.txt").read()
belt = open("assets/sample_items/belt.txt").read()

runtime_item_set = [helm, boots, mainhand, offhand, gloves, belt, boots]
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
db.builds.pob_data.update_one({"_id": "aura_stacccc"}, {"$set": run_dict})
print("it worked")
