"""
    Location Database Models
    Author: Mostafa Rasouli
    Email: mostafarasooli54@gmail.com
    2023/08/28
"""

from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100, null=True)
    english_name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey('location.Category', models.RESTRICT, 'll_type', null=True, to_field='id')
    country = models.ForeignKey('basic.Country', models.RESTRICT, 'll_country', null=True, to_field='id')
    province = models.ForeignKey('basic.Province', models.RESTRICT, 'll_province', null=True, to_field='id')
    city = models.ForeignKey('basic.City', models.RESTRICT, 'll_city', null=True, to_field='id')
    address = models.TextField(null=True)
    location = models.CharField(max_length=50, default='0.0,0.0')
    energy = models.CharField(max_length=30, default='0')
    avg_mins = models.CharField(max_length=30, default='0')
    total_popularity = models.CharField(max_length=3, default='0')
    creator = models.ForeignKey('accounts.User', models.CASCADE, 'll_creator', to_field='id', null=True)
    date_created = models.DateTimeField(null=True)
    last_modified = models.DateTimeField(null=True)
    visit = models.PositiveIntegerField(default=0)
    tags = models.TextField(null=True)
    text = models.TextField(null=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    family_suitable = models.BooleanField(default=True)
    child_suitable = models.BooleanField(default=True)
    man_only = models.BooleanField(default=False)
    woman_only = models.BooleanField(default=False)
    extra_time = models.CharField(max_length=30, default='0')
    extra_energy = models.CharField(max_length=30, default='0')
    # Open Hours
    first_saturday = models.CharField(max_length=30, null=True)
    first_sunday = models.CharField(max_length=30, null=True)
    first_monday = models.CharField(max_length=30, null=True)
    first_tuesday = models.CharField(max_length=30, null=True)
    first_wednesday = models.CharField(max_length=30, null=True)
    first_thursday = models.CharField(max_length=30, null=True)
    first_friday = models.CharField(max_length=30, null=True)
    first_holiday = models.CharField(max_length=30, null=True)
    second_saturday = models.CharField(max_length=30, null=True)
    second_sunday = models.CharField(max_length=30, null=True)
    second_monday = models.CharField(max_length=30, null=True)
    second_tuesday = models.CharField(max_length=30, null=True)
    second_wednesday = models.CharField(max_length=30, null=True)
    second_thursday = models.CharField(max_length=30, null=True)
    second_friday = models.CharField(max_length=30, null=True)
    second_holiday = models.CharField(max_length=30, null=True)
    third_saturday = models.CharField(max_length=30, null=True)
    third_sunday = models.CharField(max_length=30, null=True)
    third_monday = models.CharField(max_length=30, null=True)
    third_tuesday = models.CharField(max_length=30, null=True)
    third_wednesday = models.CharField(max_length=30, null=True)
    third_thursday = models.CharField(max_length=30, null=True)
    third_friday = models.CharField(max_length=30, null=True)
    third_holiday = models.CharField(max_length=30, null=True)
    forth_saturday = models.CharField(max_length=30, null=True)
    forth_sunday = models.CharField(max_length=30, null=True)
    forth_monday = models.CharField(max_length=30, null=True)
    forth_tuesday = models.CharField(max_length=30, null=True)
    forth_wednesday = models.CharField(max_length=30, null=True)
    forth_thursday = models.CharField(max_length=30, null=True)
    forth_friday = models.CharField(max_length=30, null=True)
    forth_holiday = models.CharField(max_length=30, null=True)
    fifth_saturday = models.CharField(max_length=30, null=True)
    fifth_sunday = models.CharField(max_length=30, null=True)
    fifth_monday = models.CharField(max_length=30, null=True)
    fifth_tuesday = models.CharField(max_length=30, null=True)
    fifth_wednesday = models.CharField(max_length=30, null=True)
    fifth_thursday = models.CharField(max_length=30, null=True)
    fifth_friday = models.CharField(max_length=30, null=True)
    fifth_holiday = models.CharField(max_length=30, null=True)
    sixth_saturday = models.CharField(max_length=30, null=True)
    sixth_sunday = models.CharField(max_length=30, null=True)
    sixth_monday = models.CharField(max_length=30, null=True)
    sixth_tuesday = models.CharField(max_length=30, null=True)
    sixth_wednesday = models.CharField(max_length=30, null=True)
    sixth_thursday = models.CharField(max_length=30, null=True)
    sixth_friday = models.CharField(max_length=30, null=True)
    sixth_holiday = models.CharField(max_length=30, null=True)
    seventh_saturday = models.CharField(max_length=30, null=True)
    seventh_sunday = models.CharField(max_length=30, null=True)
    seventh_monday = models.CharField(max_length=30, null=True)
    seventh_tuesday = models.CharField(max_length=30, null=True)
    seventh_wednesday = models.CharField(max_length=30, null=True)
    seventh_thursday = models.CharField(max_length=30, null=True)
    seventh_friday = models.CharField(max_length=30, null=True)
    seventh_holiday = models.CharField(max_length=30, null=True)
    eighth_saturday = models.CharField(max_length=30, null=True)
    eighth_sunday = models.CharField(max_length=30, null=True)
    eighth_monday = models.CharField(max_length=30, null=True)
    eighth_tuesday = models.CharField(max_length=30, null=True)
    eighth_wednesday = models.CharField(max_length=30, null=True)
    eighth_thursday = models.CharField(max_length=30, null=True)
    eighth_friday = models.CharField(max_length=30, null=True)
    eighth_holiday = models.CharField(max_length=30, null=True)
    ninth_saturday = models.CharField(max_length=30, null=True)
    ninth_sunday = models.CharField(max_length=30, null=True)
    ninth_monday = models.CharField(max_length=30, null=True)
    ninth_tuesday = models.CharField(max_length=30, null=True)
    ninth_wednesday = models.CharField(max_length=30, null=True)
    ninth_thursday = models.CharField(max_length=30, null=True)
    ninth_friday = models.CharField(max_length=30, null=True)
    ninth_holiday = models.CharField(max_length=30, null=True)
    tenth_saturday = models.CharField(max_length=30, null=True)
    tenth_sunday = models.CharField(max_length=30, null=True)
    tenth_monday = models.CharField(max_length=30, null=True)
    tenth_tuesday = models.CharField(max_length=30, null=True)
    tenth_wednesday = models.CharField(max_length=30, null=True)
    tenth_thursday = models.CharField(max_length=30, null=True)
    tenth_friday = models.CharField(max_length=30, null=True)
    tenth_holiday = models.CharField(max_length=30, null=True)
    eleventh_saturday = models.CharField(max_length=30, null=True)
    eleventh_sunday = models.CharField(max_length=30, null=True)
    eleventh_monday = models.CharField(max_length=30, null=True)
    eleventh_tuesday = models.CharField(max_length=30, null=True)
    eleventh_wednesday = models.CharField(max_length=30, null=True)
    eleventh_thursday = models.CharField(max_length=30, null=True)
    eleventh_friday = models.CharField(max_length=30, null=True)
    eleventh_holiday = models.CharField(max_length=30, null=True)
    twelfth_saturday = models.CharField(max_length=30, null=True)
    twelfth_sunday = models.CharField(max_length=30, null=True)
    twelfth_monday = models.CharField(max_length=30, null=True)
    twelfth_tuesday = models.CharField(max_length=30, null=True)
    twelfth_wednesday = models.CharField(max_length=30, null=True)
    twelfth_thursday = models.CharField(max_length=30, null=True)
    twelfth_friday = models.CharField(max_length=30, null=True)
    twelfth_holiday = models.CharField(max_length=30, null=True)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True)
    persian_name = models.CharField(max_length=60, null=True)
    description = models.TextField(null=True)


class Image(models.Model):
    location = models.ForeignKey('location.Location', models.CASCADE, 'li_location', to_field='id', null=True)
    image = models.TextField(null=True)
    alt = models.TextField(null=True)
    caption = models.TextField(null=True)


class Comment(models.Model):
    date = models.DateTimeField(null=True)
    location = models.ForeignKey('location.Location', models.CASCADE, 'lc_location', to_field='id', null=True)
    user = models.ForeignKey('accounts.User', models.CASCADE, 'lc_user', to_field='id', null=True)
    father = models.ForeignKey('location.Comment', models.CASCADE, 'lc_comments', to_field='id', null=True)
    text = models.TextField(null=True)
    deleted = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)


class Interaction(models.Model):
    location = models.ForeignKey('location.Location', models.CASCADE, 'lin_location', to_field='id', null=True)
    user = models.ForeignKey('accounts.User', models.CASCADE, 'lin_user', to_field='id', null=True)
    favorite = models.BooleanField(default=False)
    liked = models.BooleanField(default=False)
    rating = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('location', 'user')


class SubCategory(models.Model):
    class Meta:
        db_table = "location_sub_category"

    category = models.ForeignKey("location.Category", models.CASCADE, "lpt_category", to_field="id", null=True)
    name = models.CharField(max_length=30, null=True)
    energy = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    persian_name = models.CharField(max_length=30, null=True)


class PointsType(models.Model):
    class Meta:
        db_table = "location_points_type"

    sub_category = models.ForeignKey("location.SubCategory", models.CASCADE, "lpt_sub_category", to_field="id",
                                     null=True)
    key = models.CharField(max_length=30, null=True)
    value = models.CharField(max_length=30, null=True)
    point = models.IntegerField(default=0)
    extra_energy = models.IntegerField(default=0)
    extra_time = models.IntegerField(default=0)
    question = models.TextField(null=True)
    multi_question = models.TextField(null=True)


class Points(models.Model):
    class Meta:
        db_table = "location_points"

    location = models.ForeignKey("location.Location", models.CASCADE, "lp_location", to_field="id", null=True)
    category = models.ForeignKey("location.Category", models.CASCADE, "lp_category", to_field="id", null=True)
    point = models.IntegerField(default=0)


class PointAnswers(models.Model):
    class Meta:
        db_table = "location_point_answers"

    location = models.ForeignKey("location.Location", models.CASCADE, "lpa_location", to_field="id", null=True)
    sub_category = models.ForeignKey("location.SubCategory", models.CASCADE, "lpa_sub_category", to_field="id",
                                     null=True)
    key = models.CharField(max_length=100, null=True)
    value = models.CharField(max_length=100, null=True)
