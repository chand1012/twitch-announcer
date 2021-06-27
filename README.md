# twitch-announcer
Announce your Twitch stream to Twitter, Facebook, and Discord intelligently!

## To Do
- Get Facebook posts working
- Get Twitter posts working
- Get Discord Webhooks working
- Generate interesting titles using the game, my title, and a few hashtags.
- Watch the stream until it goes live.
    - When it goes live, set `live` to true and wait.
    - Will continue checking to see the state, will not do anything if live.
    - When the stream goes offline set `live` to false. 