import discord
import jsonpickle

client = discord.Client()
conf = jsonpickle.decode(open("data/configuration.json").read())



client.run(conf.bot_token)