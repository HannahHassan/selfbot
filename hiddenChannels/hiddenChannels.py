import discord
from discord.ext import commands

class Template:

	def __init__(self, bot):
		self.bot = bot

	#A cog to list all hidden channels on a Server

	#A command to sort them all. Usage: [p]channels.text/topic
	@commands.group(pass_context=True)
	async def channels(self, ctx):
		pass

	#Adds all the Text Channels of the Server the message was sent in to an embed message and sends it
	@channels.command(pass_context=True)
	async def text(self, ctx, hidden=False):
		guild = ctx.message.guild
		channelNames = []
		channel = ctx.message.channel
		channels = guild.text_channels
		hiddenChannel = self.bot.get_channel(298875467916640256)
		e = discord.Embed(title="Guild Channels")
		e.set_thumbnail(url=guild.icon_url)
		for guildChannel in channels:
			e.add_field(name="TextChannel", value=guildChannel.name)
		if hidden:
			await ctx.message.delete()
			await hiddenChannel.send(embed=e)
		else:
			await channel.send(embed=e)

	#Does the same as the text function but with Channel Topics
	@channels.command(pass_context=True)
	async def topic(self, ctx, hidden=False):
		guild = ctx.message.guild
		channel = ctx.message.channel
		channels = guild.text_channels
		hiddenChannel = self.bot.get_channel(298875467916640256)
		e = discord.Embed(title="Guild Topics")
		e.set_thumbnail(url=guild.icon_url)
		for guildChannel in channels:
			if guildChannel.topic is None or guildChannel.topic is "":
					continue
			else:
					e.add_field(name=guildChannel, value=guildChannel.topic)
		if hidden:
			await ctx.message.delete()
			await hiddenChannel.send(embed=e)
		else:
			await channel.send(embed=e)

def setup(bot):
	bot.add_cog(Template(bot))