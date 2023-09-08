#imports
from riotapi import searchsummoner


#init vars

name= "swasal" #sumonner name
summonerID = "wnglMOPBVgSwCfje1Q4Ab6N2YAtBJ9QK-im7CuQw7OJwBmw"
accountID = "9vurag-R6Hz2QmovgTendZwRsJGWr_9Jca0T5XPrQHuBeKA"
server= "eun1" #check https://developer.riotgames.com/docs/lol#data-dragon_regions for region codes

#codes

for k,v in searchsummoner.by_accountID(accountID, server).items():
    print(k,v)
