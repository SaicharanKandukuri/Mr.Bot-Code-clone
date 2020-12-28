import discord
import os
import requests
import json
from keep_alive import keep_alive
import classes_data


client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)

  quote = json_data[0]['q'] + " -" + json_data[0]['a']

  return(quote)

@client.event

async def on_ready():
  print('We have Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if message.content.startswith('$check'):
    await message.channel.send("Beep Beep .. Iam Alive and active")

  if message.content.startswith('$monday'):
    await message.channel.send(classes_data.database["monday_tb"])
  if message.content.startswith('$tuesday'):
    await message.channel.send(classes_data.database["tuesday_tb"])
  if message.content.startswith('$wednesday'):
    await message.channel.send(classes_data.database["wednesday_tb"])
  if message.content.startswith('$thursday'):
    await message.channel.send(classes_data.database["thursday_tb"])
  if message.content.startswith('$friday'):
    await message.channel.send(classes_data.database["friday_tb"])
  if message.content.startswith('$saturday'):
    await message.channel.send(classes_data.database["saaturday_tb"])
  if message.content.startswith('$sunday'):
    await message.channel.send(classes_data.database["sunday_tb"])
  if message.content.startswith('$help'):
    await message.channel.send(classes_data.database["help"])

async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
          
intents = discord.Intents.default()
intents.members = True





keep_alive()
client.run(os.getenv('START'))