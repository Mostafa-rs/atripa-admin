from django.db.models.signals import post_save
from .models import Reward, RewardUsage
from django.dispatch import receiver


@receiver(post_save, sender=Reward)
def reward_post_save(sender, **kwargs):
    reward = kwargs['instance']
    if kwargs['created']:
        RewardUsage.objects.create(reward=reward)
