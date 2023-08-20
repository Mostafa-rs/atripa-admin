"""
    Account Database Models
    Author: Mostafa Rasouli
    Email: mostafarasooli54@gmail.com
    2023/08/14
"""

from django.db import models


class AgeGroup:
    ADULT = 0
    CHILD = 1
    INFANT = 2
    ANY = 3


class Order(models.Model):
    class Status:
        BOOK = 1
        SEARCH_RESULT = 2
        REVALIDATE = 3
        PRE_RESERVE = 4
        TICKETED = 5
        PAYMENT_GATEWAY = 6
        PAYMENT_FAIL = 7
        PAYMENT_SUCCESS = 8
        TICKET_IN_PROCESS = 9
        SEARCH = 10
        TICKETED_CHANGED = 11
        CANCELLED = 12
        EXPIRED = 13
        CONFIRMED = 14
        WAIT_LIST = 15
        RESERVE_IN_PROCESS = 16

    class Currency:
        IRR = 1
        USD = 2
        EUR = 3

    class Type:
        ITINERARY = 1
        TOUR = 2
        EVENT = 3
        SUBSCRIBE = 4

        AIRPLANE = 11
        TRAIN = 12
        BUS = 13
        MINIBUS = 14
        TAXI = 15
        PRIVATE_CAR = 16

        HOTEL = 21
        ACCOMMODATION = 22

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('accounts.User', models.CASCADE, 'rro_user', null=True)
    currency = models.IntegerField(default=Currency.IRR)
    status = models.IntegerField(default=Status.SEARCH)
    rating = models.IntegerField(null=True)
    comment = models.TextField(null=True)
    type = models.IntegerField(default=Type.ITINERARY)
    create_date = models.DateTimeField(null=True)
    expire_date = models.DateTimeField(null=True)
    cancel_date = models.DateTimeField(null=True)
    booked_date = models.DateTimeField(null=True)
    defined_date = models.DateTimeField(null=True)

    @property
    def get_currency(self):
        match self.currency:
            case Order.Currency.IRR:
                return {'id': Order.Currency.IRR, 'currency': 'ریال'}
            case Order.Currency.USD:
                return {'id': Order.Currency.USD, 'currency': '$'}
            case Order.Currency.EUR:
                return {'id': Order.Currency.EUR, 'currency': ''}
            case _:
                return {'id': '', 'currency': ''}

    @property
    def get_type(self):
        match self.type:
            case Order.Type.ITINERARY:
                return {'id': Order.Type.ITINERARY, 'type': 'برنامه سفر'}
            case Order.Type.TOUR:
                return {'id': Order.Type.TOUR, 'type': 'تور'}
            case Order.Type.EVENT:
                return {'id': Order.Type.EVENT, 'type': 'رویداد'}
            case Order.Type.SUBSCRIBE:
                return {'id': Order.Type.SUBSCRIBE, 'type': 'اشتراک'}
            case Order.Type.AIRPLANE:
                return {'id': Order.Type.AIRPLANE, 'type': 'پرواز'}
            case Order.Type.TRAIN:
                return {'id': Order.Type.TRAIN, 'type': 'قطار'}
            case Order.Type.BUS:
                return {'id': Order.Type.BUS, 'type': 'اتوبوس'}
            case Order.Type.MINIBUS:
                return {'id': Order.Type.MINIBUS, 'type': 'مینی بوس'}
            case Order.Type.TAXI:
                return {'id': Order.Type.TAXI, 'type': 'تاکسی'}
            case Order.Type.PRIVATE_CAR:
                return {'id': Order.Type.PRIVATE_CAR, 'type': 'ماشین شخصی'}
            case Order.Type.HOTEL:
                return {'id': Order.Type.HOTEL, 'type': 'هتل'}
            case Order.Type.ACCOMMODATION:
                return {'id': Order.Type.ACCOMMODATION, 'type': 'اقامتگاه'}
            case _:
                return {'id': '', 'type': ''}

    def get_status(self):
        match self.status:
            case Order.Status.BOOK:
                return {'id': Order.Status.BOOK, 'status': 'رزرو شده'}
            case Order.Status.SEARCH_RESULT:
                return {'id': Order.Status.SEARCH_RESULT, 'status': 'نتیجه جستجو'}
            case Order.Status.REVALIDATE:
                return {'id': Order.Status.REVALIDATE, 'status': 'تجدید اعتبار'}
            case Order.Status.PRE_RESERVE:
                return {'id': Order.Status.PRE_RESERVE, 'status': 'پیش رزرو'}
            case Order.Status.TICKETED:
                return {'id': Order.Status.TICKETED, 'status': 'بلیت صادر شده'}
            case Order.Status.PAYMENT_GATEWAY:
                return {'id': Order.Status.PAYMENT_GATEWAY, 'status': 'درگاه پرداخت'}
            case Order.Status.PAYMENT_FAIL:
                return {'id': Order.Status.PAYMENT_FAIL, 'status': 'پرداخت لغو شده'}
            case Order.Status.PAYMENT_SUCCESS:
                return {'id': Order.Status.PAYMENT_SUCCESS, 'status': 'پرداخت شده'}
            case Order.Status.TICKET_IN_PROCESS:
                return {
                    'id': Order.Status.TICKET_IN_PROCESS,
                    'status': 'بلیت در حال صدور',
                }
            case Order.Status.SEARCH:
                return {'id': Order.Status.SEARCH, 'status': 'جستجو'}
            case Order.Status.TICKETED_CHANGED:
                return {
                    'id': Order.Status.TICKETED_CHANGED,
                    'status': 'بلیت تغییر داده شده',
                }
            case Order.Status.CANCELLED:
                return {'id': Order.Status.CANCELLED, 'status': 'لغو شده'}
            case Order.Status.EXPIRED:
                return {'id': Order.Status.EXPIRED, 'status': 'منقضی شده'}
            case Order.Status.CONFIRMED:
                return {'id': Order.Status.CONFIRMED, 'status': 'تایید شده'}
            case Order.Status.WAIT_LIST:
                return {'id': Order.Status.WAIT_LIST, 'status': 'در لیست انتظار'}
            case Order.Status.RESERVE_IN_PROCESS:
                return {'id': Order.Status.RESERVE_IN_PROCESS, 'status': 'در حال رزرو'}
            case _:
                return {'id': '', 'status': ''}


class OrderAccommodation(models.Model):
    class Meta:
        db_table = 'reserve_order_accommodation'

    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey('reserve.Order', models.RESTRICT, 'roa_order', null=True)
    accommodation = models.ForeignKey('basic.Accommodation', models.CASCADE, 'roa_accommodation', null=True)
    check_in = models.DateField(null=True)
    check_out = models.DateField(null=True)
    confirmation_code = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    # GRS Data
    grs_state = models.CharField(max_length=45, null=True)
    grs_status = models.CharField(max_length=45, null=True)
    grs_confirmation_code = models.CharField(max_length=100, null=True)
    grs_property_confirmation_code = models.CharField(max_length=100, null=True)
    grs_discount = models.IntegerField(null=True)
    grs_total_price = models.IntegerField(null=True)
    grs_total_sales_price = models.IntegerField(null=True)
    grs_total_daily_price = models.IntegerField(null=True)
    grs_total_cancellation_fee = models.IntegerField(null=True)
    grs_total_modification_fee = models.IntegerField(null=True)
    grs_disagreement = models.BooleanField(null=True)
    grs_troubled = models.BooleanField(null=True)
    grs_booked_date = models.DateField(null=True)


class OrderAccommodationRule(models.Model):
    class Meta:
        db_table = 'reserve_order_accommodation_rule'

    order = models.ForeignKey('reserve.Order', models.RESTRICT, 'roaru_order', null=True)
    accommodation = models.ForeignKey('reserve.OrderAccommodation', models.CASCADE, 'roaru_accommodation', null=True)
    grs_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    conditions = models.TextField(null=True)


class OrderAccommodationRoom(models.Model):
    class Meta:
        db_table = 'reserve_order_accommodation_room'

    order = models.ForeignKey('reserve.Order', models.RESTRICT, 'roar_order', null=True)
    accommodation = models.ForeignKey('reserve.OrderAccommodation', models.CASCADE, 'roar_accommodation', null=True)
    adult_count = models.IntegerField(null=True)
    childrens = models.TextField(null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    nationality = models.ForeignKey('basic.Country', models.CASCADE, 'roar_nationality', null=True)
    national_code = models.CharField(max_length=100, null=True)
    passport_number = models.CharField(max_length=100, null=True)
    grs_roome_type_id = models.IntegerField(null=True)
    grs_rate_plan_id = models.IntegerField(null=True)
    grs_reserve_room_code = models.TextField(null=True)
    grs_total_cancellation_fee = models.IntegerField(null=True)
    grs_total_modification_fee = models.IntegerField(null=True)
    grs_total_price = models.IntegerField(null=True)
    grs_total_daily_price = models.IntegerField(null=True)
    grs_total_sales_price = models.IntegerField(null=True)


class OrderAccommodationRoomPrice(models.Model):
    class Meta:
        db_table = 'reserve_order_accommodation_room_price'

    order = models.ForeignKey('reserve.Order', models.RESTRICT, 'roarp_order', null=True)
    room = models.ForeignKey('reserve.OrderAccommodationRoom', models.CASCADE, 'roarp_room', null=True)
    date = models.DateField(null=True)
    grs_inventory_at_reserve = models.IntegerField(null=True)
    grs_rack_rate = models.IntegerField(null=True)
    grs_daily_rate = models.IntegerField(null=True)
    grs_grs_rate = models.IntegerField(null=True)
    grs_baby_cot_rack_rate = models.IntegerField(null=True)
    grs_baby_cot_daily_rate = models.IntegerField(null=True)
    grs_baby_cot_grs_rate = models.IntegerField(null=True)
    grs_extend_bed_rack_rate = models.IntegerField(null=True)
    grs_extend_bed_daily_rate = models.IntegerField(null=True)
    grs_extend_bed_grs_rate = models.IntegerField(null=True)
    grs_reservation_state = models.TextField(null=True)
    grs_min_stay = models.IntegerField(null=True)
    grs_max_stay = models.IntegerField(null=True)
    grs_close_to_arrival = models.BooleanField(null=True)
    grs_close_to_departure = models.BooleanField(null=True)
    grs_closed = models.BooleanField(null=True)


class OrderAccommodationRoomType(models.Model):
    class Meta:
        db_table = 'reserve_order_accommodation_room_type'

    order = models.ForeignKey('reserve.Order', models.RESTRICT, 'roart_order', null=True)
    room = models.ForeignKey('reserve.OrderAccommodationRoom', models.CASCADE, 'roart_room', null=True)
    grs_id = models.IntegerField(default=0, null=True)
    grs_name = models.CharField(max_length=100, null=True)
    grs_type = models.CharField(max_length=100, null=True)
    grs_capacity = models.IntegerField(default=1, null=True)
    grs_extra_capacity = models.IntegerField(default=1, null=True)
    grs_single_bed_count = models.IntegerField(default=1, null=True)
    grs_double_bed_count = models.IntegerField(default=1, null=True)
    grs_sofa_bed_count = models.IntegerField(default=1, null=True)
    grs_out_of_service = models.BooleanField(default=False)
    grs_accept_child = models.BooleanField(default=True)
    grs_description = models.TextField(null=True)


class OrderAccommodationRoomRatePlan(models.Model):
    class Meta:
        db_table = 'reserve_order_accommodation_room_rate_plan'

    order = models.ForeignKey('reserve.Order', models.RESTRICT, 'roarrp_order', null=True)
    room = models.ForeignKey('reserve.OrderAccommodationRoom', models.CASCADE, 'roarrp_room', null=True)
    grs_id = models.IntegerField(null=True)
    grs_nationality = models.TextField(null=True)
    grs_name = models.CharField(max_length=100, null=True)
    grs_breakfast_rate = models.IntegerField(null=True)
    grs_half_board_rate = models.IntegerField(null=True)
    grs_full_board_rate = models.IntegerField(null=True)
    grs_food_board_type = models.CharField(max_length=100, null=True)
    grs_cancelable = models.BooleanField(default=False)
    grs_sleeps = models.CharField(max_length=100, null=True)
    grs_min_stay = models.IntegerField(null=True)
    grs_max_stay = models.IntegerField(null=True)


class OrderFlight(models.Model):
    class Meta:
        db_table = 'reserve_order_flight'

    order = models.ForeignKey('reserve.Order', models.CASCADE, 'rof_order', null=True)
    reserve_id = models.IntegerField(null=True)
    hash_id = models.CharField(max_length=100, null=True)
    main_price = models.IntegerField(null=True)
    total_price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    is_international = models.BooleanField(null=True)
    airline = models.CharField(max_length=100, null=True)
    airline_name = models.CharField(max_length=100, null=True)
    airline_logo = models.TextField(null=True)
    flight_number = models.CharField(max_length=45, null=True)
    aircraft = models.CharField(max_length=100, null=True)
    departure = models.ForeignKey('basic.City', models.CASCADE, 'rof_departure', null=True)
    departure_date = models.DateTimeField(null=True)
    departure_terminal = models.TextField(null=True)
    destination = models.ForeignKey('basic.City', models.CASCADE, 'rof_destination', null=True)
    destination_date = models.DateTimeField(null=True)
    destination_terminal = models.TextField(null=True)
    duration = models.CharField(max_length=45, null=True)
    cobin = models.CharField(max_length=45, null=True)
    cobin_name = models.CharField(max_length=45, null=True)
    type = models.CharField(max_length=45, null=True)
    refundable = models.BooleanField(null=True)


class OrderFlightPassenger(models.Model):
    class Meta:
        db_table = 'reserve_order_flight_passenger'

    flight = models.ForeignKey('reserve.OrderFlight', models.CASCADE, 'rofp_flight', null=True)
    order = models.ForeignKey('reserve.Order', models.CASCADE, 'rofp_order', null=True)
    gender = models.CharField(max_length=10, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    english_first_name = models.CharField(max_length=100, null=True)
    english_last_name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=10, null=True)
    national_id = models.CharField(max_length=15, null=True)
    passport_number = models.CharField(max_length=45, null=True)
    passport_expire_date = models.DateField(null=True)
    total_price = models.IntegerField(null=True)
    birthdate = models.DateField(null=True)
    fare_price = models.IntegerField(null=True)
    tax_price = models.IntegerField(null=True)


class OrderFlightRule(models.Model):
    class Meta:
        db_table = 'reserve_order_flight_rule'

    flight = models.ForeignKey('reserve.OrderFlight', models.CASCADE, 'rofr_flight', null=True)
    order = models.ForeignKey('reserve.Order', models.CASCADE, 'rofr_order', null=True)
    rule = models.TextField(null=True)


class OrderPayment(models.Model):
    class Meta:
        db_table = 'reserve_order_payment'

    class Type:
        ONLINE = 0
        BANK_RECEIPT = 1
        WALLET = 2
        CREDIT = 3
        CHEQUE = 4
        LOAN = 5
        DIGITAL_CURRENCY = 6

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('accounts.User', models.RESTRICT, 'ropa_user', null=True)
    order = models.ForeignKey('reserve.Order', models.RESTRICT, 'ropa_order', null=True)
    pay_date = models.DateTimeField(null=True)
    price = models.PositiveIntegerField(default=0)
    payment_reference = models.TextField(null=True)
    terminal = models.CharField(max_length=15, null=True)
    tracking_id = models.TextField(null=True)
    rrn = models.TextField(null=True)
    reference_number = models.CharField(max_length=50, null=True, unique=True)
    card = models.TextField(null=True)
    hashed_card = models.TextField(null=True)
    payment_type = models.IntegerField(default=Type.ONLINE)
    currency = models.IntegerField(default=Order.Currency.IRR)
    token = models.TextField(null=True)
    token_expiry = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    is_confirm = models.BooleanField(default=False)
    type = models.IntegerField(default=0)

    @property
    def get_type(self):
        match self.type:
            case OrderPayment.Type.ONLINE:
                return {'id': OrderPayment.Type.ONLINE, 'type': 'پرداخت آنلاین'}
            case OrderPayment.Type.BANK_RECEIPT:
                return {'id': OrderPayment.Type.BANK_RECEIPT, 'type': 'فیش بانکی'}
            case OrderPayment.Type.WALLET:
                return {'id': OrderPayment.Type.WALLET, 'type': 'کیف پول'}
            case OrderPayment.Type.CREDIT:
                return {'id': OrderPayment.Type.CREDIT, 'type': 'اعتباری'}
            case OrderPayment.Type.CHEQUE:
                return {'id': OrderPayment.Type.CHEQUE, 'type': 'چک'}
            case OrderPayment.Type.LOAN:
                return {'id': OrderPayment.Type.LOAN, 'type': 'وام'}
            case OrderPayment.Type.DIGITAL_CURRENCY:
                return {'id': OrderPayment.Type.DIGITAL_CURRENCY, 'type': 'ارز دیجیتال'}
            case _:
                return 'نامشخص'


class OrderSubscribe(models.Model):
    class Meta:
        db_table = 'reserve_order_subscribe'

    user = models.ForeignKey('accounts.User', models.CASCADE, 'ros_user', null=True)
    order = models.ForeignKey('reserve.Order', models.CASCADE, 'ros_order', null=True)
    subscribe = models.ForeignKey(
        'basic.Subscribe', models.CASCADE, 'ros_subscribe', null=True
    )
    month = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)


class OrderTour(models.Model):
    class Meta:
        db_table = 'reserve_order_tour'

    user = models.ForeignKey('accounts.User', models.CASCADE, 'roto_user', null=True)
    order = models.ForeignKey('reserve.Order', models.CASCADE, 'roto_order', null=True)
    # tour = models.ForeignKey('itinerary.Tour', models.CASCADE, 'roto_tour', null=True)


class OrderCancellation(models.Model):
    class Meta:
        db_table = 'reserve_order_cancellation'

    class Status:
        PENDING = 1
        CANCELED = 2
        REJECTED = 3

    order = models.ForeignKey('reserve.Order', models.CASCADE, 'roc_order', null=True)
    accommodation = models.ForeignKey('reserve.OrderAccommodation', models.CASCADE, 'roc_accommodation', null=True)
    room = models.ForeignKey('reserve.OrderAccommodationRoom', models.CASCADE, 'roc_room', null=True)
    flight = models.ForeignKey('reserve.OrderFlight', models.CASCADE, 'roc_flight', null=True)
    flight_passenger = models.ForeignKey(
        'reserve.OrderFlightPassenger', models.CASCADE, 'roc_flight_passenger', null=True)
    description = models.TextField(null=True)
    date = models.DateTimeField(null=True)
    status = models.IntegerField(default=0)


class CacheAccommodation(models.Model):
    class Meta:
        db_table = 'reserve_cache_accommodation'

    accommodation = models.ForeignKey('basic.Accommodation', models.CASCADE, 'rca_accommodation', null=True)
    grs_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    city = models.ForeignKey('basic.City', models.CASCADE, 'rca_city', null=True)


class CacheAccommodationRoom(models.Model):
    class Meta:
        db_table = 'reserve_cache_accommodation_room'

    accommodation = models.ForeignKey('reserve.CacheAccommodation', models.CASCADE, 'rcar_accommodation', null=True)
    room_id = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    extra_capacity = models.IntegerField(null=True, blank=True)


class CacheAccommodationRoomRate(models.Model):
    class Meta:
        db_table = 'reserve_cache_accommodation_room_rate'

    room = models.ForeignKey('reserve.CacheAccommodationRoom', models.CASCADE, 'rcarr_room', null=True)
    rate_id = models.IntegerField(null=True, blank=True)
    country_id = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    name = models.TextField(null=True)
    meal_type_included = models.TextField(null=True)
    food_board_type = models.TextField(null=True)
    breakfast_rate = models.IntegerField(null=True, blank=True)
    half_board_rate = models.IntegerField(null=True, blank=True)
    full_board_rate = models.IntegerField(null=True, blank=True)
    cancelable = models.BooleanField(default=False)
    sleeps = models.CharField(max_length=255, null=True, blank=True)


class CacheAccommodationRoomRatePrice(models.Model):
    class Meta:
        db_table = 'reserve_cache_accommodation_room_rate_price'

    rate = models.ForeignKey('reserve.CacheAccommodationRoomRate', models.CASCADE, 'rcarrp_rate', null=True)
    date = models.DateField(null=True)
    inventory = models.IntegerField(default=0, null=True, blank=True)
    rack_rate = models.IntegerField(default=0, null=True, blank=True)
    daily_rate = models.IntegerField(default=0, null=True, blank=True)
    grs_rate = models.IntegerField(default=0, null=True, blank=True)
    baby_cot_rack_rate = models.IntegerField(default=0, null=True, blank=True)
    baby_cot_daily_rate = models.IntegerField(default=0, null=True, blank=True)
    baby_cot_grs_rate = models.IntegerField(default=0, null=True, blank=True)
    extend_bed_rack_rate = models.IntegerField(default=0, null=True, blank=True)
    extend_bed_daily_rate = models.IntegerField(default=0, null=True, blank=True)
    extend_bed_grs_rate = models.IntegerField(default=0, null=True, blank=True)
    reservation_state = models.CharField(max_length=100, null=True, blank=True)
    min_stay = models.IntegerField(null=True, blank=True)
    max_stay = models.IntegerField(null=True, blank=True)
    close_to_arrival = models.BooleanField(default=False)
    close_to_departure = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
