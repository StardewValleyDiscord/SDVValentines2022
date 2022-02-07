# Valentine
# Discord bot made for the Valentine's Day 2022 SDV event
# aquova, 2022

import discord
import config
from commonbot.utils import check_roles

class Cupid:
    def __init__(self):
        self.roles = []

    def initialize_roles(self, client):
        server = client.guilds[0]
        for role_id in config.AWARDED_ROLES:
            role = discord.utils.get(server.roles, id=role_id)
            self.roles.append(role)

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
cupid = Cupid()

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    cupid.initialize_roles(client)

@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == config.SUBMIT_CHANNEL and check_roles(payload.member, config.MOD_ROLES):
        server = client.guilds[0]
        channel = discord.utils.get(server.channels, id=payload.channel_id)
        user = discord.utils.get(server.members, id=payload.user_id)
        if not user:
            return

        await user.add_roles(*cupid.roles)
        message = await channel.fetch_message(payload.message_id)
        await message.add_reaction(payload.emoji)

client.run(config.DISCORD_KEY)
