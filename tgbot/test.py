import logging
from time import sleep
import telegram
from telegram.error import NetworkError, Unauthorized
## 下方填入自己的TOKEN
bot = telegram.Bot('816720263:AAHFSFCQjqIP9yXVUleESaYQRPCGSK04sFU')
update_id = None
def main():
    global update_id
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1
def echo (bot):
    global update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        if update.message:
            update.message.reply_text(update.message.text)

if __name__ == '__main__':
    main()