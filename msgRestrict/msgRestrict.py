import discord
from discord.ext import commands

class Msg:

	def __init__(self, bot):
		self.bot = bot

	async def on_message(self, message):
		hiddenChannel = self.bot.get_channel("298875467916640256")
		if message.channel == hiddenChannel and message.author.bot == False:
			words = message.content.split()
			if len(words)+1 < 15:
				await self.bot.delete_message(message)


def setup(bot):
	bot.add_cog(Msg(bot))
