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

gif_links = json.load(open("gifs.json"))
moo_text = json.load(open("texts.json"))

@tree.command(name="scream", description="screaming for ur sanity")
async def scream(interaction):
  await interaction.response.send_message(random.choice(moo_text['screamies']))

@tree.command(name = "nooked", description="animal crossing funsies")
async def nooked(interaction):
  await interaction.response.send_message(file=discord.File("nook.jpeg"))
  
@tree.command(name="hug", description="hugs for ur sanity")
async def hugs(interaction):
  await interaction.response.send_message(random.choice(gif_links['hug']))
  
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
      await message.channel.send(random.choice(moo_text['good_thoughts']))
      
client.run(token) 






  