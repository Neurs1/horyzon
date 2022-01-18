from __future__ import unicode_literals

def main():
  #AUTH

  #https://discord.com/api/oauth2/authorize?client_id=897651922163626076&permissions=0&scope=bot%20applications.commands

  #-----------------------------------------------------------------

  #IMPORT PRE-INSTALLED MODULE

  from os import getenv, system

  #-----------------------------------------------

  #IMPORT MODULES

  try:
    from nextcord import Member, Activity, ActivityType, Status, Intents, Interaction
    from nextcord.ext import commands
    from discord_together import DiscordTogether
  except:
    system("pip install -U nextcord yt-dlp pynacl discord-together youtube-search-python nest_asyncio flask")
    from nextcord import Member, Activity, ActivityType, Status, Intents, Interaction
    from nextcord.ext import commands
    from discord_together import DiscordTogether

  #-----------------------------------------------

  #Components

  from horyzon.components.yt import Play, Stop, Pause, Resume, Skip
  from horyzon.components.other import Author, Version
  from horyzon.components.together import Together
  from horyzon.components.info import Info
  from horyzon.components.JandM import Meme
  from horyzon.components.mci import Mci
  from horyzon.components.werewolf import JoinWereWolf, Kill, Vote, LeaveWW

  #-----------------------------------------------

  intents = Intents.default()
  intents.members = True

  global TOKEN
  TOKEN = getenv("TOKEN")
  bot = commands.Bot(command_prefix= "!", case_insensitive=True, activity = Activity(type=ActivityType.listening, name="music | Neurs"), intents=intents, status=Status.idle)

  bot.remove_command('help')

  @bot.slash_command(name="play",
    description="Play music from YouTube video or SoundCloud (Support search on YouTube)",
    guild_ids=[guild.id for guild in bot.guilds])
  #@commands.cooldown(1, 10, commands.BucketType.user)
  async def play(ctx: Interaction, *, url):
    await Play(ctx, url, bot)

  @bot.slash_command(name="kill",
    description="Werewolf game command.",
    guild_ids=[guild.id for guild in bot.guilds])
  async def kill(ctx, player: Member):
    await Kill(ctx, player)

  @bot.slash_command(name="vote",
    description="Werewolf game command.",
    guild_ids=[guild.id for guild in bot.guilds])
  async def vote(ctx, player: Member):
    await Vote(ctx, player)

  @bot.slash_command(name="lww",
    description="Leave Werewolf game.",
    guild_ids=[guild.id for guild in bot.guilds])
  async def lww(ctx):
    await LeaveWW(ctx)

  @bot.slash_command(name="jww",
    description="Join in a Werewolf game! (4 players minimum)",
    guild_ids=[guild.id for guild in bot.guilds])
  async def joinwerewolf(ctx):
    await JoinWereWolf(ctx, bot)

  @bot.slash_command(name="mci",
    description="Get information about a name in Minecraft or check the availability of the name",
    guild_ids=[guild.id for guild in bot.guilds])
  async def mci(ctx, name):
    await Mci(ctx, name)

  @bot.slash_command(name="meme",
    description="Generate a random Meme from Reddit!",
    guild_ids=[guild.id for guild in bot.guilds])
  async def meme(ctx):
    await Meme(ctx)

  @bot.slash_command(name="info",
    description="Get info of yourself or a member in your Discord guild",
    guild_ids=[guild.id for guild in bot.guilds])
  async def info(ctx, name: Member = None):
    await Info(ctx, name)

  @bot.slash_command(name="stop",
    description="Stop current track and clear queue",
    guild_ids=[guild.id for guild in bot.guilds])
  async def stop(ctx):
    await Stop(ctx)
  
  @bot.slash_command(name="skip",
    description="Skip queue to next track",
    guild_ids=[guild.id for guild in bot.guilds])
  async def skip(ctx):
    await Skip(ctx)

  @bot.slash_command(name="pause",
    description="Pause current track",
    guild_ids=[guild.id for guild in bot.guilds])
  async def pause(ctx):
    await Pause(ctx)

  @bot.slash_command(name="resume",
    description="Resume current track",
    guild_ids=[guild.id for guild in bot.guilds])
  async def resume(ctx):
    await Resume(ctx)

  @bot.slash_command(name="author",
    description="Info about author",
    guild_ids=[guild.id for guild in bot.guilds])
  async def author(ctx):
    await Author(ctx)

  @bot.slash_command(name="version",
    description="View current version of the bot and check for new features!",
    guild_ids=[guild.id for guild in bot.guilds])
  async def version(ctx):
    await Version(ctx)

  @bot.slash_command(name="together",
    description="Lauch an activity on your Discord server!",
    guild_ids=[guild.id for guild in bot.guilds])
  #@commands.cooldown(1, 10, commands.BucketType.user)
  async def together(ctx):
    await Together(ctx, bot)
    
  #@bot.listen('on_message')
  #async def a(message):

  @bot.event
  async def on_ready():
    global TOKEN
    bot.togetherControl = await DiscordTogether(TOKEN)
    system("clear")
    print("Connected to Discord")
    
  bot.run(TOKEN)

if __name__ == "__main__":
  main()
