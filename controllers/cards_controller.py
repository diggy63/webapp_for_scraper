from flask import request, jsonify
import re

from extentions.config import db


def get_all():
    cards = list(db.cards.find())
    for card in cards:
        card["_id"] = str(card["_id"])
    return {"data":cards}

def get_one(name):
    print(name)
    cards = db.cards
    result = cards.find({"name": {"$regex": f".*{name}.*"}})
    ret = []
    for find in result:
        ret.append(find)
    return {"data":ret}


