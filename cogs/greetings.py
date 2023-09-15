import discord
from discord.ext import commands 


class Greetings(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    # @commands.Cog.listener()
    # async def on_message(self, message: discord.Message):
    #     await message.add_reaction("✅")
    
    @commands.command(brief="Greets the user", description="Greets sender")
    async def hello(self, ctx):
        await ctx.send(f"Hello {str(ctx.author)}")
        



        
async def setup(bot):
    await bot.add_cog(Greetings(bot))