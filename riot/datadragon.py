"""Used to interact with riot's centralized database for league.
refer to => https://developer.riotgames.com/docs/lol#data-dragon

***NOTE***
This uses their online databse with the requests library.
"""

#imports
import requests

#checking for the latest datadragon version
url="https://ddragon.leagueoflegends.com/api/versions.json"
r=requests.get(url)
version= r.json()[0]

#functions
class profile:
    """Initializing the python"""
    def icon(id):
        "returns url to profile icon of the given id"
        url="http://ddragon.leagueoflegends.com/cdn/"+str(version)+"/img/profileicon/"+str(id)+".png"
        return url

class champion:
    """Functions used to ahndle champions"""
    def name(championID):
        championID=str(championID)
        "returns champion anme of given champion id"
        url="http://ddragon.leagueoflegends.com/cdn/13.18.1/data/en_US/championFull.json"
        r=requests.get(url).json()["keys"]
        name=r[championID]
        return str(name)
    
    def splashart(name):
        "returns url of champion splash art"
        url="http://ddragon.leagueoflegends.com/cdn/img/champion/splash/"+name+"_0.jpg"
        return url



##tester codes ***DELETE THESE***
# print(champion.name(25))
# print(champion.splashart("Morgana"))

