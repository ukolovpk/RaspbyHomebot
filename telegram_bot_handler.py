import requests
import conf


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
            return result[len(result) - 1]
        else:
            return result[0]

    def send_message(self, chat_id, message):
        resp = SESSION.post(self.base_url + "/sendMessage", data={
            "chat_id": chat_id,
            "text": message
        })
        print("Код ответа: " + str(resp.status_code) + "\n")
        return resp
