# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord import app_commands
from discord.ext import commands

import random
from dotenv import load_dotenv
from os import getenv

from pokemon_api import PokemonApi
from utils import get_pokemon_info

load_dotenv()
description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

GUILD = discord.Object(id=284175704227315712)

@bot.event
async def on_ready():
    try:
        bot.tree.copy_global_to(guild=GUILD)
        synced = await bot.tree.sync(guild=GUILD)
        print(f"Synced {synced} commands")
    except Exception as e:
        print(e)
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

@bot.command(description="Add two numbers")
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.tree.command(name="roll", description="roll dnd style dice")
@app_commands.describe(rolls="number of dice rolls", sides="how many sides on the die")
async def roll(interaction: discord.Interaction, rolls: int, sides: int):
    """Rolls a dice in NdN format."""
    result = ', '.join(str(random.randint(1, sides)) for r in range(rolls))
    print(f"{interaction.user} rolled dice")
    await interaction.response.send_message(result)

@bot.tree.command(name="pokemon", description="lookup the base stats of a pokemon")
@app_commands.describe(pokemon="The pokemon to lookup")
async def pokemon(interaction: discord.Integration, pokemon: str):
    api = PokemonApi()
    r = api.getPokemon(pokemon)
    print(f"{interaction.user} attempted to look up {pokemon}")
    if r.status_code == 404:
        await interaction.response.send_message(f"Could not find {pokemon}", ephemeral=True)
    else:
        data = r.json()
        await interaction.response.send_message(get_pokemon_info(pokemon, data))



@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


bot.run(getenv("TOKEN"))