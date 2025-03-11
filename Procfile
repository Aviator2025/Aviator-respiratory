web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker bot:app --log-level=info
worker: python bot.py
scheduler: python scheduler.py
