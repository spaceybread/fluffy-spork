import discord
import discord
from discord.ext import commands
from discord import app_commands
from tokens import discordToken
from impls import *

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)

client = MyClient()

@client.event
async def on_ready():
    print(f"OogaBooga")
    

@client.tree.command(name="cowsay", description="Send a cow message to a specified channel")
@app_commands.describe(channel="The channel to send the message to", message="The message to send")
async def cowsay(interaction: discord.Interaction, channel: discord.TextChannel, message: str):
    out = cowsayCLI(message)

    await channel.send(out)
    await interaction.response.send_message(f"Message sent to {channel.mention}", ephemeral=True)

@client.tree.command(name="figlet", description="Convert text to a large ascii thing")
@app_commands.describe(channel="The channel to send the message to", message="The message to send")
async def figlet(interaction: discord.Interaction, channel: discord.TextChannel, message: str):
    out = figletCLI(message)

    await channel.send(out)
    await interaction.response.send_message(f"Message sent to {channel.mention}", ephemeral=True)

client.run(discordToken)
