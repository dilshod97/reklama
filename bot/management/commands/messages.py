from .commands import start
from django.conf import settings
from telegram import ParseMode, Bot
from ...models import Category
bot = Bot(
        token=settings.TOKEN,
    )


def html(update):
    res = update.message.reply_text(text='reply_text')


def handler(update, self):
    chat_id = update.message.chat_id
    text = update.message.text
    category = Category.objects.first()
    print(bot.get_chat_member(1167945861, chat_id))
    print(category)

    if text == str(category.name):
        if bot.get_chat_member(1167945861, chat_id):
            html(update)

