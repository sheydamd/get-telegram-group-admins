from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ContextTypes
from datetime import datetime

TOKEN = "7534100403:AAFEQefPJjEGGSddzmxO8z3YdDDxAcK7vXA"

# تابع برای ذخیره اطلاعات ادمین‌ها در فایل
async def write_admins_to_file(chat_title: str, chat_id: int, admins) -> None:
    with open("admins.txt", "w", encoding="utf-8") as f:
        f.write(f"\n {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f" Group Title: {chat_title}\n")
        f.write(f" Group ID: {chat_id}\n")
        f.write(" Admins:\n")
        for admin in admins:
            user = admin.user
            name = f"{user.first_name or ''} {user.last_name or ''}".strip()
            username = f"@{user.username}" if user.username else ""
            user_id = user.id
            f.write(f" - {name} {username} (ID: {user_id})\n")
        f.write("-" * 40 + "\n")

# دستور /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"سلام {user.mention_html()} عزیز\n"
        "من یه ربات مدیریتی هستم، می‌تونی از دستور /help برای دیدن امکاناتم استفاده کنی!"
    )

# دستور /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        " دستورات قابل استفاده:\n"
        "/start - شروع به کار ربات\n"
        "/help - راهنما\n"
        "ارسال پیام 'ممنون' - پاسخ مودبانه \n"
        "ارسال هر پیامی در گروه - ذخیره لیست ادمین‌ها"
    )

# ذخیره لیست ادمین‌ها (فقط داخل گروه)
async def save_admins(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat = update.effective_chat
    if chat.type in ["group", "supergroup"]:
        admins = await context.bot.get_chat_administrators(chat.id)
        await write_admins_to_file(chat.title, chat.id, admins)
        await update.message.reply_text(" لیست ادمین‌ها ذخیره شد.")
    else:
        await update.message.reply_text(" این دستور فقط در گروه‌ها فعال است.")

#  پاسخ به پیام‌های خاص (مثلاً "ممنون")
async def respond_to_thanks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text.lower() in ["ممنون", "مرسی", "سپاس"]:
        await update.message.reply_text("قربونت برم عزیز دلم ")

# اجرای برنامه
def main():
    app = Application.builder().token(TOKEN).build()
    # دستورات
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # پاسخ به ممنون
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond_to_thanks))

    # ذخیره ادمین‌ها (در هر پیام ارسالی در گروه)
    app.add_handler(MessageHandler(filters.ALL, save_admins))

    app.run_polling()

if __name__ == "__main__":
    main()