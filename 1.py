from telegram.ext import Application
import asyncio

TOKEN = "your token"
GROUP_ID = -100  # آیدی عددی گروه (با منفی شروع میشه)

async def save_admins_on_startup(app: Application):
    bot = app.bot
    try:
        admins = await bot.get_chat_administrators(GROUP_ID)
        with open("admins.txt", "w", encoding="utf-8") as f:
            for admin in admins:
                user = admin.user
                name = f"{user.first_name or ''} {user.last_name or ''}".strip()
                username = f"@{user.username}" if user.username else ""
                f.write(f"{name} {username} ({user.id})\n")
        print("✅ لیست ادمین‌ها ذخیره شد.")
    except Exception as e:
        print("❌ خطا:", e)

async def main():
    app = Application.builder().token(TOKEN).build()
    await save_admins_on_startup(app)  # اجرای تابع در شروع
    await app.initialize()
    await app.start()
    await app.updater.start_polling()


asyncio.run(main())