import discord
from discord.ext import commands
from datetime import datetime
import time
class daika(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot 
  @commands.command(aliases=['ui'])
  async def userinfo(self, ctx, *, member: discord.Member = None):
    if member is None:
        member = ctx.author  
    rlist = []
    for role in member.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)
    b = '•'.join(rlist)
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title="thông tin Của Em Gái",description=f"•> Tên: **{member.name}**\n•>Tag: **{member.discriminator}**\n•> ID: **{member.id}**\n•> Đã Vào SV: **{member.joined_at.__format__('%A, %d. %B %Y | %H:%M:%S')}**\n•> TK Đã Tạo: **{member.created_at.__format__('%A, %d. %B %Y | %H:%M:%S')}**", timestamp = datetime.utcnow(), color=discord.Color.random())
    embed.add_field(name=f"•> Role: {len(rlist)}", value="".join([b]), inline=False)
    
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'yêu cầu bởi! - {ctx.author}', icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed, mention_author=False)
#=========================================
  @commands.command(aliases =["av","avt"])
  async def avatar(self, ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    em = discord.Embed(title=str(member), color=discord.Color.random())
    em.set_image(url=member.avatar_url)
    em.set_footer(text=f'yêu cầu bởi! - {ctx.author}',
  icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=em, mention_author=False)
#=========================================
  @commands.command(name="ping")
  async def ping(self, ctx: commands.Context):
    start_time = time.time()
    message = await ctx.send("Kiểm tra độ trễ...")
    end_time = time.time()
    await message.edit(content=f"**Pong!🏓  {round(self.bot.latency * 1000)} ms | API  {round((end_time - start_time) * 500)} ms**")
#=========================================
  @commands.command(aliases=['si'])
  async def serverinfo(self, ctx):
    guild = ctx.guild
    format =  r"%x : %X : %p"
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    channels = text_channels + voice_channels
    role_count =len(ctx.guild.roles)
    embed = discord.Embed(color=discord.Color.random())
    embed.add_field(name=f"Thông tin về: **{ctx.guild.name}**", value=f"•> Chủ tịch nước: **{ctx.guild.owner.mention}**\n•> ID: **{ctx.guild.id}**\n•> Ngày Thành Lập: **{ctx.guild.created_at.strftime(format)}**\n•> Số kênh: **{channels}** | Kênh Text: **{text_channels}** • Kênh Voice: **{voice_channels}**\n•> Dân số: **{ctx.guild.member_count}**\n•> Boost: **{ctx.guild.premium_subscription_count}**\n•> Roles: **{role_count}**")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_image(url=ctx.guild.banner_url)
    await ctx.reply(embed=embed, mention_author=False)
#=========================================

#===========================================

def setup(bot):
     bot.add_cog(daika(bot))
