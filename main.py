
import discord
from discord.ext import commands
import os

# Bot setup with intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is nu online!')
    print(f'Bot ID: {bot.user.id}')

@bot.event
async def on_message(message):
    # Negeer berichten van de bot zelf
    if message.author == bot.user:
        return

    # Laat de bot reageren op "hallo"
    if message.content.lower() == 'hallo':
        await message.channel.send(f'Hallo {message.author.mention}!')

    # Verwerk commands
    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    """Test command om te checken of de bot werkt"""
    await ctx.send('Pong!')

@bot.command(name='info')
async def info(ctx):
    """Geeft informatie over de bot"""
    embed = discord.Embed(
        title="Bot Informatie",
        description="Een simpele Discord bot gemaakt in Python!",
        color=discord.Color.blue()
    )
    embed.add_field(name="Gebruiker", value=ctx.author.mention, inline=True)
    embed.add_field(name="Server", value=ctx.guild.name, inline=True)
    await ctx.send(embed=embed)

# Start de bot - je moet je token toevoegen via Secrets
if __name__ == "__main__":
    token = os.getenv('DISCORD_BOT_TOKEN')
    if token:
        bot.run(token)
    else:
        print("DISCORD_BOT_TOKEN niet gevonden! Voeg je bot token toe in Secrets.")
