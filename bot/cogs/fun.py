import discord, pyfiglet, requests, random, string, aiohttp, io, hashlib, base64
from discord.ext import commands as zzee

class Fun(zzee.Cog):
    def __init__(self, zzee):
        self.zzee = zzee
 

    @zzee.command()
    async def slap(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} slapped {user.mention}!**", color=0x0000)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

        
    @zzee.command()
    async def hug(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} hugged {user.mention}!**", color=0x0000)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

        
    @zzee.command(aliases=['dong', 'penis'])
    async def dick(self, ctx, *, user: discord.User = None):
        await ctx.message.delete()
        if user is None:
            user = ctx.author
        size = random.randint(1, 50)
        dong = ""
        for _i in range(0, size):
            dong += "="
        em = discord.Embed(title=f"{user}'s Dick size:", description=f"8{dong}D", colour=0x0000)
        await ctx.send(embed=em)
    

    
    
    @zzee.command()
    async def kiss(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} kissed {user.mention}!**", color=0x0000)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)
     
   
    
    @zzee.command()
    async def panda(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/panda").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Panda.", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
        embed.set_image(url=str(r["link"]))
        await ctx.send(embed=embed)    
    
    
    @zzee.command()
    async def meme(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/meme").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Meme.", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
        embed.set_image(url=str(r["image"]))
        await ctx.send(embed=embed)

        
    @zzee.command()
    async def cat(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/cat").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Cat.", icon_url="https://cdn.discordapp.com/attachments/796868392095186976/810566027637162034/zeenode_cat.png") 
        embed.set_image(url=str(r["link"]))
        await ctx.send(embed=embed)   
    
    
    @zzee.command()
    async def dog(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://some-random-api.ml/img/dog").json()
        embed = discord.Embed(color=0x0000)
        embed.set_author(name="Random Dog." , icon_url="https://cdn.discordapp.com/attachments/796868392095186976/810566380545114172/zeenode_dog.png") 
        embed.set_image(url=str(r["link"]))
        await ctx.send(embed=embed)    


    @zzee.command()
    async def nitro(self, ctx):
            await ctx.message.delete()
            await ctx.send(Nitro())
            
	@zzee.command()
	async def ascii(self, ctx, arg):
		text = pyfiglet.figlet_format(arg)
		await ctx.send(f"```\n{text}\n```")
    @zzee.command()
    async def embed(self, ctx, *, description):
        await ctx.message.delete()
        embed = discord.Embed(description=description, color=0x0000)
        await ctx.send(embed=embed)
		
def Nitro():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 4)))
def setup(zzee):
    zzee.add_cog(Fun(zzee))
