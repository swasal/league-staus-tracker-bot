#imports
from os import getenv
from dotenv import load_dotenv
import requests


#getting the api from local machine 
f=open("apikey.txt", "r")
api=f.readline()
f.close()

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


    def bu_sumonnerID(summoner_id, server):
        
        payload={"api_key":api}
        url= "https://"+ server +".api.riotgames.com/lol/summoner/v4/summoners/"+ summoner_id
        r=requests.get(url, params=payload)
        return r.json()

    def by_accountID(account_ID, server):

        payload={"api_key":api}
        url= "https://" + server + ".api.riotgames.com/lol/summoner/v4/summoners/by-account/" + account_ID    
        r=requests.get(url, params=payload)
        return r.json()


#testing






