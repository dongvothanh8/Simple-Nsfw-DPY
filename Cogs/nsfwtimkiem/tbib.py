import discord, aiohttp
import random
import requests
import json
from discord.ext import commands
import asyncio

class nsfwtimkiem(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.command(pass_context=True, no_pm=True, aliases=['tb'])
  @commands.is_nsfw()
  async def tbib(self, ctx, *, message:str):
    async with ctx.typing():
        await asyncio.sleep(1)
    limit = 10000
    message = message.replace(" ", "_")
    url = "https://tbib.org/index.php?page=dapi&s=post&q=index&json=1&limit={}&tags={}".format(limit, message)
    try:
     response = requests.get(url)
     data = json.loads(response.text)
     limit = len(data)
    except json.JSONDecodeError:
      await ctx.reply("xin lỗi tôi không tìm thấy", delete_after=5)
      return
    x = data[random.randint(0, limit-1)]
    final_url = "https://tbib.org/images/{}/{}".format(x["directory"], x["image"])
    mess = "**vui lòng tuân thủ luật nsfw của sv vi phạm là tự ráng chịu**"
    await ctx.reply(final_url, mention_author=False)
    await ctx.reply(mess, mention_author=False, delete_after=5)

  @tbib.error
  async def tbib_error(self, ctx: commands.Context, error):
    
    if isinstance(error, commands.errors.MissingRequiredArgument):
      await ctx.reply("**Mtbib <cái củ lol gì đó>\n VD: Mtbib mikoto**", delete_after=5)
def setup(bot):
  bot.add_cog(nsfwtimkiem(bot))