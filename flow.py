from telegram_bot_handler import RaspbyBot
import conf
from get_dht_values import DHTValues
import random


bot = RaspbyBot()
dht = DHTValues()
updated_result = bot.get_update()
user_id = updated_result["message"]["from"]["id"]
chat_id = updated_result["message"]["chat"]["id"]

if user_id in conf.dictionary["authorized users"]:
    text = bot.get_message(updated_result, dht)
    bot.send_message(chat_id, text)
else:
    bot.send_message(chat_id, "ты даже НЕ ГРАЖДАНИН!")


