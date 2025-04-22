
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = '7893409112:AAFXaQh3JAOkRLHmETmS1eatCORigMQRCrE'


YOUR_TELEGRAM_ID = 6302057190

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text
        await context.bot.send_message(chat_id=YOUR_TELEGRAM_ID, text=f"Новое анонимное сообщение:\n\n{text}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
app.run_polling()
