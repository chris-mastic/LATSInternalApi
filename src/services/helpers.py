import json

def create_json_object(**kwargs) -> object:
    return json.dumps({key: value for key, value in kwargs.items()})
