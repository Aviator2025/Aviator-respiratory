from fastapi import FastAPI, Request
import telebot
import uvicorn

# Telegram Bot Token
BOT_TOKEN = "7570391319:AAHUxB8Cp9mdAFxCcBBy81vYYX8FdFT9lc8"

# Initialize the Telegram bot
bot = telebot.TeleBot(BOT_TOKEN)

# Initialize FastAPI app
app = FastAPI()

# Webhook URL
WEBHOOK_URL = "https://aviator-bot.onrender.com/webhook"

# Set webhook when the application starts
@app.on_event("startup")
async def on_startup():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

# Webhook route for receiving Telegram updates
@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates([update])
    return {"status": "ok"}

# Command: /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Aviator Predictor Bot! Use /predict to get predictions.")

# Command: /predict
@bot.message_handler(commands=['predict'])
def send_prediction(message):
    prediction = "Next multiplier: 2.5x (Example Prediction)"
    bot.reply_to(message, prediction)

# Run FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
