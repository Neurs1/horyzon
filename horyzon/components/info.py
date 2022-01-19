#This is a very dumb code, just... move along, nothing to see here
from nextcord import Member, Embed
from replit import db
async def Info(ctx, name: Member = None):
  if name == None:
    try:
      db[str(ctx.author.id)]
    except:
      try:
        ctx.author.avatar.url
      except:
        if len(ctx.author.roles) > 1:
          await ctx.send(embed=Embed(title=ctx.author).add_field(name="Roles in "+ctx.guild.name+":", value=", ".join(["<@&"+str(c.id)+"> " for c in ctx.author.roles[1:len(ctx.author.roles)]]), inline=False).add_field(name="Account created at: ", value="`"+str(ctx.author.created_at)[5:7]+"/"+str(ctx.author.created_at)[8:10]+"/"+str(ctx.author.created_at)[0:4]+"`", inline=False))
        else:
          await ctx.send(embed=Embed(title=ctx.author).add_field(name="Account created at: ", value="`"+str(ctx.author.created_at)[5:7]+"/"+str(ctx.author.created_at)[8:10]+"/"+str(ctx.author.created_at)[0:4]+"`", inline=False))
        return
      if len(ctx.author.roles) > 1:
        await ctx.send(embed=Embed(title=ctx.author).set_thumbnail(url=ctx.author.avatar.url).add_field(name="Roles in "+ctx.guild.name+":", value=", ".join(["<@&"+str(c.id)+"> " for c in ctx.author.roles[1:len(ctx.author.roles)]]), inline=False).add_field(name="Account created at: ", value="`"+str(ctx.author.created_at)[5:7]+"/"+str(ctx.author.created_at)[8:10]+"/"+str(ctx.author.created_at)[0:4]+"`", inline=False))
      else:
        await ctx.send(embed=Embed(title=ctx.author).set_thumbnail(url=ctx.author.avatar.url).add_field(name="Account created at: ", value="`"+str(ctx.author.created_at)[5:7]+"/"+str(ctx.author.created_at)[8:10]+"/"+str(ctx.author.created_at)[0:4]+"`", inline=False))
      return
    try:
      ctx.author.avatar.url
    except:
      await ctx.send(embed=Embed(title=ctx.author).add_field(name="Roles in "+ctx.guild.name+":", value=", ".join(["<@&"+str(c.id)+"> " for c in ctx.author.roles[1:len(ctx.author.roles)]]), inline=False).add_field(name="Account created at: ", value="`"+str(ctx.author.created_at)[5:7]+"/"+str(ctx.author.created_at)[8:10]+"/"+str(ctx.author.created_at)[0:4]+"`", inline=False).add_field(name="Horyzon roles: ", value=", ".join(c for c in db[str(ctx.author.id)])))
      return
    if len(ctx.author.roles) > 1:
      await ctx.send(embed=Embed(title=ctx.author).set_thumbnail(url=ctx.author.avatar.url).add_field(name="Roles in "+ctx.guild.name+":", value=", ".join(["<@&"+str(c.id)+"> " for c in ctx.author.roles[1:len(ctx.author.roles)]]), inline=False).add_field(name="Account created at: ", value="`"+str(ctx.author.created_at)[5:7]+"/"+str(ctx.author.created_at)[8:10]+"/"+str(ctx.author.created_at)[0:4]+"`", inline=False).add_field(name="Horyzon roles: ", value=", ".join(c for c in db[str(ctx.author.id)])))
    else:
      await ctx.send(embed=Embed(title=ctx.author).set_thumbnail(url=ctx.author.avatar.url).add_field(name="Account created at: ", value="`"+str(ctx.author.created_at)[5:7]+"/"+str(ctx.author.created_at)[8:10]+"/"+str(ctx.author.created_at)[0:4]+"`", inline=False).add_field(name="Horyzon roles: ", value=", ".join(c for c in db[str(ctx.author.id)])))
  else:
    try:
      db[str(name.id)]
    except:
      try: 
        name.avatar.url
      except:
        if len(name.roles) > 1:
          await ctx.send(embed=Embed(title=name).add_field(name="Roles in "+ctx.guild.name+":", value=", ".join(["<@&"+str(c.id)+"> " for c in name.roles[1:len(name.roles)]]), inline=False).add_field(name="Account created at: ", value="`"+str(name.created_at)[5:7]+"/"+str(name.created_at)[8:10]+"/"+str(name.created_at)[0:4]+"`", inline=False))
        else:
          await ctx.send(embed=Embed(title=name).add_field(name="Account created at: ", value="`"+str(name.created_at)[5:7]+"/"+str(name.created_at)[8:10]+"/"+str(name.created_at)[0:4]+"`", inline=False))
        return
      
      if len(name.roles) > 1:
        await ctx.send(embed=Embed(title=name).set_thumbnail(url=name.avatar.url).add_field(name="Roles in "+ctx.guild.name+":", value=", ".join(["<@&"+str(c.id)+"> " for c in name.roles[1:len(name.roles)]]), inline=False).add_field(name="Account created at: ", value="`"+str(name.created_at)[5:7]+"/"+str(name.created_at)[8:10]+"/"+str(name.created_at)[0:4]+"`", inline=False))
      else:
        await ctx.send(embed=Embed(title=name).set_thumbnail(url=name.avatar.url).add_field(name="Account created at: ", value="`"+str(name.created_at)[5:7]+"/"+str(name.created_at)[8:10]+"/"+str(name.created_at)[0:4]+"`", inline=False))
      return
    try:
      name.avatar.url
    except:
      if len(name.roles) > 1:
        await ctx.send(embed=Embed(title=name).add_field(name="Roles in "+ctx.guild.name+":", value=", ".join(["<@&"+str(c.id)+"> " for c in name.roles[1:len(name.roles)]]), inline=False).add_field(name="Account created at: ", value="`"+str(name.created_at)[5:7]+"/"+str(name.created_at)[8:10]+"/"+str(name.created_at)[0:4]+"`", inline=False).add_field(name="Horyzon roles: ", value=", ".join(c for c in db[str(name.id)])))
      else:
        await ctx.send(embed=Embed(title=name).add_field(name="Account created at: ", value="`"+str(name.created_at)[5:7]+"/"+str(name.created_at)[8:10]+"/"+str(name.created_at)[0:4]+"`", inline=False).add_field(name="Horyzon roles: ", value=", ".join(c for c in db[str(name.id)])))
      return
    if len(name.roles) > 1:
      await ctx.send(embed=Embed(title=name).set_thumbnail(url=name.avatar.url).add_field(name="Roles in "+ctx.guild.name+":", value=", ".join(["<@&"+str(c.id)+"> " for c in name.roles[1:len(name.roles)]]), inline=False).add_field(name="Account created at: ", value="`"+str(name.created_at)[5:7]+"/"+str(name.created_at)[8:10]+"/"+str(name.created_at)[0:4]+"`", inline=False).add_field(name="Horyzon roles: ", value=", ".join(c for c in db[str(name.id)])))
    else:
      await ctx.send(embed=Embed(title=name).set_thumbnail(url=name.avatar.url).add_field(name="Account created at: ", value="`"+str(name.created_at)[5:7]+"/"+str(name.created_at)[8:10]+"/"+str(name.created_at)[0:4]+"`", inline=False).add_field(name="Horyzon roles: ", value=", ".join(c for c in db[str(name.id)])))
