import os
import logging
from flask import Flask, request
import telebot

# Load environment variables
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Ensure required environment variables are set
if not TOKEN or not WEBHOOK_URL:
    raise ValueError("Error: TELEGRAM_BOT_TOKEN or WEBHOOK_URL is not set!")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Enable logging
logging.basicConfig(level=logging.INFO)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()
    if update is None:
        logging.warning("Received empty request")
        return "No data received", 400

    bot.process_new_updates([telebot.types.Update.de_json(update)])
    return "OK", 200

@app.route("/")
def home():
    return "Aviator Bot is running!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
