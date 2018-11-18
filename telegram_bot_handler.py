import requests
import conf
import random


SESSION = requests.session()


class TelegramBotHandler(object):

    def __init__(self):
        self.token = conf.dictionary["token"]
        self.base_url = "https://api.telegram.org/bot{token}".format(token=self.token)

    def get_update(self, timeout=30, offset=None):
        resp = SESSION.get(self.base_url + "/getUpdates", data={'timeout': timeout, 'offset': offset})
        print("Код ответа: " + str(resp.status_code) + "\n")
        result = resp.json()["result"]
        if len(result) > 0:
            return result
        else:
            return None

    def send_message(self, chat_id, message):
        resp = SESSION.post(self.base_url + "/sendMessage", data={
            "chat_id": chat_id,
            "text": message
        })
        print("Код ответа: " + str(resp.status_code) + "\n")
        return resp


class RaspbyBot(TelegramBotHandler):

    def __init__(self):
        super(RaspbyBot, self).__init__()

    def get_message(self, updated, dht):
        try:
            text = updated['message']['text']
        except:
            text = None
        if text == conf.GET_TEMPERATURE:
            resp = "Сейчас в твоей квартире " + str(dht.get_temperature_and_humidity()["temperature"]) + " градусов по Цельсию"
        elif text == conf.GET_HUMIDITY:
            resp = "Сейчас в твоей квартире влажность воздуха составляет " + str(dht.get_temperature_and_humidity()["humidity"]) + " г/м³"
        elif text == conf.GET_ALL:
            resp = "Сейчас в твоей квартире " + str(dht.get_temperature_and_humidity()["temperature"]) + " градусов по Цельсию и " + str(dht.get_temperature_and_humidity()["humidity"]) + " г/м³ - влажности"
        else:
            resp = random.choice(["Босс, я не знаю такой команды",
                                  "Повтори, что надо сделать?",
                                  "Чё надо, хозяин?",
                                  "К сожалению, я не понимаю...",
                                  "Попробуй ещё раз"])
        return resp
