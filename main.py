import os
import time

import twitch
import dotenv
from icecream import ic

dotenv.load_dotenv()

WAIT = 60

STREAMER = 'newblood' #os.getenv('TWITCH_USERNAME')

twitch_client = twitch.Helix(client_id=os.getenv('TWITCH_CLIENT_KEY'), client_secret=os.getenv('TWITCH_CLIENT_SECRET'))

isLive = False

while True:

    streamer = twitch_client.user(STREAMER)

    currentlyLive = streamer.is_live

    if currentlyLive and not isLive:
        isLive = True
        title = streamer.stream.title
        game_id = streamer.stream.game_id
        game = twitch_client.game(name="Battlefield 4")
        game_title = game.name
        ic(isLive)
        ic(title)
        ic(game_id)
        ic(game)
        ic(game_title)
        # get more info

    break

    #time.sleep(WAIT)