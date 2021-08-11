import json
import os
import re


def get_hashtags(filename='hashtags.json'):
    data = {}
    if os.path.exists(filename):
        with open(filename) as f:
            data = json.loads(f.read())
    return data


def set_hashtags(data, filename='hashtags.json'):
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=4))


def append_hashtag(game_id, tags=None, game_name=None, filename='hashtags.json'):
    data = get_hashtags(filename=filename)
    if tags is None and not game_name is None:
        tags = '#' + re.sub(r'[^A-Za-z0-9]+', '', game_name)
    data[game_id] = tags or ''
    set_hashtags(data, filename=filename)
    return data[game_id]
