import discord, aiohttp
import random
import requests
from discord.ext import commands
import asyncio
class nsfwgif(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.command(aliases=['pgif'])
  @commands.is_nsfw()
  async def porngif(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://nekobot.xyz/api/image?type=pgif') as r:
        res = await r.json()
        embed = discord.Embed(color=0xFF6EB4)
        embed.set_image(url=res['message'])
        embed.set_footer(text=f'yêu cầu bởi! - {ctx.author}',
    icon_url=ctx.author.avatar_url)
        await ctx.reply("Của Mày Đây!",embed=embed, mention_author=False)  
def setup(bot):
  bot.add_cog(nsfwgif(bot))