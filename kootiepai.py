#bot startup file

#imports
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio

load_dotenv()


#initializing bot
def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot=commands.Bot(command_prefix="$", intents=intents)

    @bot.event
    async def on_ready():
        print("Kootiepai is loading extensions.... ~ <3\n PS U DIDNT FIX THE ISSUE WITH THE ITEMS IN LEAGUE HOSTORY <3")
        for filename in os.listdir("./cogs"):
            print(filename)
            if filename.endswith(".py") and filename != "__init__.py":
                # cut off the .py from the file name
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"added extension: {filename}")

        print("Kootiepai has sucessfully loaded all extensions! ~ <3")
        print("Kootiepai is now online!! ~ <3")



    print("Kootiepai is booting up... ~ <3")
    bot.run(os.getenv("kootiepai_token"))
    print("Ara ara seems like kootiepai has either shutdown or bot connection has failed ~ @.@")
 



if __name__=="__main__":
    run()
    
