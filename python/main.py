import discord
import os
import json
from discord.ext import commands, tasks
from itertools import cycle
rekt = 989402899660558376

TOKEN1 = 'OTg5NDA5NDM5OTU2MjEzODMw.GW_ISE.n6ioWz_sKL0kEg-QGbm7Sfi8JddGf-vW7qFmsM'

games = cycle(['Minecraft', 'Hytale', 'Half-Life 3', 'Tetris', 'Roblox'])

class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='e!',
            intents = discord.Intents.all(),
            application_id=989409439956213830
        )

    async def setup_hook(self):
        await client.load_extension(f'commands.anime_commands.waifu_commands')
        await client.load_extension(f'commands.anime_commands.mal_commands')


    async def on_ready(self):
        gameschange.start()
        print('I AM LOGGED IN!')



@tasks.loop(seconds=300)
async def gameschange():
    await client.change_presence(activity=discord.Game(next(games)))

def is_it_me(ctx):  # Comandos que só eu posso usar
    return ctx.author.id == 325049357063815176

client=MyBot()
client.run(TOKEN1)