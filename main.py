from hydrogram import Client, filters 

ammu = Client(
    "examplebot",
    api_id=25194212,
    api_hash="cd594d9d6754b78658c2ed0b7fd5b54d",
    bot_token="7543444215:AAHxyr0zcKV8NqPPbtrJjzwTnfn1ErHgUpw"
)

#commed creation 
@ammu.on_message(filters.command("start") & filters.group )
async def start(client,message):
    await message.reply_text("hey i am alive ")

ammu.run()
