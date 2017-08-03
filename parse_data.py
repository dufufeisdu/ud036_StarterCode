import json


def parse_json_data():
    """
    A utility funciton to parse JSON file
    """
    with open('data.json') as data_file:
        data = json.load(data_file)
        return data["data"]
