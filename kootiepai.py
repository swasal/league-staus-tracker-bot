#bot startup file

#imports
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()


#initializing bot
def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot=commands.Bot(command_prefix="$", intents=intents)

    @bot.event
    async def on_ready():
        ## loads all the cogs in to the bot
        for filename in os.listdir("./cogs"):
            print(filename)
            if filename.endswith(".py") and filename != "__init__.py":
                # cut off the .py from the file name
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"added {filename}")



    bot.run(os.getenv("kootiepai_token"))



if __name__=="__main__":
    # run()
    print("Kootiepai is now online!! ~ <3")
