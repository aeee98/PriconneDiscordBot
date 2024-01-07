import discord
from discord import app_commands, Interaction
from discord.ext import commands

# Viral is a section of "fun" commands to add to KyrariBot. For obvious reasons there will be cooldowns on all of these commands. This is named after Viral, the unseiso mod.
class Viral(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="isvampycore", description = "IS VAMPY CORE?!")
    @app_commands.checks.cooldown(rate=1, per=120)
    async def is_vampy_core(self, interaction : Interaction) -> None:
        await interaction.response.send_message("Yes! https://isvampycore.com/images/vampygif.gif", ephemeral = False)

    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Viral(bot))