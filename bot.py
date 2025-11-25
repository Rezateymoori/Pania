import os
from telegram.ext import Updater, MessageHandler, Filters

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("BOT_TOKEN")

# دیکشنری پاسخ‌ها: کلمه → جواب
RESPONSES = {
    "سلام": "سلام! خوش اومدی 🌸",
    "خدا حافظ": "به امید دیدار 👋",
    "عشق": "عشق یعنی زندگی 💖",
    "صبح بخیر": "صبح‌تون پر از نور و انرژی ☀️",
    "شب بخیر": "شب‌تون آروم و رویایی 🌙",
    "خسته نباشی": "خسته نباشی پهلوان 💪",
    "مرسی": "خواهش می‌کنم عزیز دل 💫",
    "چطوری؟": "خوبم! تو چطوری؟ 😊",
"چطوری": "خوبم! تو چطوری؟ 😊",
    "بای": "فعلاً 👋",
}

# تابع پاسخ‌گویی به پیام‌ها
def reply_keywords(update, context):
    text = update.message.text.lower()
    for keyword, reply in RESPONSES.items():
        if keyword in text:
            update.message.reply_text(reply)
            break  # فقط یک جواب بده

# راه‌اندازی ربات
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # هندلر برای پیام‌های متنی
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_keywords))

    # شروع ربات
    updater.start_polling()
    updater.idle()

# اجرای تابع اصلی
if __name__ == "__main__":
    main()