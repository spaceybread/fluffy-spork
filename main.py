import os
import time
import discord
from discord.ext import commands
from discord import app_commands
from tokens import discordToken

from cli_tools import cowsayCLI, figletCLI, pmatrixCLI

intents = discord.Intents.all()

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()
client.setup_hook()

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

@client.tree.command(name="pmatrix", description="Display matrix rain effect")
@app_commands.describe(width="Width of display", height="Height of display", frames="The number of frames to display")
async def matrix(interaction: discord.Interaction, width: int, height: int, frames: int):
    try:
        matrix_frames = pmatrixCLI(width, height, frames)
        await interaction.response.send_message(matrix_frames[0])
        for i in range(1, frames):
            await interaction.edit_original_response(content=matrix_frames[i])
            time.sleep(0.2)
    except:
        pass
        
client.run(discordToken)
