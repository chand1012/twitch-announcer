import os
import json
import re

from twitch import Helix
import dotenv

from hashtags import get_hashtags, set_hashtags

dotenv.load_dotenv()

# add all the games you play here and run the script
# their names can be found on their twitch pages
games = [
    'Battlefield 4',
    'Halo: The Master Chief Collection',
    "Tom Clancy's Rainbow Six Siege", 'Overwatch',
    'Minecraft',
    'Call of Duty: Black Ops Cold War',
    'Battlefield 1',
    'Insurgency: Sandstorm',
    'Onward',
    'Pavlov VR',
    'Hot Dogs, Horseshoes & Hand Grenades'
]

# the .env file must exists and have the client key and secret populated for this to work.
twitch = Helix(client_id=os.getenv('TWITCH_CLIENT_ID'),
               client_secret=os.getenv('TWITCH_CLIENT_SECRET'))

data = get_hashtags('hashtags.json')

for game_name in games:
    game = twitch.game(name=game_name)

    if game is None:
        print(f'Could not find game for {game_name}, skipping...')
        continue

    # this is so that repeats get skipped
    if game.id in data:
        continue

    default = re.sub(r'[^A-Za-z0-9]+', '', game.name)
    # add any additional hashtags that you want on all
    # games after {default}
    # add any hashtag per-game to 'hashtags.json'
    data[game.id] = f'#{default} '

set_hashtags(data, 'hashtags.json')
