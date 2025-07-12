import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")  # Render e environment variable theke token nibe

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("হ্যালো! আমি একটি টেলিগ্রাম বট। আপনি কিছু লিখুন।")

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_received = update.message.text
    await update.message.reply_text(f"আপনার বার্তা পেয়েছি: {text_received}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

    print("বট চালু হয়েছে...")
    app.run_polling()
