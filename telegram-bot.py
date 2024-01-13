from telethon.sync import TelegramClient, events
from telethon.client import messages

keys = open("keys.txt")
keysContent = keys.read().split("\n")
api_id = keysContent[0]
api_hash = keysContent[1]

deletedShorts = 0

with TelegramClient('name', api_id, api_hash) as client:
   @client.on(events.NewMessage(pattern='^(.*?(youtube.com/shorts)[^$]*)$'))
   async def handler(event: events.NewMessage):
      global deletedShorts

      if deletedShorts < 4:
         await event.reply('!!! YOUTUBE SHORT DETECTED !!! DELETING MESSAGE !!!')
      else:
         await event.reply("Why do you even bother. You realize this is automated right?")

      await client.delete_messages( event.chat_id, [ event.id ] )
      deletedShorts += 1

   client.run_until_disconnected()
