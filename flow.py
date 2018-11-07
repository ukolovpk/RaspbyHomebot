from telegram_bot_handler import TelegramBotHandler
import conf
from get_dht_values import DHTValues

bot = TelegramBotHandler()
dht = DHTValues()
values = dht.get_temperature_and_humidity()
updated_result = bot.get_update()
chat_id = updated_result["message"]["chat"]["id"]
bot.send_message(chat_id, str(values))