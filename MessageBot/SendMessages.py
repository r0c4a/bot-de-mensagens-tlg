from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import sys
import csv
import random
import time

 #Subscribe to my Youtube Channel: Solved4You
api_id = 13188969   #Enter Your 7 Digit Telegram API ID.
api_hash = 'b2093a7efa79c620a936476db5257c8f'   #Enter Yor 32 Character API Hash.
phone = '5511957265225'   #Enter Your Mobilr Number With Country Code.
client = TelegramClient(phone, api_id, api_hash)

SLEEP_TIME_2 = 300
SLEEP_TIME_1 = 60   
SLEEP_TIME = 60
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

users = []
with open(r"Scrapped.csv", encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

mode = int(input("Enter 1 to send by user ID or 2 to send by username: "))

#Enter you message here!
messages= ["Boa tarde {}, tudo bem? A nossa equipe viu que você faz parte do grupo ScarBlaze Exclusive, e selecionamos pessoas de lá a dedo para ganhar um brinde que é valido somente para hoje 20/09! Você tem interesse nesse bônus?  Preciso que responda o quanto antes, pois só temos 4 brindes restantes, e nesse exato momento, estou conversando com 7 pessoas ao mesmo tempo. Aguardo seu retorno."]
for user in users:
    if mode == 2:
        if user['username'] == "":
            continue
        receiver = client.get_input_entity(user['username'])
    elif mode == 1:
        receiver = InputPeerUser(user['id'],user['access_hash'])
    else:
        print("Invalid Mode. Exiting.")
        client.disconnect()
        sys.exit()
    message = random.choice(messages)
    try:
        print("Sending Message to:", user['name'])
        client.send_message(receiver, message.format(user['name']))
        print("Waiting {} seconds".format(SLEEP_TIME))
        time.sleep(SLEEP_TIME)
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        print("Waiting {} seconds".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except Exception as e:
        print("Error:", e)
        print("Trying to continue...")
        print("Waiting {} seconds".format(SLEEP_TIME_1))
        time.sleep(SLEEP_TIME_1)
client.disconnect()
print("Done. Message sent to all users.")
