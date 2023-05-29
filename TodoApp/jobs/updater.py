from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import send_reminder

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_reminder, 'interval', seconds=1)
    scheduler.start()