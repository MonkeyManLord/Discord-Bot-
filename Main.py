import discord
import requests
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()


DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
RAPID_API_URL = "https://love-calculator.p.rapidapi.com/getPercentage"

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


# functional
@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')


# functional
@bot.command()
async def love(ctx, name: str):
    querystring = {"fname": ctx.author.name, "sname": name}

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }

    try:
        response = requests.request("GET", RAPID_API_URL, headers=headers, params=querystring)
        response.raise_for_status()

        data = response.json()

        await ctx.channel.send(f'Love Percentage between {data["fname"]} and {data["sname"]}: {data["percentage"]}%')
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
        if msg.content.lower().startswith('!hi'):
            await msg.channel.send(f'Hi, {msg.author.display_name}')
    await bot.process_commands(msg) # This will run the other commands declared on the bot. Alternatively remove the on_message handler


# functional
@bot.event
async def on_message_delete(message):
    await message.channel.send(f'{message.author.display_name} is acting quite sus :face_with_raised_eyebrow: \n They deleted: {message.content}')


bot.run(DISCORD_TOKEN)
