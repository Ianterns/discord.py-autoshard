import discord

from discord.ext.commands import AutoShardedBot, when_mentioned_or
from discord import Game

client = AutoShardedBot(
    command_prefix=when_mentioned_or(
        '!'
    ), 
    shard_count=5,
    activity=Game(
        type=discord.ActivityType.playing,
        name="council#2078"
    )
)


client.run(token)
