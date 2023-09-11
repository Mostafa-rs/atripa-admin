from . import models as acc_models
from django.db import models
import random


def identify_generator():
    last_identify = acc_models.UserSupportRequest.objects.aggregate(max_id=models.Max('identify_no'))
    if not last_identify.get('max_id') or last_identify.get('max_id') <= 0:
        return 100000000
    return last_identify.get('max_id') + 1
