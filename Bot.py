import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".", help_command=None, intents=discord.Intents.all())


CENSORED_WORDS = ["сука", "пидор", "нахуй"]

@bot.event
async def on_ready():
	print(f"Bot {bot.user} is ready to work!")

@bot.event
async def on_member_join(member):
	role = discord.utils.get(member.guild.roles, id=1095330022266523709)
	channel = member.guild.system_channel

	embed = discord.Embed(
		title="Новый участник!",
		description=f"{member.name}#{member.discriminator}",
		color=0xffffff
	)

	await member.add_roles(role)
	await channel.send(embed=embed)


@bot.event
async def on_message(message):
	await bot.process_commands(message)

	for content in message.content.split():
		for censored_word in CENSORED_WORDS:
			if content.lower() == censored_word:
				await message.delete()
				await message.channel.send(f"{message.author.mention} такие слова запрещены!")


@bot.command()
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: discord.Member, *,reason="Нарушение правил."):
	await ctx.send(f"Администратор {ctx.author.mention} исключил пользователя {member.mention}", delete_after=3)
	await member.kick(reason=reason)
	await ctx.message.delete()

@bot.command(name="бан", aliases=["баня", "банана", "банчик"])
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, user: discord.Member, *,reason="Нарушение правил."):
	await ctx.send(f"Администратор {ctx.author.mention} забанил пользователя {member.mention}", delete_after=3)
	await member.ban(reason=reason)
	await ctx.message.delete()

bot.run("MTI3MjE0NzE2NzE3OTU3MTI5NQ.GSvcEh.c4J6d3S2MDVCpweezlurcPierU3Kp0JwQ0wvqo")