import discord
import requests
import os
from dotenv import load_dotenv
from discord.ext import commands
#from jokeapi import Jokes # Import the Jokes class
import asyncio
import json
load_dotenv()


DISCORD_TOKEN = os.getenv('token')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


# functional
@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

# @bot.command(name= "joke")
# async def startJoke(ctx):
#     asyncio.run(joke(ctx))

# async def joke(ctx):
#     j = await Jokes()  # Initialise the class
#     joke = await j.get_joke()  # Retrieve a random joke
#     if joke["type"] == "single": # Print the joke
#         ctx.channel.send(joke["joke"])
#     else:
#         ctx.channel.send(joke["setup"])
#         ctx.channel.send(joke["delivery"])
    


@bot.command(name= "catpic")
async def fact(ctx):
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = response.json()

    cat_url = data[0]["url"]
    await ctx.channel.send(cat_url)
    
    
# functional
@bot.command(name= 'Love')
async def love(ctx, name: str):
    LOVE_API_KEY = os.getenv('love_api_key')
    LOVE_API_URL = "https://love-calculator.p.rapidapi.com/getPercentage"
    if "@" in name:
        await ctx.channel.send('Please do not include \'@\' in your love request!')
        return 
    name = name.capitalize()
    querystring = {"fname": ctx.author.name, "sname": name}

    headers = {
        "X-RapidAPI-Key": LOVE_API_KEY,
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }

    try:
        response = requests.request("GET", LOVE_API_URL, headers=headers, params=querystring)
        response.raise_for_status()

        data = response.json()

        await ctx.channel.send(f'Love Percentage between {data["fname"]} and {data["sname"]}: {data["percentage"]}%\n{data["result"]}')
    except requests.exceptions.RequestException as errh:
        await ctx.channel.send(f'Uh Oh... Something broke!\nError: {errh}')

# functional
@bot.event
async def on_member_join(member):
    await member.send("Hello, World!")


# functional
@bot.event  
async def on_message(msg):
    if msg.author != bot.user:
        if msg.content.lower().startswith('hi'):
            await msg.channel.send(f'Hi, {msg.author.display_name}')
    await bot.process_commands(msg) # This will run the other commands declared on the bot. Alternatively remove the on_message handler


# functional
@bot.event
async def on_message_delete(message):
    await message.channel.send(f'{message.author.display_name} is acting quite sus :face_with_raised_eyebrow: \n They deleted: {message.content}')


bot.run(DISCORD_TOKEN)
    

