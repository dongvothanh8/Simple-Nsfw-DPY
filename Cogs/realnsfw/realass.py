import discord, aiohttp
import random
import requests
from discord.ext import commands
import asyncio
class realnsfw(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.command(aliases=['nhungquamongcangmong'])
  @commands.is_nsfw()
  async def realass(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://nekobot.xyz/api/image?type=ass') as r:
        res = await r.json()
        embed = discord.Embed(color=0xFF6EB4)
        embed.set_image(url=res['message'])
        await ctx.reply("Của Mày Đây!",embed=embed, mention_author=False)
def setup(bot):
  bot.add_cog(realnsfw(bot))