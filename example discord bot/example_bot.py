import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run("NzYxMzY4Nzc4ODUyMTM5MDA4.X3Zl7g._bDTiHy_U5sNFykYTfbazNX2jNE")