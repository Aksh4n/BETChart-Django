import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler 
from apscheduler.schedulers.background import BackgroundScheduler 

from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand 
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from transactions.models import  CurrentPrice , CandleColor 


logger = logging.getLogger(__name__)


def candle_color():

  from datetime import datetime
  import time

  p1 = float(CurrentPrice.objects.get(id=1).price)
  time.sleep(177)
  p2 = float(CurrentPrice.objects.get(id=1).price) 

  if p2 > p1 :

    CandleColor.objects.create(color=1).save()
  elif p2 < p1 :

    CandleColor.objects.create(color=2).save()

  else:

    pass    


    


def my_job():



    # Import libraries
  import json
  import requests


    # defining key/request url
  key = "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT"

    # requesting data from url
  data = requests.get(key)
  apidata = data.json()
  price = (apidata["data"]["price"])

  CurrentPrice.objects.update(price=price)
  # Your job processing logic here...




# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way. 
@util.close_old_connections
def delete_old_job_executions(max_age=3600):
  """
  This job deletes APScheduler job execution entries older than `max_age` from the database.
  It helps to prevent the database from filling up with old historical records that are no
  longer useful.
  
  :param max_age: The maximum length of time to retain historical job execution records.
                  Defaults to 7 days.
  """
  DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
  help = "Runs APScheduler."

  def handle(self, *args, **options):
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
      my_job,
      trigger=CronTrigger(second="*/3"),  # Every 10 seconds
      id="my_job",  # The `id` assigned to each job MUST be unique
      max_instances=1,
      replace_existing=True,
    )
    logger.info("Added job 'my_job'.")

    scheduler.add_job(
      candle_color,
      trigger=CronTrigger(minute="*/3"),  # Every 10 seconds
      id="candle_color",  # The `id` assigned to each job MUST be unique
      max_instances=1,
      replace_existing=True,
    )
    logger.info("Added job 'candle_color'.")



    scheduler.add_job(
      delete_old_job_executions,
      trigger=CronTrigger(
        day_of_week="mon", hour="00", minute="00"
      ),  # Midnight on Monday, before start of the next work week.
      id="delete_old_job_executions",
      max_instances=1,
      replace_existing=True,
    )
    logger.info(
      "Added weekly job: 'delete_old_job_executions'."
    )

    try:
      logger.info("Starting scheduler...")
      scheduler.start()
    except KeyboardInterrupt:
      logger.info("Stopping scheduler...")
      scheduler.shutdown()
      logger.info("Scheduler shut down successfully!")



