import os
import time

import dotenv
import requests
import tweepy
import twitch

from instabot import Bot

import twitter
from discord_hook import send_hook as discord_hook
from hashtags import append_hashtag, get_hashtags

print('Initializing....')

dotenv.load_dotenv()

# set to 10 for faster debugging
# make this an environment variable at some point
WAIT = 60*3

STREAMER = os.getenv('TWITCH_USERNAME')

isLive = False

print('Waiting...')

while True:
    hashtags = get_hashtags(filename='hashtags.json')

    twitter_hashtags = ''

    try:
        twitch_client = twitch.Helix(client_id=os.getenv(
            'TWITCH_CLIENT_ID'), client_secret=os.getenv('TWITCH_CLIENT_SECRET'))
        streamer = twitch_client.user(STREAMER)
    except requests.exceptions.HTTPError:
        print('There was an error. Waiting and retrying...')
        time.sleep(WAIT)
        continue

    currentlyLive = streamer.is_live

    if currentlyLive and not isLive:
        print(f'{STREAMER} is online!')
        print('Gathering data....')
        isLive = True
        title = streamer.stream.title
        game_id = streamer.stream.game_id
        thumbnail = streamer.stream.thumbnail_url.replace(
            '{width}', '1280').replace('{height}', '720')
        avatar = streamer.profile_image_url
        url = 'https://twitch.tv/' + streamer.login
        if game_id in hashtags:
            twitter_hashtags = hashtags.get(game_id)
        else:
            game = twitch_client.game(id=game_id)
            twitter_hashtags = append_hashtag(game_id, game_name=game.name)

        # post to discord & twitter
        if os.getenv('DISCORD_WEBHOOK_URL'):
            print("Posting to Discord....")
            while True:
                try:
                    discord_hook(url, thumbnail, title,
                                 STREAMER, avatar, '9147FF')
                except requests.exceptions.HTTPError:
                    print(
                        'There was an error trying to post to discord, waiting and retrying...')
                    time.sleep(60)
                    continue
                break
        print("Posting to Twitter....")
        try:
            twitter.make_post(title, url, twitter_hashtags)
        except tweepy.error.TweepError:
            print('Duplicate tweet, skipping.')

        # post to instagram
        if os.getenv('INSTAGRAM_USERNAME') and os.getenv('INSTAGRAM_PASSWORD'):
            try:
                bot = Bot()
                bot.login(username=os.getenv('INSTAGRAM_USERNAME'),password=os.getenv('INSTAGRAM_PASSWORD'))
                twitch_username = os.getenv("TWITCH_USERNAME");
                bot.upload_photo("img.jpg", caption=F"If you see this I am live right now! https://www.twitch.tv/{twitch_username}")

            except:
                print("instapost did not work")


    if not currentlyLive and isLive:
        isLive = False

    time.sleep(WAIT)
