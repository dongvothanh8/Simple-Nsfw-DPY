import os
import discord
from discord.ext import commands
import datetime
import json
import asyncio
from discord_components import *
intents = discord.Intents.all()
with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    prefix = data["PREFIX"]
bot = ComponentsBot(command_prefix=prefix, intents = intents)
DiscordComponents(bot)
bot.remove_command("help")
for folder in os.listdir("./Cogs"):
  for filename in os.listdir(f"./Cogs/{folder}"):
     if filename.endswith(".py"):
       bot.load_extension(f"Cogs.{folder}.{filename[:-3]}")
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.dnd)
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Mikoto Sủi Đi Thủ Dâm"))
  x = datetime.datetime.now()
  print(x.strftime("%X"), '\033[1;36;40m{0.user} đã hoạt động!'.format(bot))
  
  
  
  

bot.run(token)