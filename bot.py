from flask import Flask, request
import telebot

# Hardcoded bot token and webhook URL
BOT_TOKEN = "7570391319:AAHUxB8Cp9mdAFxCcBBy81vYYX8FdFT9lc8"
WEBHOOK_URL = "https://aviator-bot.onrender.com/webhook"

# Initialize Flask app
app = Flask(__name__)

# Initialize Telebot
bot = telebot.TeleBot(BOT_TOKEN)

@app.route('/')
def home():
    return "Aviator Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    json_update = request.get_json()
    bot.process_new_updates([telebot.types.Update.de_json(json_update)])
    return "", 200

# Set Webhook Route
@app.route('/set_webhook')
def set_webhook():
    webhook_set = bot.set_webhook(WEBHOOK_URL)
    return "Webhook set successfully!" if webhook_set else "Failed to set webhook."

# Ensure Gunicorn compatibility
if __name__ != "__main__":
    gunicorn_app = app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
