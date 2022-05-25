import discord, aiohttp
import random
import requests
import json
from discord.ext import commands
import asyncio

class nsfw(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot
  @commands.command(aliases=['gaicubu'])
  @commands.is_nsfw()
  async def futa(self, ctx):
    limit = 10000
    url = "https://danbooru.donmai.us/post/index.json?limit={}&tags=futanari".format(limit)
    response = requests.get(url)
    data = json.loads(response.text)
    limit = len(data)
    if not data:
      return
    x = data[random.randint(0, limit-1)]
    if x["file_url"].startswith("http"):
      final_url = x["file_url"]
    else:
      final_url = "http://danbooru.donmai.us{}".format(x["file_url"])
    embed = discord.Embed(color=0xFF6EB4)
    embed.set_image(url=final_url)
    embed.set_footer(text=f'yêu cầu bởi! - {ctx.author}',icon_url=ctx.author.avatar_url)
    await ctx.reply("Của Mày Đây!",embed=embed, mention_author=False)
def setup(bot):
  bot.add_cog(nsfw(bot))