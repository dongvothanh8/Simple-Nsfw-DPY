import discord
import akaneko
import random
import requests
from discord.ext import commands
import asyncio
class nsfw(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.command()
  @commands.is_nsfw()
  async def pantsu(self, ctx):
    embed = discord.Embed(color=0xFF6EB4)
    img = akaneko.nsfw.panties()
    embed.set_image(url = img)
    embed.set_footer(text=f'yêu cầu bởi! - {ctx.author}',
  icon_url=ctx.author.avatar_url)
    await ctx.reply("Của Mày Đây!",embed=embed, mention_author=False)
    
def setup(bot):
  bot.add_cog(nsfw(bot))