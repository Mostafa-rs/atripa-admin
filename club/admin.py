from django.contrib import admin
from .models import *

admin.site.register(Reward)
admin.site.register(RewardRule)
admin.site.register(RewardUsage)
admin.site.register(RewardCategory)
admin.site.register(RewardUsageGuide)
admin.site.register(TopFiveUsers)