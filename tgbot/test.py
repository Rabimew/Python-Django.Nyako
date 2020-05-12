from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

updater = Updater(token='816720263:AAHFSFCQjqIP9yXVUleESaYQRPCGSK04sFU', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="呱呱呱~!")

def echo(update, context):
    if update.message.text=='你好':
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'你好鸭{update.effective_chat.id},今天吃小猫了吗！')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text*2)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def eatcat(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text='小猫好吃！！！！！！！！！！！！！！')


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="嘤嘤嘤我看不懂这个啦")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

eatcat_handler = CommandHandler('eatcat', eatcat)
dispatcher.add_handler(eatcat_handler)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
