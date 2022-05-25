from discord.ext import commands


class ErrorHandler(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"Vui lòng chờ **{round(error.retry_after, 1)}** giây. Đừng có mà spam \>:("
        elif isinstance(error, commands.MissingPermissions):
          message = "bạn không có quyền là điều này"
        elif isinstance(error, commands.MissingRequiredArgument):
            return
        elif isinstance(error, commands.errors.NSFWChannelRequired):
           message = "**Djtme Mày Cút Vào Kênh NSFW Hộ Bố**"
           
        else:
            raise error

        await ctx.reply(message, delete_after=5)
        

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
