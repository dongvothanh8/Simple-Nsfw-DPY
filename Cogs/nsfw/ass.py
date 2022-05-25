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
  async def ass(self, ctx):
    r = requests.get("https://api.waifu.im/random/?selected_tags=ass")
    res = r.json()
    embed = discord.Embed(color=discord.Color.random())
    embed.set_image(url=res['images'][0]['url'])
    embed.set_footer(text=f'yêu cầu bởi! - {ctx.author}',
  icon_url=ctx.author.avatar_url)
    await ctx.reply(f'Của Mày Đây!',
    embed=embed, mention_author=False)

def setup(bot):
  bot.add_cog(nsfw(bot))