from django.db.models.signals import post_save
from .models import UserTransaction, User
from django.dispatch import receiver


@receiver(post_save, sender=UserTransaction)
def transaction_post_save(sender, **kwargs):
    transaction = kwargs['instance']
    if kwargs['created']:
        balance = transaction.user.income - transaction.user.spend
        if transaction.type in [0, 1, 2, 3, 4]:
            transaction.wallet_balance = balance + transaction.amount
        elif transaction.type in [10, 11, 12, 13, 14]:
            transaction.wallet_balance = balance - transaction.amount

        transaction.save()
