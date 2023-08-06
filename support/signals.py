from django.db.models.signals import post_save
from .models import Support, Chat
from django.dispatch import receiver


@receiver(post_save, sender=Support)
def support_post_save(sender, **kwargs):
    support = kwargs['instance']
    if kwargs['created']:
        Chat.objects.create(message=support.message, support=support, sender=support.creator)
