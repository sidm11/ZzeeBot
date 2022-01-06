# Zzee selfbot
Discord.py selfbot
Version: 1.0
## ATTENTION!
we are not responsible for your discord account!
this program violates the ToS discord rules!
your discord account may be blocked!

happy use! <3

# How do I get my token?
<img src="BigweldIndustries.gif" width="1000">

# about this bot
this bot is for discord account.
this program was written completely from scratch in disnake.py (discord.py)
this program is still in alpha testing, there may be bugs ...
good luck using it!

# How to install and run?
```py
# Linux
git clone https://github.com/KOTE-debug/zzeeBot
cd bot && python start.py
```
# How do I import my team into the bot?
there are 2 ways:
1.via cogs
2.addle to the main file

# Way 1

Open bot/data/account.json
change the parameter "cogs" and add to ["fun.py", "activity.py"]
your file to get it:
```py
["fun.py", "activity.py", "myfile.py"]
```
! Attention! don't forget about square brackets

now create a new file along the path: bot / cogs
let's call it as you indicated in the config!

and insert there:
```py
# imports
import discord, pyfiglet
from discord.ext import commands as zzee 
# class
class name(zzee.Cog):
    def __init__(self, zzee):
        self.zzee = zzee
#commands
        
@zzee.command()
async def commandName(self, ctx):
    await ctx.send("hello world!") #you code

def setup(zzee):
    zzee.add_cog(mass(zzee))
```
# way 2
bot/start.py
now we open the start.py file
and insert the following code there:
```py
@zzee.command()
async def commandName(ctx):
    await ctx.send("hello world!") #you code
```
and yes, you probably think "why cogs? if you can use option 2."
1 option is better than 2
because the cogs are automatically updated, that is, you do not need to restart the bot every time + the bot starts up faster with them.
choice with yours.

# varibles
| {name} | info | |
| {__token__} | send your token | |
