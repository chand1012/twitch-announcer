import os
import time

import twitch
import dotenv

dotenv.load_dotenv()

WAIT = 60

STREAMER = os.getenv('TWITCH_USERNAME')

twitch_client = twitch.Helix(client_id=os.getenv('TWITCH_CLIENT_KEY'), client_secret=os.getenv('TWITCH_CLIENT_SECRET'))

isLive = False

while True:

    streamer = twitch_client.user(STREAMER)

    currentlyLive = streamer.is_live

    if currentlyLive and not isLive:
        # do things
        pass

    time.sleep(WAIT)