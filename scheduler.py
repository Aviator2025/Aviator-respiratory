from apscheduler.schedulers.background import BackgroundScheduler
import time

def predict_aviator():
    print("🔮 Running prediction algorithm...")
    # Add your prediction logic here

scheduler = BackgroundScheduler()
scheduler.add_job(predict_aviator, 'interval', minutes=1)  # Runs every minute
scheduler.start()

while True:
    time.sleep(60)  # Keep script running
