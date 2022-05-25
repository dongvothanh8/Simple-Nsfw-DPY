import discord, aiohttp
import random
import requests
import json
from discord.ext import commands
import asyncio

class nsfwtimkiem(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.command(pass_context=True, no_pm=True, aliases=['hyp'])
  @commands.is_nsfw()
  async def hypnohub(self, ctx, *, message:str):
    async with ctx.typing():
        await asyncio.sleep(1)
    limit = 10000
    message = message.replace(" ", "_")
    url = "https://hypnohub.net/index.php?page=dapi&s=post&q=index&json=1&limit={}&tags={}".format(limit, message)
    try:
      response = requests.get(url)
      data = json.loads(response.text)
      limit = len(data)
    except json.JSONDecodeError:
      await ctx.reply("xin lỗi tôi không tìm thấy", delete_after=5)
      return
    
    x = data[random.randint(0, limit-1)]['file_url']
    mess = "**vui lòng tuân thủ luật nsfw của sv vi phạm là tự ráng chịu**"
    await ctx.reply(x, mention_author=False)
    await ctx.reply(mess, mention_author=False, delete_after=5)
  @hypnohub.error
  async def hypnohub_error(self, ctx: commands.Context, error):
    
    if isinstance(error, commands.errors.MissingRequiredArgument):
      return await ctx.reply("**Mhypnohub <cái củ lol gì đó>\n VD: Mhypnohub mikoto**", delete_after=5)
      
def setup(bot):
  bot.add_cog(nsfwtimkiem(bot))