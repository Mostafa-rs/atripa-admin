from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Reward(models.Model):
    class Type:
        NORMAL = 0
        PERCENT = 1

    name = models.CharField(max_length=45, null=True)
    type = models.IntegerField(default=Type.NORMAL, validators=[MinValueValidator(0), MaxValueValidator(1)])
    amount = models.IntegerField(default=0)
    max_amount = models.PositiveIntegerField(default=0)
    required_point = models.IntegerField(default=0)
    desc_title = models.TextField(null=True)
    desc = models.TextField(null=True)
    date_validate = models.DateTimeField(null=True)
    usage_validate_per_user = models.IntegerField(default=1)
    usage_validate_total = models.IntegerField(default=0)
    date_created = models.DateTimeField(null=True, auto_now_add=True)
    hash_prefix = models.CharField(max_length=6, null=True)
    avatar = models.TextField(null=True)
    icon = models.CharField(max_length=100, null=True)
    category = models.ForeignKey('club.RewardCategory', models.CASCADE, 'cr_category', to_field='id', null=True)
    creator = models.ForeignKey('accounts.User', models.CASCADE, 'cr_creator', to_field='id', null=True)

    def __str__(self):
        return self.name

    @property
    def get_type(self):
        match self.type:
            case 1:
                return 'تخفیف نقدی'
            case 2:
                return 'تخفیف درصدی'
            case _:
                return 'نامشخص'


class RewardCategory(models.Model):
    name = models.CharField(max_length=45, null=True)
    icon = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class RewardUsage(models.Model):
    reward = models.ForeignKey('club.Reward', models.CASCADE, 'cru_reward', to_field='id', null=True)
    all = models.BooleanField(default=False)
    all_transport = models.BooleanField(default=False)
    accommodation_all = models.BooleanField(default=False)
    tour_all = models.BooleanField(default=False)
    airplane = models.BooleanField(default=False)
    train = models.BooleanField(default=False)
    bus = models.BooleanField(default=False)
    hotel = models.BooleanField(default=False)
    other_accommodation = models.BooleanField(default=False)
    tour = models.BooleanField(default=False)
    subscribe_low_all = models.BooleanField(default=False)
    subscribe_low_one_month = models.BooleanField(default=False)
    subscribe_low_three_month = models.BooleanField(default=False)
    subscribe_low_six_month = models.BooleanField(default=False)
    subscribe_low_one_year = models.BooleanField(default=False)
    subscribe_med_all = models.BooleanField(default=False)
    subscribe_med_one_month = models.BooleanField(default=False)
    subscribe_med_three_month = models.BooleanField(default=False)
    subscribe_med_six_month = models.BooleanField(default=False)
    subscribe_med_one_year = models.BooleanField(default=False)
    subscribe_high_all = models.BooleanField(default=False)
    subscribe_high_one_month = models.BooleanField(default=False)
    subscribe_high_three_month = models.BooleanField(default=False)
    subscribe_high_six_month = models.BooleanField(default=False)
    subscribe_high_one_year = models.BooleanField(default=False)

    def __str__(self):
        return self.reward.name


class RewardUsageGuide(models.Model):
    reward = models.ForeignKey('club.Reward', models.CASCADE, 'crug_reward', to_field='id', null=True)
    guide = models.TextField(null=True)

    def __str__(self):
        return self.reward.name


class RewardRule(models.Model):
    reward = models.ForeignKey('club.Reward', models.CASCADE, 'crr_reward', to_field='id', null=True)
    rule = models.TextField(null=True)

    def __str__(self):
        return self.reward.name


class TopFiveUsers(models.Model):
    user_one = models.CharField(max_length=45, null=True)
    user_two = models.CharField(max_length=45, null=True)
    user_three = models.CharField(max_length=45, null=True)
    user_four = models.CharField(max_length=45, null=True)
    user_five = models.CharField(max_length=45, null=True)
    user_point_one = models.IntegerField(default=0)
    user_point_two = models.IntegerField(default=0)
    user_point_three = models.IntegerField(default=0)
    user_point_four = models.IntegerField(default=0)
    user_point_five = models.IntegerField(default=0)
    date = models.DateField(null=True)


