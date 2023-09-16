#imports
from os import getenv
from dotenv import load_dotenv
import requests


#getting the api from local machine 
load_dotenv()
api=getenv("riotAPI")

class searchsummoner:
    """Search a sumonner by different keys.
    
    ***for testing the putp[ut***
    example code:

        for k,v in searchsummoner.bu_sumonnerID(summonerID, server).items():
        print(k,v)
    
    
    """

    def by_name(summoner_name, server):
        
        payload={"api_key":api}
        url= "https://"+ server +".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ summoner_name
        r=requests.get(url, params=payload)
        return r.json()


    def by_sumonnerID(summoner_id, server):
        
        payload={"api_key":api}
        url= "https://"+ server +".api.riotgames.com/lol/summoner/v4/summoners/"+ summoner_id
        r=requests.get(url, params=payload)
        return r.json()

    def by_accountID(account_ID, server):

        payload={"api_key":api}
        url= "https://" + server + ".api.riotgames.com/lol/summoner/v4/summoners/by-account/" + account_ID    
        r=requests.get(url, params=payload)
        return r.json()




class summonerStats:
    "used to access the player's profile stats history"
    def highestmastery(id, server):
        """highestmastery(id, server)
        returns stats for highest mastery champion"""
        url="https://"+str(server)+".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+str(id)+"?api_key="+str(api)
        r=requests.get(url)
        r=r.json()
        return r[0]
    

    def rank(summonerID: str, server):
        "returns ranked in solo and flex"
        url="https://"+server+".api.riotgames.com/lol/league/v4/entries/by-summoner/"+summonerID+"?api_key="+api
        r=requests.get(url).json()
        ranked={'flex':{}, 'solo':{}}
        if len(r)==0:
            ranked['flex']['rank']="Unranked"
            ranked['flex']['lp']="0"
            ranked['solo']['rank']="Unranked"
            ranked['solo']['lp']="0"

        elif len(r)==1:
            #only one rnaked queue hence set the other rank to none
            #finsing out which one is available RANKED_SOLO_5x5 or RANKED_FLEX_SR
            if r[0]['queueType']=="RANKED_SOLO_5x5": #set flex to none
                ranked['flex']['rank']="Unranked"
                ranked['flex']['lp']="0"
                ranked['solo']['rank']=r[0]['tier']+" "+ r[0]['rank']
                ranked['solo']['lp']=str(r[0]['leaguePoints'])

            if r[0]['queueType']=="RANKED_FLEX_SR": #set solo to none
                ranked['flex']['rank']=r[0]['tier']+" "+ r[0]['rank']
                ranked['flex']['lp']=str(r[0]['leaguePoints'])
                ranked['solo']['rank']="Unranked"
                ranked['solo']['lp']="0"

        else: #set ranked stats len==2
            if r[0]['queueType']=="RANKED_SOLO_5x5": #set flex to none
                ranked['flex']['rank']=r[1]['tier']+" "+ r[1]['rank']
                ranked['flex']['lp']=str(r[1]['leaguePoints'])
                ranked['solo']['rank']=r[0]['tier']+" "+ r[0]['rank']
                ranked['solo']['lp']=str(r[0]['leaguePoints'])


            else:
                ranked['flex']['rank']=r[0]['tier']+" "+ r[0]['rank']
                ranked['flex']['lp']=str(r[0]['leaguePoints'])
                ranked['solo']['rank']=r[1]['tier']+" "+ r[1]['rank']
                ranked['solo']['lp']=str(r[1]['leaguePoints'])



        return ranked


    def matches():
        pass




class Spectate:
    "get live stats on summoner"




# # testing codes here
# z=summonerStats.rank("XdhH7yDClPMA-H7BqTVxxV-QOsg4_fIhieMHAufc4LS8xUI","eun1")
# # # for k,v in z.items():
# # #     print(k,"  ", v)
# print(z)
# print(z['flex']['rank'])




