#!/bin/bash
echo "🚀 Starting Bot Deployment..."

# Create logs directory
mkdir -p logs

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Apply database migrations (if using one)
alembic upgrade head  # Only if using SQLAlchemy

# Run API server with Gunicorn (background)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker bot:app --log-level=info --access-logfile logs/access.log --error-logfile logs/error.log &

# Run Telegram bot in background
python bot.py >> logs/bot.log 2>&1 &

# Run scheduler for predictions
python scheduler.py >> logs/scheduler.log 2>&1 &

# Monitor logs
tail -f logs/bot.log logs/scheduler.log logs/access.log
