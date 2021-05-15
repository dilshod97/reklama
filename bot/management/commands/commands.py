from .keyboards import darslar
import json
from ...models import Category


def start(update, user):
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    category = Category.objects.all()
    reply_markup = darslar(category)
    reply_text = 'lanasdasd'

    res = update.message.reply_text(text=reply_text, reply_markup=reply_markup)
