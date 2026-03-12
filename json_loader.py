import json

def read_js(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data

