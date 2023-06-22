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
  embed = discord.Embed(colour=discord.Colour.random(), description=random.choice(moo_text["hug_text"]))
  embed.set_image(url=random.choice(gif_links['hug']))
  await interaction.response.send_message(embed=embed)

@tree.command(name="real", description="real depressing anime memes...not the funnest")
async def real(interaction):
  embed = discord.Embed(colour=discord.Colour.random())
  embed.set_image(url=random.choice(gif_links['real']))
  await interaction.response.send_message(embed=embed)

@tree.command(name="slap", description="slaps for venties")
async def slaps(interaction, name:str):
  embed = discord.Embed(colour=discord.Colour.random(), description=f"you slapped {name} !")
  embed.set_image(url=random.choice(gif_links['slap']))
  await interaction.response.send_message(embed=embed)

@tree.command(name="funnyadvice", description="Funny advice (courtesy of spellcast.)")
async def funnyadvice(interaction):
  possibilities - [
    ["You should ", "You should not ", "This is the greatest advice "],
    ["explode ", "eat ", "defenestrate ", "consume ", "explode ", "slap "],
    ["a car.", "jvm compiler arch (spellcast reference)", "esp32.", "mongodb server (programming reference).", "xtensa chip (spellcast reference).", "potato.", "the sun.", "an atom bomb."]
  ]

  value = ""

  for ind, val in enumerate(possibilities):
    value += random.choice(val)

  await interaction.response.send_message(value)
  #tcp reference spellcast was here hahahahah

  
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






  
