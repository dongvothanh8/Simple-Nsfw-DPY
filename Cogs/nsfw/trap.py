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
  async def trap(self, ctx):
    r = requests.get("https://api.waifu.pics/nsfw/trap")
    res = r.json()
    embed = discord.Embed(color=0xFF6EB4)
    embed.set_image(url=res['url'])
    embed.set_footer(text=f'yêu cầu bởi! - {ctx.author}',
  icon_url=ctx.author.avatar_url)
    await ctx.reply(f'Của Mày Đây!', embed=embed, mention_author=False)
def setup(bot):
  bot.add_cog(nsfw(bot))