import discord
import requests
import os
import json
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv(f'-implimented-') 


token = os.getenv('token')
api_key = os.getenv('api_key')


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
url = "https://love-calculator.p.rapidapi.com/getPercentage"

#functional
@bot.event
async def on_ready():
   print(f'Bot logged in as {bot.user}')

#not functional
@bot.command(name='Love')
async def love_calculator(ctx, *, name2):
   name1 = ctx.author.name
   name2 = name2[1:]
   querystring = {"sname":name2,"fname":name1}


   # Call the Love Calculator API with the two names and the API key
   headers = {
   "X-RapidAPI-Key": api_key,
   "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
   }

   print("It shouldve worked")
   response = requests.request("GET", url, headers=headers, params=querystring)


   # Parse the response and send the result to the user
   #data = response.json()\
   data = json.loads(response.text)
   first = data['fname']
   second = data['sname']
   percentage = data['percentage']
   result = data['result']
   message = f'Love Percentage between {first} and {second}: {percentage}%'
   
   await ctx.channel.send(message)


  #not functional
@bot.event
async def on_member_join(member):
   user = member.author
   await user.send("Hello, World!")

#functional
@bot.event
async def on_message(msg):
   if msg.author != bot.user:
       if msg.content.lower().startswith('!hi'):
           await msg.channel.send(f'Hi, {msg.author.display_name}')

#functional
@bot.event
async def on_message_delete(message):
   await message.channel.send(f'{message.author.display_name} is acting quite sus :face_with_raised_eyebrow: \n They deleted: {message.content}')
bot.run(token)


