import os

from discord_webhook import DiscordWebhook, DiscordEmbed

def send_hook(url, thumbnail_url, title, username, author_image, color):
    webhook = DiscordWebhook(url=os.getenv('DISCORD_WEBHOOK_URL'))

    embed = DiscordEmbed(title=f'{username} just went live!', description=title, color=color)
    embed.set_url(url)
    embed.set_author(name=username, url=url, icon_url=author_image)
    embed.set_image(url=thumbnail_url)

    webhook.add_embed(embed)

    resp = webhook.execute()

    return resp