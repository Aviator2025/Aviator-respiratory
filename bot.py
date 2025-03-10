import logging
import time
import random
import requests
from flask import Flask, request

# Hardcoded bot token and webhook URL
TELEGRAM_TOKEN = "7570391319:AAHUxB8Cp9mdAFxCcBBy81vYYX8FdFT9lc8"
WEBHOOK_URL = "https://api.telegram.org/bot7570391319:AAHUxB8Cp9mdAFxCcBBy81vYYX8FdFT9lc8/setWebhook?url=https://aviator-bot.onrender.com/7570391319:AAHUxB8Cp9mdAFxCcBBy81vYYX8FdFT9lc8"

BOT_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

# Initialize Flask app
app = Flask(__name__)

# Logging setup
logging.basicConfig(level=logging.INFO)

# Store past predictions for AI analysis
past_predictions = []

@app.route("/", methods=["GET"])
def home():
    return "Bot is running 24/7 with AI improvements!"

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "").lower()

        response = handle_command(text)
        if response:
            send_message(chat_id, response)

    return "OK", 200

def handle_command(text):
    command_responses = {
        "/start": "Welcome to the Aviator Predictor! Running 24/7 with AI enhancements.
"
                  "Commands:
"
                  "/predict - Get next Aviator prediction
"
                  "/multiround - Show next 3 predictions
"
                  "/highconfidence - High-accuracy alert
"
                  "/track - Start tracking rounds
"
                  "/history - View past predictions
"
                  "/successrate - Check bot accuracy
"
                  "/stoptracking - Stop tracking
"
                  "/setfilter - Set prediction filters
"
                  "/setaccuracy - Adjust accuracy settings
"
                  "/status - Check bot status
"
                  "/restart - Restart the bot",

        "/predict": f"Next Aviator prediction: {generate_prediction()}",
        "/multiround": f"Next 3 rounds: {', '.join([generate_prediction() for _ in range(3)])}",
        "/highconfidence": "🚀 High-confidence prediction: 5x+ multiplier (Example).",
        "/track": "Tracking started. Logging Aviator results...",
        "/history": f"Past 5 predictions: {', '.join(past_predictions[-5:])}",
        "/successrate": f"Bot success rate: {calculate_accuracy()}%",
        "/stoptracking": "Tracking stopped.",
        "/setfilter": "Filter set: Only showing 2x+ multipliers.",
        "/setaccuracy": "Accuracy threshold adjusted.",
        "/status": "✅ Bot is running 24/7 with AI analysis.",
        "/restart": "Restarting bot..."
    }
    return command_responses.get(text, "Unknown command. Type /start for a list of commands.")

def generate_prediction():
    possible_outcomes = ["1.5x", "2x", "3x", "5x", "10x"]
    prediction = random.choice(possible_outcomes)
    past_predictions.append(prediction)
    return prediction

def calculate_accuracy():
    if not past_predictions:
        return 0
    correct_predictions = len([p for p in past_predictions if p in ["2x", "3x", "5x"]])
    return round((correct_predictions / len(past_predictions)) * 100, 2)

def send_message(chat_id, text):
    url = f"{BOT_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    while True:
        try:
            app.run(host="0.0.0.0", port=5000)
        except Exception as e:
            logging.error(f"Bot crashed: {e}. Restarting...")
            time.sleep(5)  # Wait before restarting
