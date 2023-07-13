from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    english_name = models.CharField(max_length=45, null=True)
    continental = models.CharField(max_length=15, null=True)
    prefix_number = models.CharField(max_length=5, null=True)
    iata = models.CharField(max_length=45, null=True)
    description = models.TextField(null=True)
    grs_id = models.IntegerField(null=True)
    nationality = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.name} - {self.english_name}'

    class Meta:
        verbose_name_plural = 'Countries'


class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)
    english_name = models.CharField(max_length=45, null=True)
    country = models.ForeignKey(Country, models.RESTRICT, 'bp_country', null=True, to_field='id')
    description = models.TextField(null=True)
    grs_id = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name} - {self.english_name}'


class City(models.Model):
    name = models.CharField(max_length=45, null=True)
    english_name = models.CharField(max_length=45, null=True)
    iata = models.CharField(max_length=10, null=True)
    province = models.ForeignKey(Province, models.RESTRICT, 'bci_province', null=True, to_field='id')
    country = models.ForeignKey(Country, models.RESTRICT, 'bci_country', null=True, to_field='id')
    latitude = models.DecimalField(decimal_places=6, max_digits=8, default=0.0)
    longitude = models.DecimalField(decimal_places=6, max_digits=8, default=0.0)
    description = models.TextField(null=True)
    is_province_capital = models.BooleanField(default=False)
    is_country_capital = models.BooleanField(default=False)
    grs_id = models.IntegerField(default=0)
    has_plan = models.BooleanField(default=False)
    usage_flight = models.IntegerField(default=0)
    usage_accommodation = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.english_name}'

    class Meta:
        verbose_name_plural = 'Cities'


class Terminal(models.Model):
    class Type:
        AIR_PORT = 0
        TRAIN_STATION = 1
        BUS_STATION = 2
        TAXI_STATION = 3
        SHIP_STATION = 4

    name = models.CharField(max_length=100, null=True)
    english_name = models.CharField(max_length=100, null=True)
    type = models.IntegerField(default=Type.AIR_PORT, validators=[MinValueValidator(0), MaxValueValidator(5)])
    country = models.ForeignKey(Country, models.RESTRICT, 'bt_country', null=True, to_field='id')
    province = models.ForeignKey(Province, models.RESTRICT, 'bt_province', null=True, to_field='id')
    city = models.ForeignKey(City, models.RESTRICT, 'bt_city', null=True, to_field='id')
    popularity = models.FloatField(default=0)
    iata = models.CharField(max_length=45, null=True)
    is_international = models.BooleanField(default=False)
    latitude = models.DecimalField(decimal_places=6, max_digits=8, default=0.0)
    longitude = models.DecimalField(decimal_places=6, max_digits=8, default=0.0)
    address = models.TextField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.name} - {self.english_name}'

    @property
    def get_type(self):
        # match self.type:
        #     case 0:
        #         return 'فرودگاه'
        #     case 1:
        #         return 'پایانه قطار'
        #     case 2:
        #         return 'پایانه اتوبوس'
        #     case 3:
        #         return 'پایانه تاکسی'
        #     case 4:
        #         return 'پابانه کشتی'
        if self.type == 0:
            return 'فرودگاه'
        elif self.type == 1:
            return 'پایانه قطار'
        elif self.type == 2:
            return 'پایانه اتوبوس'
        elif self.type == 3:
            return 'پایانه تاکسی'
        elif self.type == 4:
            return 'پایانه کشتی'


class Vehicle(models.Model):
    class Type:
        BUS = 1
        TRAIN = 2
        FLIGHT = 3

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    type = models.IntegerField(default=Type.FLIGHT, validators=[MinValueValidator(1), MaxValueValidator(3)])
    capacity = models.IntegerField(default=1)
    manufacturer = models.CharField(max_length=100, null=True)

    @property
    def get_type(self):
        match self.type:
            case 1:
                return 'اتوبوس'
            case 2:
                return 'قطار'
            case 3:
                return 'هواپیما'
            case _:
                return 'نامشخص'
        # if self.type == 1:
        #     return 'اتوبوس'
        # elif self.type == 2:
        #     return 'قطار'
        # elif self.type == 3:
        #     return 'هواپیما'


class Accommodation(models.Model):
    name = models.CharField(max_length=45, null=True)
    location = models.CharField(max_length=45, null=True)
    type = models.CharField(max_length=100, null=True)
    country = models.ForeignKey(Country, models.RESTRICT, 'ba_country', null=True, to_field='id')
    province = models.ForeignKey(Province, models.RESTRICT, 'ba_province', null=True, to_field='id')
    city = models.ForeignKey(City, models.RESTRICT, 'ba_city', null=True, to_field='id')
    address = models.TextField(null=True)
    phone_number = models.CharField(max_length=15, null=True)
    website = models.TextField(null=True)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    star = models.IntegerField(default=0, null=True)
    star_rating = models.FloatField(default=0, null=True)
    reservable = models.BooleanField(default=True)
    is_foreign = models.BooleanField(default=False)
    latitude = models.FloatField(default=0, null=True)
    longitude = models.FloatField(default=0, null=True)
    description = models.TextField(null=True)
    grs_id = models.IntegerField(default=0, null=True)
    features = models.ManyToManyField('AccommodationFeature', 'ba_features')

    @property
    def get_type(self):
        match self.type:
            case 'apartment_hotel':
                return 'هتل آپارتمان'

            case 'beach_residential_complex':
                return 'مجتمع مسکونی ساحلی'

            case 'boutique':
                return 'بوتیک'

            case 'ecotourism_resorts':
                return 'اقامتگاه بوم گردی'

            case 'hostel':
                return 'خوابگاه'

            case 'hotel':
                return 'هتل'

            case 'inn':
                return 'مهمانپذیر'

            case 'motel':
                return 'متل'

            case 'residential_complex':
                return 'مجتمع مسکونی'

            case 'residential_unit':
                return 'واحد مسکونی'

            case 'traditional_residence':
                return 'اقامتگاه مسکونی'

            case 'traveler_house':
                return 'خانه مسافر'

            case _:
                return 'نامشخص'

    @property
    def avatar(self):
        if image := AccommodationImage.objects.filter(accommodation=self).first():
            return image.image
        else:
            return None

    @property
    def rooms(self):
        return AccommodationRoom.objects.filter(accommodation=self)

    @property
    def room_count(self):
        return AccommodationRoom.objects.filter(accommodation=self).count()


class AccommodationFeature(models.Model):
    name = models.CharField(max_length=45, null=True)
    icon = models.CharField(max_length=45, null=True)
    category = models.ForeignKey('AccommodationFeatureCategory', models.CASCADE, 'baf_category', null=True)

    def __str__(self):
        return self.name


class AccommodationImage(models.Model):
    accommodation = models.ForeignKey(Accommodation, models.CASCADE, 'bai_accommodation', null=True)
    image = models.TextField(null=True)
    alt = models.TextField(null=True)
    caption = models.TextField(null=True)
    grs_name = models.TextField(null=True)


class AccommodationPOI(models.Model):
    accommodation = models.ForeignKey(Accommodation, models.CASCADE, 'bapoi_accommodation', to_field='id',
                                      null=True)
    poi = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(default=0)
    walk_time = models.IntegerField(default=0)
    drive_time = models.IntegerField(default=0)


class AccommodationFeatureCategory(models.Model):
    name = models.CharField(max_length=45, null=True)

    class Meta:
        verbose_name_plural = 'Accommodation feature categories'


class AccommodationRoom(models.Model):
    accommodation = models.ForeignKey(Accommodation, models.CASCADE, 'bar_accommodation', null=True)
    grs_id = models.IntegerField(default=0, null=True)
    name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    capacity = models.IntegerField(default=1, null=True)
    extra_capacity = models.IntegerField(default=1, null=True)
    single_bed_count = models.IntegerField(default=1, null=True)
    double_bed_count = models.IntegerField(default=1, null=True)
    sofa_bed_count = models.IntegerField(default=1, null=True)
    out_of_service = models.BooleanField(default=False)
    accept_child = models.BooleanField(default=True)
    description = models.TextField(null=True)
    deleted_at = models.DateTimeField(null=True)
    features = models.ManyToManyField(AccommodationFeature, 'bar_features')


class AccommodationRuleCategory(models.Model):
    name = models.CharField(max_length=100, null=True)
    english_name = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = 'Accommodation rule categories'


class AccommodationRule(models.Model):
    name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(AccommodationRuleCategory, models.CASCADE, 'baru_category', null=True)
    accommodation = models.ForeignKey(Accommodation, models.CASCADE, 'baru_accommodation', null=True)
    description = models.TextField(null=True)


class AccommodationRuleCondition(models.Model):
    rule = models.ForeignKey(AccommodationRule, models.CASCADE, 'barc_rule', null=True)
    name = models.CharField(max_length=100, null=True)
    english_name = models.CharField(max_length=100, null=True)
    value = models.CharField(max_length=100, null=True)


class AccommodationService(models.Model):
    name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    price = models.IntegerField(default=0, null=True)
    accommodation = models.ForeignKey(Accommodation, models.CASCADE, 'bas_accommodation', null=True)
    description = models.TextField(null=True)


class AccommodationServiceCondition(models.Model):
    service = models.ForeignKey(AccommodationService, models.CASCADE, 'basc_service', null=True)
    name = models.CharField(max_length=100, null=True)
    english_name = models.CharField(max_length=100, null=True)
    value = models.CharField(max_length=100, null=True)


class SiteOption(models.Model):
    option_name = models.TextField(null=True)
    option_value = models.TextField(null=True)
    option_title = models.TextField(null=True)
    option_desc = models.TextField(null=True)

    class Options:
        USER_CLUB_DASHBOARD_BANNER = "user_club_dashboard_banner"


class Bank(models.Model):
    name = models.CharField(max_length=45, null=True)
    logo = models.TextField(null=True)
    color_first = models.CharField(max_length=7, null=True)
    color_last = models.CharField(max_length=7, null=True)
    color_code = models.CharField(max_length=200, null=True, blank=True)


class SupportType(models.Model):
    name = models.CharField(max_length=45, unique=True)
    icon = models.CharField(max_length=45, null=True)
    father = models.ForeignKey('self', models.CASCADE, "bst_father", to_field="id", null=True, blank=True)


class Subscribe(models.Model):
    name = models.CharField(max_length=45, null=True, unique=True)
    english_name = models.CharField(max_length=45, null=True, unique=True)
    price = models.PositiveIntegerField(default=0)
    discount_three_month = models.FloatField(default=0)
    discount_six_month = models.FloatField(default=0)
    discount_one_year = models.FloatField(default=0)
    color_code = models.CharField(max_length=7)


class SubscribeOptions(models.Model):
    subscribe = models.ForeignKey(Subscribe, models.CASCADE, 'bso_subscribe', to_field="id", null=True)
    name = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'Subscribe options'


class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.TextField()
    ceo = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    mail = models.EmailField()
    website = models.TextField()
    address = models.TextField()
    agency_number = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Companies'







