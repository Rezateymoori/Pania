import os
from telegram.ext import Updater, MessageHandler, Filters

# توکن رو از Railway می‌گیریم
TOKEN = os.getenv("BOT_TOKEN")

def reply_keywords(update, context):
    text = update.message.text.lower()
    if "سلام" in text:
        update.message.reply_text("سلام! خوش اومدی 🌸")
    elif "خداحافظ" in text:
        update.message.reply_text("به امید دیدار 👋")
    elif "عشق" in text:
        update.message.reply_text("عشق یعنی زندگی 💖")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_keywords))

updater.start_polling()
updater.idle()