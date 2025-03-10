import os
import telebot
from flask import Flask, request

TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()
    if update:
        bot.process_new_updates([telebot.types.Update.de_json(update)])
    return "OK", 200

@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    success = bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")
    return f"Webhook set: {success}"

@app.route("/remove_webhook", methods=["GET"])
def remove_webhook():
    bot.delete_webhook()
    return "Webhook removed"

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Webhook is working!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
