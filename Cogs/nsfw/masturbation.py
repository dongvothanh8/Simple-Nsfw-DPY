import discord
import aiohttp
import random
import requests
from discord.ext import commands
import asyncio
class nsfw(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.command(aliases=['thudam'])
  @commands.is_nsfw()
  async def masturbation(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://api.l0calserve4.ml/hmtai/v2_4/masturbation') as r:
        res = await r.json()
        embed = discord.Embed(color=0xFF6EB4)
        embed.set_image(url=res)
        embed.set_footer(text=f'yêu cầu bởi! - {ctx.author}',
  icon_url=ctx.author.avatar_url)
        await ctx.reply("Của Mày Đây!",embed=embed, mention_author=False)
    
def setup(bot):
  bot.add_cog(nsfw(bot))