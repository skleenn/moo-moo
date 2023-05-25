import discord
from discord import app_commands
from discord.ext import commands
import requests, json
import os
import random

#discord bot code
token = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(command_prefix='/', intents=intents)
tree = app_commands.CommandTree(client)

links = json.load(open("gifs.json"))

good_thoughts = ["moo. go watch thewizardliz.", "moo. go grind the code.", "moo. being sad is stupid.", "moo. get a fucking grip.", "moo. go talk to akhila about it."]
screamies = ["STOP FEELING SAD ABOUT STUPID SHIT.", "STOP THINKING ABOUT THE PAST.", "BITCHH YOU CAN DO 10X BETTER.", "IM THE FUCKING BEST MY RIZZ GAME IS CRAZY.", "STOP WANTING TO BE LOVED SO BADLY AND PATHETICALLY. LOVE YOUR FUCKING SELF.", "YOU DONT NEED MEN."]
hug = [
      "https://tenor.com/view/anime-hug-sweet-love-gif-14246498",
      "https://tenor.com/view/anime-hug-love-anime-girls-gif-26404145",
      "https://tenor.com/view/hug-gif-25588769",
      "https://tenor.com/view/yakuzas-way-to-babysitting-anime-hug-gif-26453807",
      "https://tenor.com/view/teria-wang-kishuku-gakkou-no-juliet-hug-anime-gif-16509980",
      "https://tenor.com/view/hug-gif-21989089",
      "https://tenor.com/view/anime-hug-girl-girlxgirl-cute-gif-22306001",
      "https://tenor.com/view/anime-priconne-anime-hug-hug-gif-24806471"
    ]

@tree.command(name="scream", description="screaming for ur sanity")
async def scream(interaction):
  await interaction.response.send_message(random.choice(screamies))

@tree.command(name = "nooked", description="animal crossing funsies")
async def nooked(interaction):
  await interaction.response.send_message(file=discord.File("nook.jpeg"))


  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await tree.sync()
  
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    bad_thoughts = ["i wanna kms", "die", "sad", "hate", "suicide"]
    if any(word in message.content for word in bad_thoughts):
      await message.channel.send(random.choice(good_thoughts))
      
client.run(token) 






  