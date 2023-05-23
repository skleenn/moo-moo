import discord
from discord import app_commands
from discord.ext import commands
import os
import random

#discord bot code

TOKEN = 'MTAyNjI2NTI0MTkxMjM0NDY2Ng.GDkSqk.PPK0_tLc86MkJ__N2IB7c7z1fKBBkToX71GGaY'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(command_prefix='/', intents=intents)
tree = app_commands.CommandTree(client)


good_thoughts = ["moo. go watch thewizardliz.", "moo. go grind the code.", "moo. being sad is stupid.", "moo. get a fucking grip.", "moo. go talk to akhila about it."]
screamies = ["STOP FEELING SAD ABOUT STUPID SHIT.", "STOP THINKING ABOUT THE PAST.", "BITCHH YOU CAN DO 10X BETTER.", "IM THE FUCKING BEST MY RIZZ GAME IS CRAZY.", "STOP WANTING TO BE LOVED SO BADLY AND PATHETICALLY. LOVE YOUR FUCKING SELF."]

@tree.command(name="scream", description="slash command test")
async def scream(interaction):
  await interaction.response.send_message(random.choice(screamies))

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
    if message.content.startswith('/getnooked'):
      await message.channel.send(file=discord.File("nook.jpeg"))


client.run(TOKEN) 






  