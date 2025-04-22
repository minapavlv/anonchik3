import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = '7893409112:AAFXaQh3JAOkRLHmETmS1eatCORigMQRCrE'
YOUR_CHAT_ID = 6624984494

logging.basicConfig(level=logging.INFO)

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message and update.message.text:
            await context.bot.send_message(
                chat_id=YOUR_CHAT_ID,
                text=update.message.text
            )
    except Exception as e:
        print(f"Ошибка: {e}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_message))
app.run_polling()
