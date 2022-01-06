# -*- coding: UTF-8 -*-
import os
def install(package):
	if os.name == "nt":
		os.system("{sys.executable} -m pip install {package}")
		os.system("cls")
		print(f"{package} installed!")
	if os.name == "posix":
		os.system(f"pip install {package}")
		os.system("clear")
		print(f"{package} installed!")
try:
	import ast
except ModuleNotFoundError:
	install("ast")
try:
    import discord
except ModuleNotFoundError:
	install("disnake")

try:
    import requests
except ModuleNotFoundError:
    	install("requests")
    	
try:
    import time
except ModuleNotFoundError:
    	install("time")
try:
    import json
except ModuleNotFoundError:
    	install("json")
try:
    import pyfiglet
except ModuleNotFoundError:
    	install("pyfiglet")
try:
    import colorama
except ModuleNotFoundError:
    	install("colorama")
try:
	import subprocess
except ModuleNotFoundError:
		install("subprocess")
from datetime import datetime
from discord.ext import commands, tasks
from colorama import Fore, Back, Style
import sys
colorama.init()
print(Fore.MAGENTA)
__logo__ = pyfiglet.figlet_format("zzeeBot")
__lastRun__ = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
__starttime__ = time.time()
open("logs/info.log", "w").write(" ")
print(Fore.GREEN + "Resetting info log.")
open("logs/warning.log", "w").write(" ")
print(Fore.GREEN + "Resetting warning log.")
open("logs/error.log", "w").write(" ")
print(Fore.GREEN + "Resetting error log.")
open("logs/critical.log", "w").write(" ")
print(Fore.GREEN + "Resetting critical log.")
time.sleep(2)
os.system("clear")
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
logging.basicConfig(filename="logs/error.log", level=logging.ERROR)
logging.basicConfig(filename="logs/warning.log", level=logging.WARNING)
logging.basicConfig(filename="logs/info.log", level=logging.INFO)
accountJson = json.load(open("data/account.json"))
accountFile = open("data/account.json", "r").read()
__token__ = accountJson["token"]
__cogs__ = accountJson["cogs"] #["name1.py", "start.py"]
__prefix__ = accountJson["prefix"] #+
__logsID__ = accountJson["logsID"] #channel ID
__ownerID__ = accountJson["ownerID"] #owner user id
nitrosnipestatus = False
class zzee(commands.Bot):
    def shell(code):
        return subprocess.check_output(code, shell=True).decode("utf-8")
zzee=commands.Bot(command_prefix=__prefix__, selfbot=True)
for filename in __cogs__:
  if filename.endswith('.py'):
    zzee.load_extension(f'cogs.{filename[:-3]}')
  else:
    print(f'failed load cog {filename[:-3]}')

@zzee.event
async def on_ready():
	print(Fore.MAGENTA + __logo__)
	await zzee.get_channel(int(__logsID__)).send('<ZzEE bot> zzee started!')
	open("runinfo.log", "w").write(f"last run: {__lastRun__}\n run time: %s seconds" % (time.time() - __starttime__))
	print(Fore.GREEN + "runinfo edited!")
	print(Fore.GREEN + "prefix: " + __prefix__)
	print("account name: " + zzee.user.name)
	print("bot started!")
	
@zzee.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
        await zzee.get_channel(int(__logsID__)).send(f'<ZzEE bot> [error] missing arguments: {error}')
        await ctx.send(f"missing arguments: {error}")
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
        await zzee.get_channel(int(__logsID__)).send('<ZzEE bot> [error] discord error: \n```py\n{error}\n```')
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)
        await ctx.send(f"error! ```py\n{error_str}\n```")
        await zzee.get_channel(int(__logsID__)).send(f'<ZzEE bot> [error] error!:\n```py\n{error}\n```')

def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])
        if isinstance(body[-1], ast.If):
            insert_returns(body[-1].body)
            insert_returns(body[-1].orelse)
        if isinstance(body[-1], ast.With):
            insert_returns(body[-1].body)

@zzee.command()
async def e(ctx, *, cmd):
    if ctx.author.id in [int(__ownerID__)]:
        try:
            fn_name = "_eval_expr"
            cmd = cmd.strip("` ")
            cmd = "\n".join(f" {i}" for i in cmd.splitlines())
            body = f"async def {fn_name}():\n{cmd}"
            parsed = ast.parse(body)
            body = parsed.body[0].body
            insert_returns(body)
            env = { 'bot': bot, 'discord': discord, 'commands': commands, 'ctx': ctx, '__import__': __import__ }
            exec(compile(parsed, filename="<ast>", mode="exec"), env)
            result = (await eval(f"{fn_name}()", env))
        except Exception as error:
            emb = discord.Embed(title="{error.__class__name__}", description=error, color=discord.Color.red())
            await ctx.send(embed=emb)
            print(f"[EVAL ERROR] error: {error}")
    else:
        await ctx.send("no prems!")   

@zzee.command()
async def nitrosnipe(ctx, arg):
    global nitrosnipestatus
    thing = arg
    await ctx.message.delete()
    if thing == "on":
        nitrosnipestatus = True
    if thing == "off":
        nitrosnipestatus = False

@zzee.event
async def on_message(message):
    global nitrosnipestatus
    if nitrosnipestatus == True:
        if codeRegex.search(message.content):
            code = codeRegex.search(message.content).group(2)
            start_time = time.time()
            async with httpx.AsyncClient() as client:
                result = await client.post(
                'https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem',
                json={'channel_id': str(message.channel.id)},
                headers={'authorization': TOKEN, 'user-agent': 'Mozilla/5.0'})
                delay = (time.time() - start_time)
                if 'This gift has been redeemed already' in str(result.content):
                    print(Fore.YELLOW+f"We found a code but it was redeemed already ({code}, delay of {delay})")
                elif 'nitro' in str(result.content):
                    print(Fore.GREEN+f"We found a code and claimed it! ({code}, delay of {delay})")
                elif 'Unknown Gift Code' in str(result.content):
                    print(Fore.RED+f"We found a code but it was invalid ({code}, delay of {delay})")
zzee.run(__token__)