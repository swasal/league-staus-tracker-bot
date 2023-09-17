import discord
from discord.ext import commands
import datetime
import riot.riotapi as riotapi
import riot.datadragon as datadragon


class leaguefn:
    server={'BR1': 'Brazil', 'EUN1': 'Europe Nordic & East', 'EUW1': 'Europe West', 'JP1': 'Japan', 'KR': 'Republic of Korea', 'LA1': 'Latin America North', 'LA2': 'Latin America South', 'NA1': 'North America', 'OC1': 'Oceania', 'TR1': 'Turkey', 'RU': 'Russia', 'PH2': 'The Philippines', 'SG2': 'Singapore, Malaysia, & Indonesia', 'TH2': 'Thailand', 'TW2': 'Taiwan, Hong Kong, and Macao', 'VN2': 'Vietnam'}
    "all the functions for league bot in here"
    def profile(server, summoner):
        "gives summoner profile"
        
        summ=riotapi.searchsummoner.by_name(summoner, server)
        summ["profilepic"]=datadragon.profile.icon(summ["profileIconId"]) #adding url to profile picture
        mastery=riotapi.summonerStats.highestmastery(summ["id"], server)
        summ["favchampion_name"]=datadragon.champion.name(mastery["championId"]) #returns anme of highest mastery champion
        summ["favchampion_splash"]= datadragon.champion.splashart(summ["favchampion_name"])#returns url of splash art for highest mastery champion
        summ["favchampion_level"]=mastery['championLevel']
        summ["favchampion_points"]=mastery['championPoints']
        summ['rank']=riotapi.summonerStats.rank(summ['id'], server)
        return summ


    def matchsummary(matchid, puuid):
        r=riotapi.summonerStats.matchdetails(matchid)
        puuidlist=r['metadata']['participants'] #puuid
        output={} #, 'win':None, 'player':None}
        index=puuidlist.index(puuid)
        player= r['info']['participants'][index]
        output['gameid']=r['metadata']['matchId']
        output['gameCreation']=datetime.datetime.fromtimestamp((r['info']['gameCreation'])/1000)
        output['gameDuration']=round(r['info']['gameDuration']/60,2)
        output['mapname']=datadragon.gameconstants.mapname(r['info']['mapId'])
        output['name']=player['summonerName']
        output['kda']=str(player['kills'])+"/"+str(player['deaths'])+"/"+str(player['assists'])
        output['damage']=player['totalDamageDealt']
        output['gold']=player['goldEarned']
        output['championName']=player['championName']
        #neutralMinionsKilled=jungle; totalMinionsKilled=laneminions
        output['cs']=player['neutralMinionsKilled']+player['totalMinionsKilled']+player['wardsKilled']

        #appending all items in a string[exceeds embed space]
        output['items']=""        
        #appending items
        for i in range(0,6):
            output['items']+=f"{datadragon.gameconstants.itemsname(player['item'+str(i)])}\n"

        output['items']=output['items'][0:-2]


        #setting win and color
        if player['win']==True:
            output['status']="Victory"
            output['color']="#55EC10"
        else:
            output['status']="Defeat"
            output['color']="#F1140E"

        #checking que type to add to mapname
        q= r['info']['queueId']
        if q == 0:
            output['mapname']+=" [Custom]"
        elif q in [4, 420]:
            output['mapname']+=" [Ranked SOLO]"
        elif q in [9, 440]:
            output['mapname']+=" [Ranked Flex]"
        else:
            output['mapname']+=" [Normal]"

        output['name']=player['summonerName']

        return output




#the cog for kootiepai
class League(commands.Cog):
    "the cog for kootiepai"
    
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(brief=": $leagueprofile [server] [summoner name]",description="Shows league profile of the requested player.\n error maybe due to incorrect server name or username")
    async def leagueprofile(self, ctx, server: str, *summonername: str):
        server=server.lower()
        summoner=" ".join(summonername).lower()
        summonerdetails=leaguefn.profile(server, summoner)     

        embed = discord.Embed(
            colour=discord.Colour.from_str("#A522E7"), 
            description=f"Sumonner level: {summonerdetails['summonerLevel']}", 
            title=f"The profile for {summonerdetails['name']}" #set it to name of player
        )
        
        # embed.set_footer(text="Last online:") #add last match time for last online
        embed.set_author(name=f"Server:{leaguefn.server[server.upper()]} [{server.upper()}]") #set it to server name

        #use thumbnail for profile icon
        #set image to be splash art of most played champion from last 20 games
        embed.set_thumbnail(url=summonerdetails['profilepic']) #url for profile pic
        embed.set_image(url=summonerdetails['favchampion_splash'])# url for splashart
        
        
        embed.add_field(name="Ranked Solo", value=f"{summonerdetails['rank']['solo']['rank']} \n LP: {summonerdetails['rank']['solo']['lp']}" )
        embed.add_field(name="Ranked Flex", value=f"{summonerdetails['rank']['flex']['rank']} \n LP: {summonerdetails['rank']['flex']['lp']}" )
        embed.add_field(name="Champion with highest mastery:", value=summonerdetails['favchampion_name'], inline=False)
        embed.add_field(name="Mastery Level", value=summonerdetails["favchampion_level"] )
        embed.add_field(name="Mastery Points", value=summonerdetails["favchampion_points"] )
        
        
        await ctx.send(embed=embed)
      

    @commands.command(brief=": $leaguehistory [server] [summoner name]", description="Returns match history of the most recent 20 games of the player.")
    async def leaguehistory(self, ctx, server: str, *summonername: str):
        server=server.lower()
        summoner=" ".join(summonername).lower()
        puuid=riotapi.searchsummoner.by_name(summoner, server)['puuid']

        matches=riotapi.summonerStats.matchlist(server, puuid, 5)

        embeds={}

        for i in range(len(matches)):
            embeds[i]=None



        for i in range(len(matches)):
            match=matches[i]
            summary=leaguefn.matchsummary(match, puuid)

            embed = discord.Embed(
            colour=discord.Color.from_str(summary['color']),
            title=f"{summary['name']} • {summary['status']}",
            # description=f"Items:\n{summary['items']}",
            url=f"https://www.google.com/search?q={summary['status']}+meaning")          

            embed.set_thumbnail(url=str(datadragon.champion.square(summary['championName']))) #url for champion square icon
            embed.set_footer(text=f"{summary['gameid']} • {summary['gameCreation']}")
            embed.add_field(name="Stats", value=f"Champion: {summary['championName']}\nDuration: {summary['gameDuration']}\nKDA: {summary['kda']}\nDamage: {summary['damage']}\nCS: {summary['cs']}\n Gold: {summary['gold']}")
            embed.add_field(name="Items", value=f"{summary['items']}")
            embed.add_field(name="", value="................................................................................................................................",inline=False)

            embeds[i]=embed
        
        await ctx.send(embed=embeds[0])
        await ctx.send(embed=embeds[1])
        await ctx.send(embed=embeds[2])
        await ctx.send(embed=embeds[3])
        await ctx.send(embed=embeds[4])





        
async def setup(bot):
    await bot.add_cog(League(bot))


#tester
# summonerdetails=leaguefn.profile("eun1", "kootiepai")



#example of a help text in function
#    @commands.command(brief=": $leagueprofile [server] [summoner name]", description="")
#     async def leagueprofile(self, ctx, server: str=commands.parameter(default="this is default", description="this is description"), *summonername: str):
  

#descriptions
# description="""
# The command requires you to put in two parameeters



# $leagueprofile [server] [summonername]



# server corresponds to the league servers [refer to the server list below]

# summonername refers to the players in game name(not their riot id but their name in league)      



# server list:

# BR1     Brazil

# EUN1    Europe Nordic & East

# EUW1    Europe West

# JP1         Japan

# KR          Republic of Korea

# LA1         Latin America North

# LA2         Latin America South

# NA1         North America

# OC1         Oceania

# TR1         Turkey

# RU          Russia

# PH2         The Philippines

# SG2         Singapore, Malaysia, & Indonesia

# TH2         Thailand

# TW2         Taiwan, Hong Kong, and Macao

# VN2         Vietnam
# """


