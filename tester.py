#imports
from riot.riotapi import searchsummoner
import riot.datadragon as datadragon

abc="abcdef"
#init vars

name= "Skillful Tongue" #sumonner name
summonerID = "wnglMOPBVgSwCfje1Q4Ab6N2YAtBJ9QK-im7CuQw7OJwBmw"
accountID = "9vurag-R6Hz2QmovgTendZwRsJGWr_9Jca0T5XPrQHuBeKA"
server= "eun1" #check https://developer.riotgames.com/docs/lol#data-dragon_regions for region codes

#codes

for k,v in searchsummoner.by_name(name, server).items():
    print(k,v)

