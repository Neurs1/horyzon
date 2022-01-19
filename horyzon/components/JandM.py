from nextcord import Embed, Colour
import asyncio
from json import loads
from threading import Thread
from random import choice

#Get meme in another thread for JSON module. I'm lazy
async def getmeme(stdout, ctx):
  stdout = loads(stdout)
  await ctx.send(embed = Embed(title = stdout["title"]).set_image(url = stdout["url"]))

async def Meme(ctx):
  await asyncio.sleep(1)
  meme = choice(["holup", "dankmemes", "darkmemers", "memes"])
  proc = await asyncio.create_subprocess_shell(
  f"curl https://meme-api.herokuapp.com/gimme/{meme}",
  stdout=asyncio.subprocess.PIPE,
  stderr=asyncio.subprocess.PIPE)
  stdout = await proc.communicate()
  t = Thread(target = await getmeme(stdout[0].decode(), ctx))
  t.start()
