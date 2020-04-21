import os
import discord
from dotenv import load_dotenv
import asyncio
from youtube_search import YoutubeSearch

load_dotenv()

token = os.getenv('Discord_Token')
guildx = os.getenv('Discord_Guild')
bot = commands.Bot(command_prefix = '<')
client = discord.Client()

@bot.command(name='play')
async def play(ctx, search_query):
    results = 

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=guildx)
    
    print(
        F'{client.user} has connected to the following Discord server:\n'
        F'{guild.name} (id: {guild.id})'
        )

client.run(token)
