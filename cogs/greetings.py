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
        print(f"hello command triggered by user id:{ctx.author.id}")
        if ctx.author.id=="507227799778492426":
            await ctx.send("Hello my shuntu munutu... My kolijar tukra I wuv you bbg <3")
        
        await ctx.send(f"Hello {str(ctx.author)}")
        



        
async def setup(bot):
    await bot.add_cog(Greetings(bot))