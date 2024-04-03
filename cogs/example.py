import discord
from discord.ext import commands
from utilities.context import Context

class example(commands.Cog):
    """Example Cog"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx: Context):
        embed = discord.Embed(
            title = "bot template help",
            color = 0x2F3136
        )
        embed.add_field(
            name = "Commands",
            value = "```help, ping, roles```"
        )

        return await ctx.reply(embed = embed, mention_author = False)

    @commands.command(
        name = "ping",
        description = "pong"
    )
    async def ping(self, ctx: Context):
        return await ctx.success(f"Latency: {round(self.bot.latency * 1000)}ms")
    
    @commands.command(
        name = "roles",
        description = "Show a list of the server's roles"
    )
    async def roles(self, ctx: Context):
        if not ctx.guild.roles:
            return await ctx.error("There aren't any roles in this server")
        
        embed = discord.Embed(
            title = f"Roles in {ctx.guild.name}",
            color = 0x2F3136
        )
        embed.description = list()

        for role in reversed(ctx.guild.roles[1:]):
            embed.description.append(f"{role.mention} - {len(role.members):,} members")
        
        return await ctx.paginate(embed)

async def setup(bot):
    await bot.add_cog(example(bot))