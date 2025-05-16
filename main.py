import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я минимальный бот без фоновых задач.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Команды:\n/start - начать\n/help - помощь")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"Добро пожаловать, {member.full_name}!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("welcome", welcome))

    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", "8443")),
        webhook_url=f"https://YOUR_RENDER_DOMAIN.onrender.com/{BOT_TOKEN}"
    )
