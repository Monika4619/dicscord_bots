import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        #if message.author.id == self.user.id:
        #   return

        if message.content.startswith('hello'):
            await message.reply('Hello!', mention_author=True)

client = MyClient()
client.run('OTMyNjg3MTczNDE5OTU0MjI2.YeWmng.A83I-NQMT7evqi6D5vkx6-He9Vs')