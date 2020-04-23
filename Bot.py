import os
import discord
import random
from dotenv import load_dotenv
import asyncio
from youtube_search.yt import YT
from discord.ext import commands

load_dotenv()

token = os.getenv('Discord_Token')
guildx = os.getenv('Discord_Guild')
bot = commands.Bot(command_prefix = '!')
client = discord.Client()

@bot.command(name='play')
async def play(ctx, *args):
    seperator = ' '
    search_query = seperator.join(args)
    results = YT(search_query, max_results = 5).export()
    output = '''1. {name1} \n 2. {name2} \n 3. {name3} \n 4. {name4} \n 5. {name5}\
    '''.format(name1=results[0][0], name2=results[1][0], name3=results[2][0], name4=results[3][0], name5=results[4][0])
    await ctx.send(output)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(token)
