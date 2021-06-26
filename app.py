import os

import discord

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


client.run(TOKEN)  # bot token, needs to always be last line of code
