from django.db import models


class TrackableBaseModel(models.Model):
    create_user = models.ForeignKey('account.User', models.RESTRICT, 'create_user_%(class)ss', null=True)
    modify_user = models.ForeignKey('account.User', models.RESTRICT, 'modify_user_%(class)ss', null=True)
    delete_user = models.ForeignKey('account.User', models.RESTRICT, 'delete_user_%(class)ss', null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    modify_date = models.DateTimeField(auto_now=True, null=True)
    delete_date = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
