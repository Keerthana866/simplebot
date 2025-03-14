from hydrogram import client,filters 

ammu =clinet(
  "examplebot",
  api_id=25194212,
  api_hash="cd594d9d6754b78658c2ed0b7fd5b54d",
  bot_token="7543444215:AAHxyr0zcKV8NqPPbtrJjzwTnfn1ErHgUpw"
)

#commed creation 
@ammu.on_message(filters.commend("start") && filters.group )
async def start(client,message):
    await message.replay_text("hey i am alive ")

ammu.run()
