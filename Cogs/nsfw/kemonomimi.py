import discord
import aiohttp
import random
import requests
from discord.ext import commands
import asyncio
class nsfw(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.command(aliases=['kemo'])
  @commands.is_nsfw()
  async def kemonomimi(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://api.nekos.dev/api/v3/images/nsfw/img/kemonomimi_lewd/') as r:
        res = await r.json()
        embed = discord.Embed(color=0xFF6EB4)
        embed.set_image(url=res['data']['response']['url'])
        embed.set_footer(text=f'yêu cầu bởi! - {ctx.author}',
  icon_url=ctx.author.avatar_url)
        await ctx.reply("Của Mày Đây!",embed=embed, mention_author=False)
    
def setup(bot):
  bot.add_cog(nsfw(bot))