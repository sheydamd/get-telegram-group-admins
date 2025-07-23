from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "your token"

async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    await update.message.reply_text(f"آیدی عددی این چت:\n{chat.id}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, get_chat_id))
app.run_polling()