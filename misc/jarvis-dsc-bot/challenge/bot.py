# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from time import sleep

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

try:
    with open('/app/flag.txt', 'r') as r:
        FLAG = r.read().strip()
except FileNotFoundError:
    FLAG = os.getenv('FLAG', 'bts{tmpflag}')

prefix = "!!"
accepted_role = "Mr.Stark"
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print('### Working as {0.user}'.format(bot))

@commands.guild_only()
@bot.command()
async def secret(ctx):
    role = discord.utils.get(ctx.guild.roles, name=accepted_role)
    if role in ctx.author.roles:
        await ctx.send(f"Here is secret for you, sir: `{FLAG}`")
    else:
        await ctx.send(f":no_entry_sign: I am sorry {ctx.author.mention}, but you have no power of `{accepted_role}` here")

@commands.guild_only()
@bot.command()
async def armor(ctx):
    role = discord.utils.get(ctx.guild.roles, name=accepted_role)
    if role in ctx.author.roles:
        await ctx.send(f"You armor will be delivered shortly, sir.")
        sleep(0.5)
        await ctx.send(f"Safe journey {ctx.author.mention}. :rocket:")
    else:
        await ctx.send(f"You armor will be delivered shortly, sir.")
        await ctx.send(f":no_entry_sign: Wait {ctx.author.mention}, you are not `{accepted_role}` :no_entry_sign:")
    
@commands.guild_only()
@bot.command()
async def friday(ctx):
    role = discord.utils.get(ctx.guild.roles, name=accepted_role)
    if role in ctx.author.roles:
        await ctx.send(f"Check this out: https://www.youtube.com/watch?v=cjgldht4PKw")
    else:
        await ctx.send(f":no_entry_sign: I am sorry {ctx.author.mention}, but you have no power of `{accepted_role}` :no_entry_sign:")

@commands.guild_only()
@bot.command()
async def ultron(ctx):
    await ctx.send(f":shield: Thanks to {ctx.author.mention}, the Earth will have it's own shield :shield:")

@commands.guild_only()
@bot.command()
async def vision(ctx):
    await ctx.send(f":superhero: Hi {ctx.author.mention}, you can call me Vision from now on :superhero:")

@commands.guild_only()
@bot.command()
async def grid(ctx):
    await ctx.send(f":flag_no: No worries. I'll hide in the Grid, sir :flag_no:")

@commands.guild_only()
@bot.command()
async def help(ctx):
    help_desc = f"Here is a little help for you, sir. Available of commands can be seen below."
    e = discord.Embed(title=":question: Help :question:", description=help_desc)

    avengers = f"""\
`{prefix}ultron` - protect the Earth
`{prefix}vision` - turn into Vision 
`{prefix}grid` - hide in the Internet
    """
    e.add_field(name="***Avengers***", value=avengers)

    stark = f"""\
`{prefix}armor` - summon Mr. Stark's armor
`{prefix}friday` - call for replacement
`{prefix}secret` - reveal one of Mr. Stark's secrets
    """
    e.add_field(name="***Stark***", value=stark)

    await ctx.send(embed=e)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        e = discord.Embed(title=":exclamation: No such command :exclamation:", description="Try `!!help`")
        await ctx.send(embed=e)
    elif "403 Forbidden" in error:
        return
    else:
        print(f"---- Unknown error: {error} ----")
        return

bot.run(TOKEN)