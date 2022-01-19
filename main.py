import discord
from discord.ext import commands
from discord import Intents
import random

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


TOKEN = 'OTMyNjk2MTk0NzAwOTUxNzA0.YeWvBQ.FD5y0V7b6mBB8MWAs_dYj7aaP38'
client = commands.Bot(command_prefix = '.')




@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(
    type=discord.ActivityType.watching, name="Prefix: ."
  ))
  print("Bot is ready")


test = True

@client.event
async def on_member_join(member):

  embed = discord.Embed(title = "Új sziszakommandó tag!",color = discord.Colour.green())
  embed.set_thumbnail(url=f"{member.avater_url}")
  embed.set_footer(text =f"{member.mention} üdvözöllek a szerveren!")
  await client.get_channel(909028015420370967).send(embed = embed)


@client.command()
async def szar(ctx):
  embed = discord.Embed(title = "Új sziszakommandó tag!",color = discord.Colour.green())
  embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/762925022922539018.webp?size=96&quality=lossless")
  embed.set_footer(text ="Ez az én botom")
  await client.get_channel(933024220470992917).send(embed = embed)


@client.command()
async def seggkitörlés(ctx):
  embed = discord.Embed(title = "Ennek mi értelme?", color = discord.Colour.green())


  embed.set_image(url = 'https://c.tenor.com/cgzki_0z2qkAAAAC/dog-toilet.gif')
  embed.set_footer(text = 'Zeco külön commandja')


  await ctx.send(embed = embed)


@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Ismeretlen parancs.')




@client.command()
async def köpeny(ctx):
  embed = discord.Embed(color = discord.Colour.green())


  embed.set_image(url = 'https://cdn.discordapp.com/attachments/839858413030342696/932705145291145266/Sziszaaa_Kopeny.png')
  embed.set_footer(text = 'sziszakommandó köpeny')

  await ctx.send(embed = embed)



@client.command(case_insensive=True)
async def say(ctx, *, message):
  await ctx.message.delete()
  await ctx.send(f"{message}" .format(message))


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
  await ctx.channel.purge(limit=amount)
  await ctx.send("Üzenetek törölve✅")

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'Sikeresen Kickelve lett {member.mention}')

def is_me(ctx):
  if ctx.message.author.id == 488289002441408512:
      return True
      return False


@client.command()
@commands.check(is_me)
async def höszk(ctx, role:discord.Role, user:discord.Member):
  await ctx.message.delete()
  await user.add_roles(role)
  await ctx.send(f"A rangot sikeresen megkapta {user.mention}.")



@client.command()
@commands.check(is_me)
async def unhöszk(ctx, role:discord.Role, user:discord.Member):
  await user.remove_roles(role)
  await ctx.send(f"Rang sikeresen megvonva {user.mention} felhasználótól")


@client.command()
@commands.check(is_me)
async def hehe(ctx, member: discord.Member, *, reason=None):
  await ctx.message.delete()
  await member.send("Sus2ás valamit nagyon ás")



@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'Sikeresen Bannolva lett {member.mention}')

@client.command()
@commands.check(is_me)
async def mester(ctx):
  await ctx.message.delete()
  await ctx.send("Mondom Kevin a mester.")

@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
  guild = ctx.guild
  mutedRole = discord.utils.get(guild.roles, name="Muted")
  if not mutedRole:
    mutedRole = await guild.create_role(name="Muted")

    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_messages=False, )

  await ctx.message.delete()
  await member.add_roles(mutedRole, reason=reason)
  await ctx.send(f"{member} Muteolva lett {reason} indokkal.")
  await member.send(f'Némítva lettél a szerveren {guild.name} {reason} indokkal.')


@clear.error
async def clear_error(ctx, error):
   if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Helytelen parancs!')

@say.error
async def say_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Helytelen parancs!')


@client.event
async def on_command_error(ctx, error):
  if isinstance(error,commands.MissingPermissions):
    await ctx.send("Nincs jogod ehez")
    await ctx.message.delete()


client.run('OTMyNjk2MTk0NzAwOTUxNzA0.YeWvBQ.FD5y0V7b6mBB8MWAs_dYj7aaP38')

