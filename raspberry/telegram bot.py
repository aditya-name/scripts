import sys


sys.setdefaultencoding('utf8')

import random
import datetime
import time
import RPi.GPIO as GPIO  # GPIO funktioniert nicht, wenn du in dir eine Datei mit dem Namen RPi.py hast. # RPi.GPIO kann nur auf RPi installiert werden nicht auf einem PC.
import requests
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

GPIO.output(22, True)


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

        # url = "https://api.telegram.org/bot<token>/" #

    def get_updates(self, offset=0, timeout=30):
        method = "getUpdates"
        params = {"timeout": timeout, "offset": offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()["result"]
        return result_json

    def send_message(self, chat_id, text):
        params = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
        method = "sendMessage"
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = "740101585:AAEcw_0IDwmFa3QMwZnpxlPzbZBzCDN2AjM"
magnito_bot = BotHandler(token)


def main():
    new_offset = 0
    print("...im Gange...")

    try:
        while True:
            all_updates = magnito_bot.get_updates(new_offset)

            if len(all_updates) > 0:
                for current_update in all_updates:
                    # print(current_update)
                    first_update_id = current_update["update_id"]
                    if "text" not in current_update["message"]:
                        first_chat_text = "New member"
                    else:
                        first_chat_text = current_update["message"]["text"]
                    first_chat_id = current_update["message"]["chat"]["id"]
                    if "first_name" in current_update["message"]:
                        first_chat_name = current_update["message"]["chat"]["first_name"]
                    elif "new_chat_member" in current_update["message"]:
                        first_chat_name = current_update["message"]["new_chat_member"]["username"]
                    elif "from" in current_update["message"]:
                        first_chat_name = current_update["message"]["from"]["first_name"]
                    else:
                        first_chat_name = "unknown"
                    a = 0
                    b = 1
                    if first_chat_text == "start" and first_chat_name == "Telegram Konto":
                        magnito_bot.send_message(first_chat_id, "angefangen")
                        while True:
                            all_updates = magnito_bot.get_updates(new_offset)
                            if a == b:
                                break

                            if len(all_updates) > 0:
                                for current_update in all_updates:

                                    # print(current_update)
                                    first_update_id = current_update["update_id"]
                                    if "text" not in current_update["message"]:
                                        first_chat_text = "New member"
                                    else:
                                        first_chat_text = current_update["message"]["text"]
                                    first_chat_id = current_update["message"]["chat"]["id"]
                                    if "first_name" in current_update["message"]:
                                        first_chat_name = current_update["message"]["chat"]["first_name"]
                                    elif "new_chat_member" in current_update["message"]:
                                        first_chat_name = current_update["message"]["new_chat_member"]["username"]
                                    elif "from" in current_update["message"]:
                                        first_chat_name = current_update["message"]["from"]["first_name"]
                                    else:
                                        first_chat_name = "unknown"

                                    if first_chat_text == "stop" and first_chat_name == "Telegram Konto":
                                        magnito_bot.send_message(first_chat_id, "angehalten")  # + first_chat_name)
                                        new_offset = first_update_id + 1
                                        a = 1
                                    log = datetime.datetime.now()
                                    print(first_chat_name + " " + str(log) + first_chat_text)
                                    delay = random.randint(0, 11)
                                    magnito_bot.send_message(first_chat_id, "OK " + first_chat_name + ', ich leite es weiter (' + first_chat_text + ") [Verzoegerung:" + str(delay) + "]")
                                    GPIO.output(22, False)
                                    time.sleep(delay)
                                    GPIO.output(22, True)
                                    new_offset = first_update_id + 1
                                    os.system("./speech.sh %s" % first_chat_text)
    except SyntaxError:
        print("testing")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
