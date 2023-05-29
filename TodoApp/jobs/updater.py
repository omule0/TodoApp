from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import send_reminder, mark_skipped_tasks,delete_old_tasks, delete_old_weekly_tasks

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_reminder, 'interval', seconds=1)
    scheduler.add_job(mark_skipped_tasks, 'interval', seconds=1)
    scheduler.add_job(delete_old_tasks, 'interval', seconds=5)
    scheduler.add_job(delete_old_weekly_tasks, 'interval', seconds=5)
    scheduler.start()