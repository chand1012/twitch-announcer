# twitch-announcer
Announce your Twitch stream to Twitter, and Discord intelligently!

## Usage

### Requirements

This requires you have Docker installed at minimum. Python 3.8 with virtualenv is preffered but not required. This guide assumes you are running this program on a Unix based system or Windows Subsystem for Linux.

### Getting the Code

First, clone the repo. A [Docker Hub build](https://hub.docker.com/r/chand1012/twitch-announcer) does exist but it is not complete.

```bash
git clone https://github.com/chand1012/twitch-announcer
cd twitch-announcer
```

### Creating an environment file

Next, copy the [`example.env`](./example.env) and populate the proper `.env` file.

- See [here](https://www.streamweasels.com/support/how-to-setup-a-client-id-and-client-secret/) on how to get a Twitch Client ID and Secret.
- See [here](https://realpython.com/twitter-bot-python-tweepy/#creating-twitter-api-authentication-credentials) on how to get your Twitter credentials. 
- See [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) on setting up a Discord webhook.

```bash
cp example.env .env
# then open up .env in your favorite editor
# for this example we will use nano
nano .env
```

### **OPTIONAL:** Populate your Hashtags

This section required the optional dependencies of Python 3 and virtualenv. Here is how you would install it on Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-dev python3-pip python3-venv
```

You can do this by running the script [`generate_hashtags_table.py`](./generate_hashtags_table.py). Open up the file in your favorite editor and edit the list called `games` to add the FULL TITLE of the games you want to add. This is the title of the game as it is found on the Twitch game page. After this is finished, install the virtual environment along with the required packages and run the script.

```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python generate_hashtag_table.py
```

This should populate your [`hashtags.json`](./hashtags.json) with all the games that you play. Go down the list and add any additional hashtags you want for each game.

### Building and Running the Docker Container

Build the container.

```bash
docker build -t twitch-announcer:latest .
```

Wait for the build to finish.

Finally, run the container. 

```bash
docker run --name "Twitch Announcer" --env-file .env --restart="always" twitch-announcer:latest
```

And that's it!