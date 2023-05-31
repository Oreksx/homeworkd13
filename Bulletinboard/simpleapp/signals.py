from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import send_mail
from simpleapp.models import Replies, AcceptReply
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
 
 
# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(post_save, sender=Replies)
def notify_addreply(sender, instance, created, **kwargs):
    if created:
        replyfrom = instance.replyfrom
        replyto = instance.replyto.author

        send_mail("New Reply on your Post", f'Hi, Your Post in website World of Game give reply from {replyfrom}', "Robotoreksx@yandex.ru", {replyto.email})



































































