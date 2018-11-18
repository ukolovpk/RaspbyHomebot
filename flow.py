from telegram_bot_handler import RaspbyBot
from get_dht_values import DHTValues
import conf
from time import sleep


bot = RaspbyBot()
dht = DHTValues()
updated_result = bot.get_update()
global last_update_id
last_update_id = updated_result[len(updated_result) - 1]["update_id"]


def auth_and_send(message_info):

    user_id = message_info["message"]["from"]["id"]
    chat_id = message_info["message"]["chat"]["id"]
    update_id = message_info["update_id"]

    if user_id in conf.dictionary["authorized users"]:
        text = bot.get_message(message_info, dht)
        bot.send_message(chat_id, text)
    else:
        bot.send_message(chat_id, "ты даже НЕ ГРАЖДАНИН!")

    global last_update_id
    last_update_id = update_id
    sleep(2)


if __name__ == "__main__":
    while True:
        updated_result = bot.get_update(offset=last_update_id + 1)
        if updated_result:
            for i in updated_result:
                auth_and_send(i)
        sleep(30)
