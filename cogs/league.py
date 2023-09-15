import discord
from discord.ext import commands
import riotapi


class League(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    # @commands.Cog.listener()
    # async def on_message(self, message: discord.Message):
    #     await message.add_reaction("✅")
    
    @commands.command(brief=": $leagueprofile [server] [summoner name]", description="""
The command requires you to put in two parameeters



$leagueprofile [server] [summonername]



server corresponds to the league servers [refer to the server list below]

summonername refers to the players in game name(not their riot id but their name in league)      



server list:

BR1     Brazil

EUN1    Europe Nordic & East

EUW1    Europe West

JP1         Japan

KR          Republic of Korea

LA1         Latin America North

LA2         Latin America South

NA1         North America

OC1         Oceania

TR1         Turkey

RU          Russia

PH2         The Philippines

SG2         Singapore, Malaysia, & Indonesia

TH2         Thailand

TW2         Taiwan, Hong Kong, and Macao

VN2         Vietnam
""")
    async def leagueprofile(self, ctx, server: str=commands.parameter(default="this is default", description="this is description"), *summonername: str):
        server=server
        summonerdetails=riotapi.searchsummoner.by_name(" ".join(summonername), server)


        #code from got to edit

        embed = discord.Embed(
            colour=discord.Colour.dark_teal(), 
            description="this is the description", 
            title="this is the title"
        )
        
        embed.set_footer(text="this is the footer")
        embed.set_author(name="Richard", url="https://www.youtube.com/channel/UCIJe3dIHGq1lIAxCCwx8eyA")
        
        embed.set_thumbnail(url="https://yt3.ggpht.com/GiBCvnzO8e3_cPclwtRCUqLye86F0_xNOPK0FYeshaths5DO2SLvJq9cBVZ0BL-oNwjt90huIw=s108-c-k-c0x00ffffff-no-rj")
        embed.set_image(url="https://i.ytimg.com/vi/SoqYG_5pQBA/maxresdefault.jpg")
        
        embed.add_field(name="Channel", value="https://www.youtube.com/channel/UCIJe3dIHGq1lIAxCCwx8eyA", inline=False)
        embed.add_field(name="Website", value="richardschwabe.de" )
        embed.insert_field_at(1,name="Tree", value="https://linktr.ee/richardschwabe")
        
        await ctx.send(embed=embed)

        await ctx.send(f"Heres the profile for ***{summoner}*** ")
        await ctx.send(f"Heres the profile for ***{summoner}*** ")
        



        
async def setup(bot):
    await bot.add_cog(League(bot))