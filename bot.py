from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# Telegram Bot Token
TOKEN = "7570391319:AAHUxB8Cp9mdAFxCcBBy81vYYX8FdFT9lc8"

# Define start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot.")

# Initialize Telegram bot with webhook
def run_telegram_bot():
    bot_app = ApplicationBuilder().token(TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    
    # Set webhook
    webhook_url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://aviator-bot.onrender.com/{TOKEN}"
    response = requests.get(webhook_url)
    print("Webhook response:", response.json())

    bot_app.run_webhook(
        listen="0.0.0.0",
        port=5000,
        webhook_url=f"https://aviator-bot.onrender.com/{TOKEN}"
    )

# Run Telegram bot in a separate thread
if __name__ == "__main__":
    from threading import Thread
    bot_thread = Thread(target=run_telegram_bot)
    bot_thread.start()
    
    app.run(host="0.0.0.0", port=5000)
