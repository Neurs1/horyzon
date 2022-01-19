from asyncio import get_event_loop, wait, ALL_COMPLETED, sleep
from concurrent.futures import ThreadPoolExecutor
import asyncio, base64
from json import loads
from threading import Thread
from nextcord import Embed, Colour

async def run(stdout, ctx):
  #Get skin and previous names
  global down_skin, view
  uuid = loads(stdout)["id"]
  username = loads(stdout)["name"]
  proc = await asyncio.create_subprocess_shell(
    f"curl https://sessionserver.mojang.com/session/minecraft/profile/{uuid}",
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE)
  skindata = await proc.communicate()
  skindata = skindata[0].decode()
  skindata = loads(skindata)["properties"][0]["value"]
  skindata = base64.b64decode(skindata)
  skindata = loads(skindata)["textures"]["SKIN"]["url"]
  proc = await asyncio.create_subprocess_shell(
    f"curl https://api.mojang.com/user/profiles/{uuid}/names",
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE)
  namedata = await proc.communicate()
  namedata = namedata[0].decode()
  namedata = loads(namedata)
  namedata = "\n".join(["`"+c["name"]+"`" for c in namedata])
  await ctx.send(embed = Embed(title = username, description =  f"[Download skin]({skindata})", color = Colour.blue()).add_field(name = "Username's UUID:",value = f"`{uuid}`").add_field(name = "Previous names:", value = f"{namedata}", inline = False))

async def checkspec(string):
  if string.isalnum():
    return True
  else:
    #If contains special characters, remove "_" and check again, if False again, return False.
    string = string.replace("_", "")
    if string.isalnum() == False:
      return False
    else:
      return True

#Condition:
#Minecraft username length is 3 - 16
#No special characters, except "_"
async def Mci(ctx, name):
  #Check the requirement
  if len(name) < 16 and await checkspec(name):
    try:
      proc = await asyncio.create_subprocess_shell(
    f"curl https://api.mojang.com/users/profiles/minecraft/{name}",
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE)
      stdout = await proc.communicate()
      t = Thread(target = await run(stdout[0].decode(), ctx))
      t.start()
    except:
      #If API return nothing, that mean the name is not taken.
      await ctx.send(embed = Embed(title = "Username available!", description = "This username hasn't been owned yet, go grab it before someone does!", color = Colour.green()))
  else:
    await ctx.send(embed = Embed(title = "Invalided username", description = "This username contains more than 16 characters or contains special characters!", color = Colour.red()))
