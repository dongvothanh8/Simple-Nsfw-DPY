import discord, aiohttp
import random
import requests
import json
from discord.ext import commands
import asyncio

class nsfwtimkiem(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.command(pass_context=True, no_pm=True, aliases=['yd'])
  @commands.is_nsfw()
  async def yandere(self, ctx, *, message:str):
    async with ctx.typing():
        await asyncio.sleep(1)
    
    message = message.replace(" ", "_")
    url = f'https://yande.re/post.json?tags={message}&3Afalse&limit=1000&api_version=2&filter=1&'f'include_tags=1&include_votes=1&include_pools=1'
    try:
      response = requests.get(url)
      data = json.loads(response.text)
      limit = len(data)
    except json.JSONDecodeError:
      await ctx.reply("xin lỗi tôi không tìm thấy", delete_after=5)
      return
    
    x = data['posts'][random.randint(0, 1000)]['file_url']
    mess = "**vui lòng tuân thủ luật nsfw của sv vi phạm là tự ráng chịu**"
    await ctx.reply(x,mention_author=False)
    await ctx.reply(mess, mention_author=False, delete_after=5)
  @yandere.error
  async def yandere_error(self, ctx: commands.Context, error):
    
    if isinstance(error, commands.errors.MissingRequiredArgument):
      return await ctx.reply("**Myandere <cái củ lol gì đó>\n VD: Myandere mikoto**", delete_after=5)
      
def setup(bot):
  bot.add_cog(nsfwtimkiem(bot))