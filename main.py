import praw
import telegram
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

telegram_bot_token = '2133115792:AAH0oPMpddaOO1ixnwD4bli8lFq14GrBBZw'

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def getBlondes(update, context):
    file = open('credentials.json', 'r')
    data = json.load(file)

    reddit = praw.Reddit(
             client_id=data['client_id'],
            client_secret=data['client_secret'],
            user_agent=data['user_agent']
        )   

    subreddit = reddit.subreddit('OnlyFansBlonde')
    for submission in subreddit.top(limit=5):
        chat_id = update.effective_chat.id
        context.bot.send_photo(chat_id=671798413, photo=f'{submission.url}')


def getRedHeads(update, context):
    file = open('credentials.json', 'r')
    data = json.load(file)

    reddit = praw.Reddit(
             client_id=data['client_id'],
            client_secret=data['client_secret'],
            user_agent=data['user_agent']
        )   

    subreddit = reddit.subreddit('OnlyFansReds')
    for submission in subreddit.top(limit=5):
        chat_id = update.effective_chat.id
        context.bot.send_photo(chat_id=671798413, photo=f'{submission.url}')



def getBrunettes(update, context):
    file = open('credentials.json', 'r')
    data = json.load(file)

    reddit = praw.Reddit(
             client_id=data['client_id'],
            client_secret=data['client_secret'],
            user_agent=data['user_agent']
        )   

    subreddit = reddit.subreddit('OnlyFansBrunette')
    for submission in subreddit.top(limit=5):
        chat_id = update.effective_chat.id
        context.bot.send_photo(chat_id=671798413, photo=f'{submission.url}')


dispatcher.add_handler(CommandHandler("getblondes", getBlondes))
dispatcher.add_handler(CommandHandler("redheads", getRedHeads))
dispatcher.add_handler(CommandHandler("brunettes", getBrunettes))

updater.start_polling()
