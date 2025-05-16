import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.environ.get("PORT", "10000"))
WEBHOOK_URL = f"https://sceneminds.onrender.com/{BOT_TOKEN}"

facts = [
    "Факт: Мозг потребляет 20% всей энергии тела.",
    "Факт: Солнце в 109 раз больше Земли.",
    "Факт: Вода — единственное вещество на Земле, встречающееся в природе в трёх состояниях.",
]

intro_text = "Здорово, братишка! Я твой Sceneminds Helper. Выбери, что хочешь:"
reply_keyboard = [["Интересный факт"], ["Реклама"], ["Контакты"]]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(intro_text, reply_markup=markup)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Интересный факт":
        await update.message.reply_text(random.choice(facts))
    elif text == "Реклама":
        await update.message.reply_text(
            "Реклама: Хочешь попасть сюда? Пиши в инсту: @scenemindsreal"
        )
    elif text == "Контакты":
        await update.message.reply_text(
            "Контакты:\nTelegram: @scenemindsreal\nInstagram: scenemindsreal\nEmail: adilflow1n@gmail.com"
        )
    else:
        await update.message.reply_text("Выбери кнопку или напиши /start")


async def greet_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"Здорово, {member.full_name}! Добро пожаловать в нашу группу!"
        )


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, greet_new_member))

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL,
    )
