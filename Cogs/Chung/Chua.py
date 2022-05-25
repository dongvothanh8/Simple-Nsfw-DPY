import discord
from discord.ext import commands

class admin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['clear'])
  @commands.has_permissions(manage_messages = True) 
  async def donrac(self, ctx, amount: int = 1000000):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'thưa ngài {ctx.author.mention} tôi đã dọn sạch rác!')
    
def setup(bot):
  bot.add_cog(admin(bot))