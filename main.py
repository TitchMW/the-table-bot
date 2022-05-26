import discord
import discord.ext
import discord.utils
from discord.ext import commands
import random

client = discord.Client()
client = commands.Bot(command_prefix = '!', help_command=None)


#Ready Message
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name='Monitoring the Table...'))
    print("The Table's Saviour is here!")


@client.command()
async def about(ctx):
  embed = discord.Embed(colour=discord.Colour.blue(), title=f"The Table Bot",
  description="Welcome to The Table! This bot is supposed to be a bot to expand over time with new features based around the Table and its people! If you have any suggestions, please let the Director know! \n - Titch")
  await ctx.send(embed=embed)

@client.command()
async def slander(ctx):
  list_of_insults = ["Sherwood when he gets called a Dwarf for the 5000th time : ", 
                    "Roni when he gets called an AI : ",
                    "When people don't recognise Ethan is an Emo : ",
                    "Luke when you don't think the Conservatives are the best party ever : ",
                    "Luke when you call him a Tory : ",
                    "Sherwood when he finds out he isnt 5'4 : ",
                    "Tom when his blood tests come back positive for Hepatitis A-Z : ",
                    "Luke when you don't have a parliment election to decide who sits where on the Table : ",
                    "Eric is a gink (Summer and Felix's Suggestion)",
                    "Sherwood when he gets paralysed from sitting on the Music Room floor : ",
                    "Roni when you call him Vector : ",
                    "The Table when they get no bitches : "
                    ]
  
  list_of_gifs = ["https://c.tenor.com/qPYHhhSw638AAAAC/slander-meme.gif",
                  "https://c.tenor.com/QUNe_w_zZ5EAAAAd/slander.gif",
                  "https://c.tenor.com/7xkComI9yxkAAAAS/solluminati-sol.gif",
                  "https://c.tenor.com/DyPndE43z8gAAAAM/slander-tiktok.gif",
                  "https://c.tenor.com/IwCWDIxnqcwAAAAM/tiktok-tiktok-slander.gif"
                  ]
  
  embed = discord.Embed(color=discord.Color.blurple(), title="Table Slander",
  description=random.choice(list_of_insults))

  embed.set_image(url=random.choice(list_of_gifs))
  
  await ctx.send(embed=embed)


client.run("OTc5MTE5Mzc1MDM2NjEyNjM5.GFwEdB.UOcgSCFGWROYrM-2Cvry24cYUBVYL-DaleJlmI")