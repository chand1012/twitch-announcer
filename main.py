import os
import time

import twitch
import dotenv
from icecream import ic

from hashtags import get_hashtags, append_hashtag
from discord_hook import send_hook as discord_hook

dotenv.load_dotenv()

# set to 10 for faster debugging
# make this an environment variable at some point
WAIT = 10 #60 

STREAMER = 'dogdog' #os.getenv('TWITCH_USERNAME')

twitch_client = twitch.Helix(client_id=os.getenv('TWITCH_CLIENT_KEY'), client_secret=os.getenv('TWITCH_CLIENT_SECRET'))

isLive = False

while True:
    hashtags = get_hashtags(filename='hashtags.json')

    twitter_hashtags = ''

    streamer = twitch_client.user(STREAMER)

    currentlyLive = streamer.is_live

    if currentlyLive and not isLive:
        
        isLive = True
        title = streamer.stream.title
        game_id = streamer.stream.game_id
        thumbnail = streamer.stream.thumbnail_url.replace('{width}', '1280').replace('{height}', '720')
        avatar = streamer.profile_image_url
        url = 'https://twitch.tv/' + streamer.login
        if game_id in hashtags:
            twitter_hashtags = hashtags.get(game_id)
        else:
            game = twitch_client.game(id=game_id)
            twitter_hashtags = append_hashtag(game_id, game_name=game.name)
        
        # post to discord, twitter, facebook
        discord_hook(url,thumbnail, title, STREAMER, avatar, '9147FF')

    if not currentlyLive and isLive:
        isLive = False

        # add the option to make a post thanking people for watching?

    time.sleep(WAIT)