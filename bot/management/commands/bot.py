from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler, InlineQueryHandler
from telegram.utils.request import Request
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .commands import start
from .messages import handler


@csrf_exempt
def webhook(request):
    bot = Bot(
        token=settings.TOKEN,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, handler))

    data = json.loads(request.body.decode("utf-8"))
    update = Update.de_json(data, bot)
    updater.dispatcher.process_update(update)

    return HttpResponse("ok")

def set_webhook(request):
    bot = Bot(
        token=settings.TOKEN,
    )
    print(bot.get_me())
    print(bot.get_webhook_info())

    updater = Updater(
        bot=bot,
        use_context=True,
    )

    updater.bot.set_webhook(settings.BASE_URL + "/webhook/" + settings.TOKEN)
    return HttpResponse(settings.BASE_URL + "/webhook/" + settings.TOKEN)

def delete_webhook(request):
    bot = Bot(
        token=settings.TOKEN,
    )
    print(bot.get_me())

    updater = Updater(
        bot=bot,
        use_context=True,
    )

    updater.bot.delete_webhook()
    return HttpResponse("ok")

class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )

        bot = Bot(
            token=settings.TOKEN,
        )
        print(bot.get_me())

        updater = Updater(
            bot=bot,
            use_context=True,
        )

        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, handler))

        updater.start_polling()
        updater.idle()

