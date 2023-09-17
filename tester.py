# #imports
# from riot.riotapi import searchsummoner
# # import riot.datadragon as datadragon
# import datetime


abc="abcdef"
#init vars

name= "kootiepai" #sumonner name
summonerID = "wnglMOPBVgSwCfje1Q4Ab6N2YAtBJ9QK-im7CuQw7OJwBmw"
accountID = "9vurag-R6Hz2QmovgTendZwRsJGWr_9Jca0T5XPrQHuBeKA"
server= "eun1" #check https://developer.riotgames.com/docs/lol#data-dragon_regions for region codes
puuid="-uzcGyaoBjG7k3fGrHB8Bttg3lTsXaAa7N0U0H89D5wbWqxQjdkW_G_5LiVCY5N8mf_vQjGdwfF20g"
#codes

# for k,v in searchsummoner.by_name(name, server).items():
# #     print(k,v)


# a=datetime.datetime.fromtimestamp(1694755285)
# print(a)


# embed.add_field(name="Items", value=f"{summary['items']}")


out=""
# for i in range(0,6):
#     out+=f"output['items{i}']= datadragon.gameconstants.itemsname(player['item{i}'])\n"

# for i in range(0,6):


print(out)

raise errors.ExtensionFailed(key, e) from e
discord.ext.commands.errors.ExtensionFailed: Extension 'cogs.league' raised an error: ModuleNotFoundError: No module named 'datadragon'