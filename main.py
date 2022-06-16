import discord
import os
import requests
import glob
import random
import urllib.request
from IPython.display import Image,display,Audio
#import requests
#import json

client = discord.Client()

def get_hug():
#  reponse = requests.get("https://api.shinobu.host/api/v1/action/hug")
#  json_data = json.loads(response.image)
  hug = requests.get("https://api.shinobu.host/api/v1/action/hug")
  print(hug)

  # if(hug["media_type"] == "image"):
  #   title = d + "_" + hug["title"].replace(" ","_").replace(":","_") + ".gif"

  #   image_dir = "./Hug_Images"

  #       #Checking if the directory already exists?
  #   dir_res = os.path.exists(image_dir)

  #       #If it doesn't exist then make a new directory:
  #   if (dir_res==False):
  #     os.makedirs(image_dir)

  #       #If it exist then print a statement:
  #   else:
  #     print("Directory already exists!\n")

  #       #POINT E:
  #       #Retrieving the image:
  #   urllib.request.urlretrieve(url = hug["hdurl"] , filename = os.path.join(image_dir,title))

  #       #POINT F:
  #       #Displaying information related to image:

  #   if("date" in hug.keys()):
  #     print("Date image released: ",hug["date"])
  #     print("\n")
  #   if("copyright" in hug.keys()):
  #     print("This image is owned by: ",hug["copyright"])
  #     print("\n")
  #   if("title" in hug.keys()):
  #     print("Title of the image: ",hug["title"])
  #     print("\n")
  #   if("explanation" in hug.keys()):
  #     print("Description for the image: ",hug["explanation"])
  #     print("\n")
  #   if("hdurl" in hug.keys()):
  #     print("URL for this image: ",hug["hdurl"])
  #     print("\n")

  #       #POINT G:
  #       #Displaying main image:
  #   display(Image(os.path.join(image_dir,title)))

# const love = require('discord_love');
# const { Client, Intents } = require('discord.js');
# const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

@client.event
async def on_ready():
  print('We have logged in as {0.user}', format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # if (message.content == 'kiss') {
  #   message.channel.send(love.kiss())
  # }
  if message.content.startswith('$hug'):
    
    #hugs = glob.glob("https://api.shinobu.host/api/v1/action/hug") # this wil get all the file paths in the foldes.
    urls = "https://api.shinobu.host/api/v1/action/hug"
  # ['FULL_PATH_HERE/1.gif', 'FULL_PATH_HERE/2.jpg']
    #the_hug = random.choice(hugs)
    embed = discord.Embed()#url=random.choice(urls))
    #ctx.send(file = discord.File(the_hug))
    embed.description = "https://api.shinobu.host/api/v1/action/hug"
    await message.channel.send(embed=embed)
    #huggif = get_hug()
    #await message.channel.send(huggif)
    


client.run(os.getenv('TOKEN'))