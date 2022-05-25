import discord
from discord.ext import commands
from discord_components import *
from datetime import datetime
import time
import asyncio
bot = discord.ext.commands.Bot(command_prefix = "M");
DiscordComponents(bot)
class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.group(invoke_without_command=True)
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def help(self, ctx):
      async with ctx.typing():
          await asyncio.sleep(1)
      em = discord.Embed(color=discord.Color.random(), timestamp = datetime.utcnow())
      em.set_author(name="**Bo may gay me may beo**", icon_url=ctx.author.avatar_url)
      em.add_field(name="Danh Sách Lệnh Của Mấy Thg Nigga", value="<:WND_troll_face:978144246018240543> 👉 `vui lòng  xuống menu và nhấp vào danh mục để xem các lệnh của bot`")
      em.set_image(url="https://media.discordapp.net/attachments/975075750984171723/978141074486861886/Screenshot_20220512-175044_Discord.jpg")
      em.set_footer(text='MonDz - 2022 ©', icon_url="https://files.catbox.moe/j1lcf0.png")
      await ctx.send("Danh Mục Bi Li <:WND_mikoto:957805362524856381>",
        components = [
            Select(
                placeholder = "🖕 Mảine Béo Như Mẹ Mày",
                options = [
                    SelectOption(label = "Seg Alumi", 
                      emoji = "🥴",
                      description = "khá nứng nha ae",  
                      value="1"),
                    SelectOption(label = "Seg Gif", 
                      emoji = "🥵", description = "phịch nhau ko ngừng nghỉ", value="2"),
                    SelectOption(label = "real Seg", description="nungws lv max", emoji = "😖", value="3"),
                    SelectOption(label = "Search Seg",description="cái lồn gì cũng có", emoji ="🧐", value="4"),
                    SelectOption(label = "Thông Tin",description="để xem lại sự thất bại của mày", emoji = "🤓", value="5")
                    
                    
                ],custom_id="SelectSomething"
            )
        ]
      , embed=em)

      while(True):
        try:
          msg = await self.bot.wait_for("select_option", check = lambda inter: inter.custom_id == "SelectSomething" and inter.user == ctx.author)
          res = msg.values[0]
          if res == "1":
            em1 = discord.Embed(color=discord.Color.random(), timestamp = datetime.utcnow())
            em1.add_field(name="<:ukmrs:956506249053208588> **SEG ALIMI**\nThẹn thùng nhìn em quay gót đi mãi Anh đứng chết lặng trong mưa :", value="`ass` • `boobs` • `bucu` • `ecchi` • `ero` • `futa` • `neko` \n`public` • `kitsune` • `lon` • `milf` • `hentai` • `solo`\n`paizuri` • `trap` • `waifu` • `xuctua` • `yaoi` • `yuri`\n`bdsm` • `tits` • `holo` • `pantyhose` • `orgy` • `elves`\n`feet` • `maid` • `anus` • `succubus` • `femdom` • `anal`\n`gangbang` • `doujin` • `loanluan` • `bondage` • `fox`\n`uniform` • `glasses` • `pantsu` • `thudam` • `zettai`\n`dui` • `ntr` • `ahegao` • `hocsinh` • `azurlane` • `fgo`\n`genshin` • `kemo` • `cum` • `creampie` • `dom` • `furry`\n`ff`", inline=False)
            await msg.send(embed=em1)
            
          elif res == "2":
            em2 = discord.Embed(color=discord.Color.random(), timestamp = datetime.utcnow())
            em2.add_field(name="<:emoji_432:971715973352685598> **SEG GIF**\nDù rằng bên em đã có ai Nhưng nơi đây anh vẫn còn chờ :", value=">>> `bucugif` • `liemlongif` • `longif` • `porngif`\n`classicgif`• `2nu1nam` • `2nam1nu` • `yaoigif`\n`nekogif` • `cumgif` • `yurigif` • `spank`  • `3nu` ", inline=False)
            await msg.send(embed=em2)
          elif res == "3":
            em3 = discord.Embed(color=discord.Color.random(), timestamp = datetime.utcnow())
            em3.add_field(name="<:4546animediscusted:959540133063983224> **REAL SEG**\nNgọt ngào em trao chẳng thấy Nhưng chỉ toàn chua cay :", value=">>> `realanal`\n`realass`\n`realboobs`\n`4k`\n`bikini`\n`reallon`\n`realbucu`\n`realdui`", inline=False)
            await msg.send(embed=em3)
          elif res == "4":
            em4 = discord.Embed(color=discord.Color.random(), timestamp = datetime.utcnow())
            em4.add_field(name="<:emoji_166:957770331001589791> **Tìm Kiếm**\nCố xóa những phút giây Ngày mà bên nhau bao ước thề :", value=">>> **tbib(tb) : `rule34 là đbrr`**\n**xbooru(xb) : `đệ rule34`**\n**rule34(r34) : `all thể loại vip pro max`**\n**yandere(yd) : `alimi`**\n**konachan(kc) : `alimi`**\n**realbooru(rb) : `thực tế`**\n**danbooru(dnb) : `alimi nhưng vip pro `**\n**hypnohub(hyp) : `all thể loại`**\n", inline=False)
            
            await msg.send(embed=em4)
          elif res == "5":
            em5 = discord.Embed(color=discord.Color.random(), timestamp = datetime.utcnow())
            em5.add_field(name="<:WND_kannastare:963162446636404806> **thông tin**\nCô bước đi Lặng thầm tìm lại em hôm qua Mặn nồng ta trao cùng nhau vun đắp :", value=">>> ping\navatar\nuserinfo\nserverinfo\nbotinfo", inline=False)
            
            await msg.send(embed=em5)
          else:
            await msg.send(res)
        except:
          await ctx.send("Mẹ Mày Béo!", ephemeral = True)
def setup(bot):
    bot.add_cog(ExampleCog(bot))