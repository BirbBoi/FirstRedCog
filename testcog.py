from discord.ext import commands


class testing: 
    """testing someshit"""

    def __init__(self, bot):
        self.bot = bot
    
@commands.command(no_pm=True)
async def copycat(self, *, text):
    await self.bot.say(text)


 def setup(bot):
    n = testing(bot)
    bot.add_cog(n)