import os
import discord
import random
import asyncio
import youtube_dl
from dotenv import load_dotenv
from youtube_search.yt import YT
from youtube_search.yt import YTDLSource
from discord.ext import commands

load_dotenv()

token = os.getenv('Discord_Token')
guildx = os.getenv('Discord_Guild')
bot = commands.Bot(command_prefix = '!')
client = discord.Client()

resultsx = []
players = {}

@bot.command(name='play')
async def play(ctx, *args):
    if ctx.message.author.voice == None:
        await ctx.send('Join a voice channel before using this command.')
    else:     
        user_channel = ctx.message.author.voice.channel
        if args[0] == '1':
            if len(resultsx) == 0:
                await ctx.send('Please make a request before choosing a number.')
            else:
                if ctx.voice_client != user_channel and ctx.voice_client != None:
                    vc = await user_channel.move_to(user_channel)
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[0][1])
                    vc.play(player)
                    resultsx.clear()
                elif ctx.voice_client != user_channel:
                    vc = await user_channel.connect()
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[0][1])
                    vc.play(player)
                    resultsx.clear()
                else:
                    vc = ctx.voice_client
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[0][1])
                    vc.play(player)
                    resultsx.clear()
        elif args[0] == '2':
            if len(resultsx) == 0:
                await ctx.send('Please make a request before choosing a number.')
            else:            
                if ctx.voice_client != user_channel and ctx.voice_client != None:
                    vc = await user_channel.move_to(user_channel)
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[1][1])
                    vc.play(player)
                    resultsx.clear()
                elif ctx.voice_client != user_channel:
                    vc = await user_channel.connect()
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[1][1])
                    vc.play(player)
                    resultsx.clear()
                else:
                    vc = ctx.voice_client
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[1][1])
                    vc.play(player)
                    resultsx.clear()
        elif args[0] == '3':
            if len(resultsx) == 0:
                await ctx.send('Please make a request before choosing a number.')
            else:            
                if ctx.voice_client != user_channel and ctx.voice_client != None:
                    vc = await user_channel.move_to(user_channel)
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[2][1])
                    vc.play(player)
                    resultsx.clear()
                elif ctx.voice_client != user_channel:
                    vc = await user_channel.connect()
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[2][1])
                    vc.play(player)
                    resultsx.clear()                    
                else:
                    vc = ctx.voice_client
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[2][1])
                    vc.play(player)
                    resultsx.clear()
        elif args[0] == '4':
            if len(resultsx) == 0:
                await ctx.send('Please make a request before choosing a number.')
            else:            
                if ctx.voice_client != user_channel and ctx.voice_client != None:
                    vc = await user_channel.move_to(user_channel)
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[3][1])
                    vc.play(player)
                    resultsx.clear()
                elif ctx.voice_client != user_channel:
                    vc = await user_channel.connect()
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[3][1])
                    vc.play(player)
                    resultsx.clear()                    
                else:
                    vc = ctx.voice_client
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[3][1])
                    vc.play(player)
                    resultsx.clear()
        elif args[0] == '5':
            if len(resultsx) == 0:
                await ctx.send('Please make a request before choosing a number.')
            else:            
                if ctx.voice_client != user_channel and ctx.voice_client != None:
                    vc = await user_channel.move_to(user_channel)
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[4][1])
                    vc.play(player)
                    resultsx.clear()
                elif ctx.voice_client != user_channel:
                    vc = await user_channel.connect()
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[4][1])
                    vc.play(player)
                    resultsx.clear()                    
                else:
                    vc = ctx.voice_client
                    player = await YTDLSource.from_url('https://www.youtube.com' + resultsx[4][1])
                    vc.play(player)
                    resultsx.clear()
        else:                        
            seperator = ' '
            search_query = seperator.join(args)
            results = YT(search_query, max_results = 5).export()
            resultsx.append(results[0])
            resultsx.append(results[1])
            resultsx.append(results[2])
            resultsx.append(results[3])
            resultsx.append(results[4])
            output = '''1. {name1}\n2. {name2}\n3. {name3}\n4. {name4}\n5. {name5}\
            '''.format(name1=results[0][0], name2=results[1][0], name3=results[2][0], name4=results[3][0], name5=results[4][0])
            await ctx.send(output)

@bot.command(name='url', pass_context=True)
async def url(ctx, url):
    if ctx.message.author.voice == None:
        await ctx.send('Join a voice channel before using this command.')
    else:
        user_channel = ctx.message.author.voice.channel
        if url.startswith('https://www.youtube.com/watch?v=') or url.startswith('www.youtube.com/watch?v='):
            if ctx.voice_client != user_channel:
                vc = await user_channel.connect()
                player = await YTDLSource.from_url(url)
                vc.play(player)
            else:
                vc = ctx.voice_client
                player = await YTDLSource.from_url(url)
                vc.play(player)
        else:
            await ctx.send('Please send valid YouTube URL.')

                    
@bot.command(name='state')
async def state(ctx):
    await ctx.send(ctx.message.author.voice)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(token)
