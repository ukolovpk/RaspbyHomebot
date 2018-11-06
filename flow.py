from telegram_bot_handler import TelegramBotHandler
import conf
from get_dht_values import DHTValues

bot = TelegramBotHandler()
dht = DHTValues()
updated_results = bot.get_update()