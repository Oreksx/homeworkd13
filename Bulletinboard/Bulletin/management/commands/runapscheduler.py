import logging
 
from django.conf import settings
 
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from Bulletin.models import Post, Category
from datetime import datetime, timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
 
 
logger = logging.getLogger(__name__)
 
 
def my_job():
    #  Your job processing logic here...
    date = datetime.now().date() - timedelta(seconds=7)
    post = Post.objects.all().filter(datepost__gt=date)
    users = User.objects.all()
    title = []
    urlposts = []
    users_email = []
    for i in post:
        title.append(i.title)
        urlposts.append(i.get_absolute_url())
        if not len(title) == 0:
            for t in users:
                users_email.append(t.email)
            html_content = render_to_string( 
            'appointment_created1.html',
            {
                'urlpost': urlposts,
            })
            msg = EmailMultiAlternatives(
                subject=f'Новые посты за неделю',
                body="Вы подписаны на посты",
                from_email="Robotoreksx@yandex.ru",
                to=users_email,
            )
            msg.attach_alternative(html_content, "text/html")

            msg.send()
 
 
# функция которая будет удалять неактуальные задачи
def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)
 
 
class Command(BaseCommand):
    help = "Runs apscheduler."
 
    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        
        # добавляем работу нашему задачнику
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second=10),  # Тоже самое что и интервал, но задача тригера таким образом более понятна django
            id="my_job",  # уникальный айди
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")
 
        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
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