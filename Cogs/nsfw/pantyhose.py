import discord, aiohttp
import random
import requests
import json
from discord.ext import commands
import asyncio
class nsfw(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.command()
  @commands.is_nsfw()
  async def pantyhose(self, ctx):
    limit = 10000
    url = f'https://konachan.com/post.json?tags=pantyhose&3Afalse&limit={limit}&api_version=2&filter=1&'f'include_tags=1&include_votes=1&include_pools=1'
    try:
      response = requests.get(url)
      data = json.loads(response.text)
      limit = len(data)
    except json.JSONDecodeError:
      
       return


    x = data['posts'][random.randint(0, limit-1)]['file_url']
    embed = discord.Embed(color=0xFF6EB4)
    embed.set_image(url=x)
    embed.set_footer(text=f'yêu cầu bởi! - {ctx.author}',icon_url=ctx.author.avatar_url)
    await ctx.reply("Của Mày Đây!",embed=embed, mention_author=False)    
def setup(bot):
  bot.add_cog(nsfw(bot))