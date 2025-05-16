import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

BOT_TOKEN = os.getenv("BOT_TOKEN")

facts = [
    "Факт: Мозг потребляет 20% всей энергии тела.",
    "Факт: Солнце в 109 раз больше Земли.",
    "Факт: Вода — единственное вещество на Земле, встречающееся в природе в трёх состояниях."
]

intro_text = "Здорово, братишка! Я твой сценемайнс-бот. Выбери, что хочешь:"
reply_keyboard = [["Интересный факт"], ["Реклама"], ["Контакты"]]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(intro_text, reply_markup=markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Интересный факт":
        await update.message.reply_text(random.choice(facts))
    elif text == "Реклама":
        await update.message.reply_text("Реклама: Хочешь попасть сюда? Пиши в инсту: @scenemindsreal")
    elif text == "Контакты":
        await update.message.reply_text("Контакты:
Telegram: @scenemindsreal
Instagram: scenemindsreal
Email: adilflow1n@gmail.com")
    else:
        await update.message.reply_text("Выбери кнопку или напиши /start")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
