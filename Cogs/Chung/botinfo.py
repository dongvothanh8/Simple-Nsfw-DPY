import discord
from discord.ext import commands
import psutil
import datetime
from datetime import datetime , timedelta
import time
class daika(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.Cog.listener()
  async def on_ready(self):
    global startTime
    startTime = time.time()

  @commands.command(aliases=["info"])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def infobot(self, ctx):
    uptime = str(timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(timestamp = datetime.utcnow(), color=discord.Color.random())
    embed.set_author(name="Mẹ Mày Béo")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/975075750984171723/976344864134426654/HxPCHxZe.png")
    embed.add_field(name=f"Thẹn Thùng Nhìn Em Quay Gót Đi Mãi Anh Đứng Chết Lặng Trong Mưa", value=f'•>Dev Lỏ : **mmbeo#7580**\n•>Ngôn Ngữ : **Python**\n•>Dpy : **1.7.3**\n•>Host Chùa : **Heroku**\n•>Cpu : **{psutil.cpu_percent()}%**\n•>Bộ Nhớ : **{psutil.virtual_memory().percent}%**\n•>Uptime : **{uptime}**')
    
        
    await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
     bot.add_cog(daika(bot))