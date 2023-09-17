
![anime cat greeting](/extras/cat_greeting.jpg)

# Kootiepai

Welcome to the source code for kootiepai. The files below are what essentially gives kootiepai it's life. It's devolopment started in September 2023 starting out as a curious project to see how discord bots work to being fully hooked on the idea of bringing the two things I adored at that point in time; League of Legends (yes I know I have issues for liking this game pls don't judge :c) and Discord. I practically spent half my life on discord so why not have something to leave a mark I suppose... and mainly because Google bullied my PC :). I am looking towards adding valorant integration as well only after I get a decent progress in getting the hang of the league api.

# Actual intro
Get jebaited!

kidding

Kootiepai uses the bot module instead of using the client module as you'd see in the quick start guide (from September 2023, hopefully they include more examples cause it killed me to figure out how to use this module or maybe I'm just stupid). it loads the cogs onto the main kootiepai.py files and then does the computational magic to bring the bot to life.

# Version

### version info
XX.Y.AAA.BBBBB

XX => major update [includes implementing new api or something really big]

Y => experimental or released [0 is experimental 1 is released]

AAA => minor updates [mostly includes new functions with existing modules]

BBBB => patces and quality of life updates




# Files

Alist of all the files used and short description on their functionality.




## .env file

The .env file should contain your riot API (used in the riotapi.py file only)
and the bot token from discord bot (only used once in kootiepai.py for establishing the connection)




## kootiepai.py
This file is the main file for running kootiepai. This file is responsible for loading the cogs into kootiepai upon startup




## riot

This folder contains the files that fetches the the data from riot servers using the responses library and works with Jason files.


### riotapileague.py

This file contains the functions to interact with the league of legends part of the riot API focussed on all things league


### riotapivalorant.py

This file interacts with the valorant part of the riot API


### datadragon.py

Used to interact with the riot's centralized database for league named "DataDragon"




## cogs

Contains all the cog files for Kootiepai 


### league.py

Contains the bot commands that are used to get information related to league


### valorant.py

Contains the commands to get information related to Valorant. 



## extras

Contains extra Files that are used as personal pointers  are only here for the time being and will be deleted <3
don't ask me why they are there I legit don't even know why some things exist there 

P.S. thanks for taking the time to read this I apologize for the unprofessional comments but this is meant to be a fun side project so here it is in the future if I ever do come back maybe I'll use my brains then to make it sound more professional 























