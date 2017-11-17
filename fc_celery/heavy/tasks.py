import time

from config import celery_app


@celery_app.task(bind=True)
def long_task(self):
    time.sleep(5)
    print('long_task')
