import discord
from discord.ext import commands

class Msg:

	def __init__(self, bot):
		self.bot = bot

	async def on_message(self, message):
		channel = self.bot.get_channel("403928190982160384")
		if message.channel == channel and message.author.bot == False:
			words = message.content.split()
			if len(words)+1 < 15:
				await self.bot.delete_message(message)


def setup(bot):
	bot.add_cog(Msg(bot))
