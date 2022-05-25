import discord, aiohttp
import random
import requests
import json
from discord.ext import commands
import asyncio

class nsfwtimkiem(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.command(pass_context=True, no_pm=True, aliases=["dnb"])
  @commands.is_nsfw()
  async def danbooru(self, ctx, *, message:str):
    async with ctx.typing():
        await asyncio.sleep(1)
    limit = 10000
    message = message.replace(" ", "_")
    url = "https://danbooru.donmai.us/post/index.json?limit={}&tags={}".format(limit, message)
    response = requests.get(url)
    data = json.loads(response.text)
    limit = len(data)
    if not data:
      await ctx.reply("Xin Lỗi Tôi Không Tìm Thấy", delete_after=5)
      return
    x = data[random.randint(0, limit-1)]
    if x["file_url"].startswith("http"):
      final_url = x["file_url"]
    else:
      final_url = "http://danbooru.donmai.us{}".format(x["file_url"])
    mess = "**vui lòng tuân thủ luật nsfw của sv vi phạm là tự ráng chịu**"
    await ctx.reply(final_url, mention_author=False)
    await ctx.reply(mess, mention_author=False, delete_after=5)
  @danbooru.error
  async def danbooru_error(self, ctx: commands.Context, error):
    
    if isinstance(error, commands.errors.MissingRequiredArgument):
      await ctx.reply("**Mdanbooru <cái củ lol gì đó>\n VD: Mdanbooru azur lane**", delete_after=5)
def setup(bot):
  bot.add_cog(nsfwtimkiem(bot))