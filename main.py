import os
import time
import asyncio
from pyrogram import Client, filters
from KeepAlive import keep_alive

# Replace 'YOUR_API_ID', 'YOUR_API_HASH', and 'PHONE_NUMBER' with your own values
api_id = int(os.environ['ID'])
api_hash = os.environ['HASH']

keep_alive()

"""

we will start thw=e autorization using this code  :: uncomment for the first time
async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("", "Hi sister, this message is sent using python bot! ")

asyncio.run(main())

"""
# Create a new Pyrogram client
app = Client("my_account")
"""

## used to get message from a group, channel and user
# Start the Pyrogram client
with app:
    # Get the chat ID of the account or chat from which you want to retrieve messages
    chat_id = -1001793637099

    # Get the recent 10 messages from the chat
    messages = app.get_chat_history(chat_id, limit=1)

    # Iterate over the messages and print their text
    for i, message in enumerate(messages):
        print(message)
        if message.text != None:
            try:
                if  str(message.chat.type) == "ChatType.SUPERGROUP":
                    print(f"{i}, {message.from_user.first_name} ---- {message.text}")
                if str(message.sender_chat.type) == "ChatType.CHANNEL":
                    print(f"{i}, {message.text}")
                else:
                    #print(message)
                    print(f"{i}, {message.from_user.first_name} ---- {message.text}")
            except:
                pass

"""


chat_id = ""  # ID or name of channel, group or user from where we forward from
result = []
item = 0
with app:

    while item < 100000000:
              # Get the latest message from the group
        ids = []
        element = 10
        time.sleep(2)
        messages = list(app.get_chat_history(chat_id, limit=element))
        
        # Check if any messages are returned
        if len(messages) > 0:
            # Get the latest message
            element -= 1
            while element >= 0:
                latest_message = messages[element]
                #print(latest_message)
                # Forward the latest message to your account
                destination_chat_id = ""   # ID or name of channel, group or user to which we will forward to
                #app.forward_messages(destination_chat_id, chat_id, latest_message.id)
                ids.append(latest_message.id)
                element -= 1
        #print(ids)
        if item == 0:
            print("this is the first trial")
        else:
            for i, j in enumerate(ids):
                if j not in result :
                    try:
                        app.forward_messages(destination_chat_id, chat_id, j)  
                        print("there is a message sent...")
                    except Exception as e:
                        print(f"there was an error:: {e}")
        #print(result)
        result = ids
        #print(result)
        time.sleep(5)
        #print(ids)
        print(item)
        item += 1
