# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OcAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    company = models.CharField(max_length=40)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    custom_field = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_address'


class OcAddressSimpleFields(models.Model):
    address_id = models.IntegerField(primary_key=True)
    metadata = models.TextField(blank=True, null=True)
    field_customer_street = models.TextField(blank=True, null=True)
    field_customer_house = models.TextField(blank=True, null=True)
    field_customer_apartments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_address_simple_fields'


class OcAffiliate(models.Model):
    affiliate_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    company = models.CharField(max_length=40)
    website = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    code = models.CharField(max_length=64)
    commission = models.DecimalField(max_digits=4, decimal_places=2)
    tax = models.CharField(max_length=64)
    payment = models.CharField(max_length=6)
    cheque = models.CharField(max_length=100)
    paypal = models.CharField(max_length=64)
    bank_name = models.CharField(max_length=64)
    bank_branch_number = models.CharField(max_length=64)
    bank_swift_code = models.CharField(max_length=64)
    bank_account_name = models.CharField(max_length=64)
    bank_account_number = models.CharField(max_length=64)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate'


class OcAffiliateActivity(models.Model):
    affiliate_activity_id = models.AutoField(primary_key=True)
    affiliate_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_activity'


class OcAffiliateLogin(models.Model):
    affiliate_login_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=96)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_login'


class OcAffiliateTransaction(models.Model):
    affiliate_transaction_id = models.AutoField(primary_key=True)
    affiliate_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_transaction'


class OcApi(models.Model):
    api_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    key = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_api'


class OcApiIp(models.Model):
    api_ip_id = models.AutoField(primary_key=True)
    api_id = models.IntegerField()
    ip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'oc_api_ip'


class OcApiSession(models.Model):
    api_session_id = models.AutoField(primary_key=True)
    api_id = models.IntegerField()
    token = models.CharField(max_length=32)
    session_id = models.CharField(max_length=32)
    session_name = models.CharField(max_length=32)
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_api_session'


class OcAttribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    attribute_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_attribute'


class OcAttributeDescription(models.Model):
    attribute_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_attribute_description'
        unique_together = (('attribute_id', 'language_id'),)


class OcAttributeGroup(models.Model):
    attribute_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_attribute_group'


class OcAttributeGroupDescription(models.Model):
    attribute_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_attribute_group_description'
        unique_together = (('attribute_group_id', 'language_id'),)


class OcBanner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_banner'


class OcBannerImage(models.Model):
    banner_image_id = models.AutoField(primary_key=True)
    banner_id = models.IntegerField()
    language_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_banner_image'


class OcCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    api_id = models.IntegerField()
    customer_id = models.IntegerField()
    session_id = models.CharField(max_length=32)
    product_id = models.IntegerField()
    recurring_id = models.IntegerField()
    option = models.TextField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_cart'


class OcCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField(default=0)
    top = models.IntegerField(default=1)
    column = models.IntegerField(default=0)
    sort_order = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'oc_category'
        unique_together = (('category_id', 'parent_id'),)


class OcCategoryDescription(models.Model):
    category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField(default=1)
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    meta_title = models.CharField(max_length=255, default='')
    meta_h1 = models.CharField(max_length=255, default='')
    meta_description = models.CharField(max_length=255, default='')
    meta_keyword = models.CharField(max_length=255, default='')

    class Meta:
        managed = False
        db_table = 'oc_category_description'
        unique_together = (('category_id', 'language_id'),)


class OcCategoryFilter(models.Model):
    category_id = models.IntegerField(primary_key=True)
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_filter'
        unique_together = (('category_id', 'filter_id'),)


class OcCategoryPath(models.Model):
    category_id = models.IntegerField(primary_key=True)
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_path'
        unique_together = (('category_id', 'path_id'),)


class OcCategoryToLayout(models.Model):
    category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_layout'
        unique_together = (('category_id', 'store_id'),)


class OcCategoryToStore(models.Model):
    category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_store'
        unique_together = (('category_id', 'store_id'),)


class OcCountry(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    iso_code_2 = models.CharField(max_length=2)
    iso_code_3 = models.CharField(max_length=3)
    address_format = models.TextField()
    postcode_required = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_country'


class OcCoupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=20)
    type = models.CharField(max_length=1)
    discount = models.DecimalField(max_digits=15, decimal_places=4)
    logged = models.IntegerField()
    shipping = models.IntegerField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()
    uses_total = models.IntegerField()
    uses_customer = models.CharField(max_length=11)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_coupon'


class OcCouponCategory(models.Model):
    coupon_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_category'
        unique_together = (('coupon_id', 'category_id'),)


class OcCouponHistory(models.Model):
    coupon_history_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_history'


class OcCouponProduct(models.Model):
    coupon_product_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_product'


class OcCurrency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    code = models.CharField(max_length=3)
    symbol_left = models.CharField(max_length=12)
    symbol_right = models.CharField(max_length=128)
    decimal_place = models.CharField(max_length=1)
    value = models.FloatField()
    status = models.IntegerField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_currency'


class OcCustomField(models.Model):
    custom_field_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    value = models.TextField()
    validation = models.CharField(max_length=255)
    location = models.CharField(max_length=7)
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field'


class OcCustomFieldCustomerGroup(models.Model):
    custom_field_id = models.IntegerField(primary_key=True)
    customer_group_id = models.IntegerField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field_customer_group'
        unique_together = (('custom_field_id', 'customer_group_id'),)


class OcCustomFieldDescription(models.Model):
    custom_field_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_custom_field_description'
        unique_together = (('custom_field_id', 'language_id'),)


class OcCustomFieldValue(models.Model):
    custom_field_value_id = models.AutoField(primary_key=True)
    custom_field_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field_value'


class OcCustomFieldValueDescription(models.Model):
    custom_field_value_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_custom_field_value_description'
        unique_together = (('custom_field_value_id', 'language_id'),)


class OcCustomer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_group_id = models.IntegerField()
    store_id = models.IntegerField()
    language_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    cart = models.TextField(blank=True, null=True)
    wishlist = models.TextField(blank=True, null=True)
    newsletter = models.IntegerField()
    address_id = models.IntegerField()
    custom_field = models.TextField()
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    safe = models.IntegerField()
    token = models.TextField()
    code = models.CharField(max_length=40)
    date_added = models.DateTimeField()
    socnetauth2_identity = models.CharField(max_length=300)
    socnetauth2_link = models.CharField(max_length=100)
    socnetauth2_provider = models.CharField(max_length=100)
    socnetauth2_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_customer'


class OcCustomerActivity(models.Model):
    customer_activity_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_activity'


class OcCustomerGroup(models.Model):
    customer_group_id = models.AutoField(primary_key=True)
    approval = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customer_group'


class OcCustomerGroupDescription(models.Model):
    customer_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_customer_group_description'
        unique_together = (('customer_group_id', 'language_id'),)


class OcCustomerHistory(models.Model):
    customer_history_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_history'


class OcCustomerIp(models.Model):
    customer_ip_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_ip'


class OcCustomerLogin(models.Model):
    customer_login_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=96)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_login'


class OcCustomerOnline(models.Model):
    ip = models.CharField(primary_key=True, max_length=40)
    customer_id = models.IntegerField()
    url = models.TextField()
    referer = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_online'


class OcCustomerReward(models.Model):
    customer_reward_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_reward'


class OcCustomerSearch(models.Model):
    customer_search_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    language_id = models.IntegerField()
    customer_id = models.IntegerField()
    keyword = models.CharField(max_length=255)
    category_id = models.IntegerField(blank=True, null=True)
    sub_category = models.IntegerField()
    description = models.IntegerField()
    products = models.IntegerField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_search'


class OcCustomerSimpleFields(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    metadata = models.TextField(blank=True, null=True)
    field23 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_customer_simple_fields'


class OcCustomerTransaction(models.Model):
    customer_transaction_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_transaction'


class OcCustomerWishlist(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_wishlist'
        unique_together = (('customer_id', 'product_id'),)


class OcDownload(models.Model):
    download_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=140)
    mask = models.CharField(max_length=128)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_download'


class OcDownloadDescription(models.Model):
    download_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_download_description'
        unique_together = (('download_id', 'language_id'),)


class OcEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=32)
    trigger = models.TextField()
    action = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_event'


class OcExtension(models.Model):
    extension_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_extension'


class OcFilter(models.Model):
    filter_id = models.AutoField(primary_key=True)
    filter_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_filter'


class OcFilterDescription(models.Model):
    filter_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    filter_group_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_filter_description'
        unique_together = (('filter_id', 'language_id'),)


class OcFilterGroup(models.Model):
    filter_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_filter_group'


class OcFilterGroupDescription(models.Model):
    filter_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_filter_group_description'
        unique_together = (('filter_group_id', 'language_id'),)


class OcGeoZone(models.Model):
    geo_zone_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_modified = models.DateTimeField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_geo_zone'


class OcInformation(models.Model):
    information_id = models.AutoField(primary_key=True)
    bottom = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information'


class OcInformationDescription(models.Model):
    information_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_h1 = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_information_description'
        unique_together = (('information_id', 'language_id'),)


class OcInformationToLayout(models.Model):
    information_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information_to_layout'
        unique_together = (('information_id', 'store_id'),)


class OcInformationToStore(models.Model):
    information_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information_to_store'
        unique_together = (('information_id', 'store_id'),)


class OcLanguage(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=5)
    locale = models.CharField(max_length=255)
    image = models.CharField(max_length=64)
    directory = models.CharField(max_length=32)
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_language'


class OcLayout(models.Model):
    layout_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_layout'


class OcLayoutModule(models.Model):
    layout_module_id = models.AutoField(primary_key=True)
    layout_id = models.IntegerField()
    code = models.CharField(max_length=64)
    position = models.CharField(max_length=14)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_layout_module'


class OcLayoutRoute(models.Model):
    layout_route_id = models.AutoField(primary_key=True)
    layout_id = models.IntegerField()
    store_id = models.IntegerField()
    route = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_layout_route'


class OcLengthClass(models.Model):
    length_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_length_class'


class OcLengthClassDescription(models.Model):
    length_class_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'oc_length_class_description'
        unique_together = (('length_class_id', 'language_id'),)


class OcLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    address = models.TextField()
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    geocode = models.CharField(max_length=32)
    image = models.CharField(max_length=255, blank=True, null=True)
    open = models.TextField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_location'


class OcManufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'oc_manufacturer'


class OcManufacturerDescription(models.Model):
    manufacturer_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField(default=1)
    name = models.CharField(max_length=64)
    description = models.TextField(default='')
    meta_title = models.CharField(max_length=255)
    meta_h1 = models.CharField(max_length=255, default='')
    meta_description = models.CharField(max_length=255, default='')
    meta_keyword = models.CharField(max_length=255, default='')

    class Meta:
        managed = False
        db_table = 'oc_manufacturer_description'
        unique_together = (('manufacturer_id', 'language_id'),)


class OcManufacturerToStore(models.Model):
    manufacturer_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_manufacturer_to_store'
        unique_together = (('manufacturer_id', 'store_id'),)


class OcMarketing(models.Model):
    marketing_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.TextField()
    code = models.CharField(max_length=64)
    clicks = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_marketing'


class OcMenu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    type = models.CharField(max_length=6)
    link = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_menu'


class OcMenuDescription(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_menu_description'
        unique_together = (('menu_id', 'language_id'),)


class OcMenuModule(models.Model):
    menu_module_id = models.IntegerField(primary_key=True)
    menu_id = models.IntegerField()
    code = models.CharField(max_length=64)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_menu_module'


class OcModification(models.Model):
    modification_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    version = models.CharField(max_length=32)
    link = models.CharField(max_length=255)
    xml = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_modification'


class OcModule(models.Model):
    module_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=32)
    setting = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_module'


class OcOaslIdentity(models.Model):
    oasl_identity_id = models.AutoField(primary_key=True)
    oasl_user_id = models.PositiveIntegerField()
    identity_token = models.CharField(max_length=36)
    identity_provider = models.CharField(max_length=255)
    num_logins = models.IntegerField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_oasl_identity'


class OcOaslUser(models.Model):
    oasl_user_id = models.AutoField(primary_key=True)
    customer_id = models.PositiveIntegerField()
    user_token = models.CharField(max_length=36)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_oasl_user'


class OcOcfilterOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=16)
    keyword = models.CharField(max_length=255)
    selectbox = models.IntegerField()
    grouping = models.IntegerField()
    color = models.IntegerField()
    image = models.IntegerField()
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_ocfilter_option'


class OcOcfilterOptionDescription(models.Model):
    option_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    postfix = models.CharField(max_length=32)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_ocfilter_option_description'
        unique_together = (('option_id', 'language_id'),)


class OcOcfilterOptionToCategory(models.Model):
    option_id = models.IntegerField()
    category_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'oc_ocfilter_option_to_category'
        unique_together = (('category_id', 'option_id'),)


class OcOcfilterOptionToStore(models.Model):
    option_id = models.IntegerField()
    store_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'oc_ocfilter_option_to_store'
        unique_together = (('store_id', 'option_id'),)


class OcOcfilterOptionValue(models.Model):
    value_id = models.BigAutoField(primary_key=True)
    option_id = models.IntegerField()
    keyword = models.CharField(max_length=255)
    color = models.CharField(max_length=6)
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_ocfilter_option_value'
        unique_together = (('value_id', 'option_id'),)


class OcOcfilterOptionValueDescription(models.Model):
    value_id = models.BigIntegerField(primary_key=True)
    option_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_ocfilter_option_value_description'
        unique_together = (('value_id', 'language_id'),)


class OcOcfilterOptionValueToProduct(models.Model):
    ocfilter_option_value_to_product_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    value_id = models.BigIntegerField()
    slide_value_min = models.DecimalField(max_digits=15, decimal_places=4)
    slide_value_max = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'oc_ocfilter_option_value_to_product'


class OcOcfilterOptionValueToProductDescription(models.Model):
    product_id = models.IntegerField(primary_key=True)
    value_id = models.BigIntegerField()
    option_id = models.IntegerField()
    language_id = models.IntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_ocfilter_option_value_to_product_description'
        unique_together = (('product_id', 'value_id', 'option_id', 'language_id'),)


class OcOcfilterPage(models.Model):
    ocfilter_page_id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()
    ocfilter_params = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    description = models.TextField()
    title = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_ocfilter_page'


class OcOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_option'


class OcOptionDescription(models.Model):
    option_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_option_description'
        unique_together = (('option_id', 'language_id'),)


class OcOptionValue(models.Model):
    option_value_id = models.AutoField(primary_key=True)
    option_id = models.IntegerField()
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_option_value'


class OcOptionValueDescription(models.Model):
    option_value_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    option_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_option_value_description'
        unique_together = (('option_value_id', 'language_id'),)


class OcOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    invoice_no = models.IntegerField()
    invoice_prefix = models.CharField(max_length=26)
    store_id = models.IntegerField()
    store_name = models.CharField(max_length=64)
    store_url = models.CharField(max_length=255)
    customer_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    custom_field = models.TextField()
    payment_firstname = models.CharField(max_length=32)
    payment_lastname = models.CharField(max_length=32)
    payment_company = models.CharField(max_length=40)
    payment_address_1 = models.CharField(max_length=128)
    payment_address_2 = models.CharField(max_length=128)
    payment_city = models.CharField(max_length=128)
    payment_postcode = models.CharField(max_length=10)
    payment_country = models.CharField(max_length=128)
    payment_country_id = models.IntegerField()
    payment_zone = models.CharField(max_length=128)
    payment_zone_id = models.IntegerField()
    payment_address_format = models.TextField()
    payment_custom_field = models.TextField()
    payment_method = models.CharField(max_length=128)
    payment_code = models.CharField(max_length=128)
    shipping_firstname = models.CharField(max_length=32)
    shipping_lastname = models.CharField(max_length=32)
    shipping_company = models.CharField(max_length=40)
    shipping_address_1 = models.CharField(max_length=128)
    shipping_address_2 = models.CharField(max_length=128)
    shipping_city = models.CharField(max_length=128)
    shipping_postcode = models.CharField(max_length=10)
    shipping_country = models.CharField(max_length=128)
    shipping_country_id = models.IntegerField()
    shipping_zone = models.CharField(max_length=128)
    shipping_zone_id = models.IntegerField()
    shipping_address_format = models.TextField()
    shipping_custom_field = models.TextField()
    shipping_method = models.CharField(max_length=128)
    shipping_code = models.CharField(max_length=128)
    comment = models.TextField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    order_status_id = models.IntegerField()
    affiliate_id = models.IntegerField()
    commission = models.DecimalField(max_digits=15, decimal_places=4)
    marketing_id = models.IntegerField()
    tracking = models.CharField(max_length=64)
    language_id = models.IntegerField()
    currency_id = models.IntegerField()
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(max_digits=15, decimal_places=8)
    ip = models.CharField(max_length=40)
    forwarded_ip = models.CharField(max_length=40)
    user_agent = models.CharField(max_length=255)
    accept_language = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order'


class OcOrderCustomField(models.Model):
    order_custom_field_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    custom_field_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)
    location = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'oc_order_custom_field'


class OcOrderHistory(models.Model):
    order_history_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_history'


class OcOrderOption(models.Model):
    order_option_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_product_id = models.IntegerField()
    product_option_id = models.IntegerField()
    product_option_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_order_option'


class OcOrderProduct(models.Model):
    order_product_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    total = models.DecimalField(max_digits=15, decimal_places=4)
    tax = models.DecimalField(max_digits=15, decimal_places=4)
    reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_order_product'


class OcOrderRecurring(models.Model):
    order_recurring_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_quantity = models.IntegerField()
    recurring_id = models.IntegerField()
    recurring_name = models.CharField(max_length=255)
    recurring_description = models.CharField(max_length=255)
    recurring_frequency = models.CharField(max_length=25)
    recurring_cycle = models.SmallIntegerField()
    recurring_duration = models.SmallIntegerField()
    recurring_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial = models.IntegerField()
    trial_frequency = models.CharField(max_length=25)
    trial_cycle = models.SmallIntegerField()
    trial_duration = models.SmallIntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_recurring'


class OcOrderRecurringTransaction(models.Model):
    order_recurring_transaction_id = models.AutoField(primary_key=True)
    order_recurring_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_recurring_transaction'


class OcOrderSimpleFields(models.Model):
    order_id = models.IntegerField(primary_key=True)
    metadata = models.TextField(blank=True, null=True)
    payment_field_customer_street = models.TextField(blank=True, null=True)
    shipping_field_customer_street = models.TextField(blank=True, null=True)
    payment_field_customer_house = models.TextField(blank=True, null=True)
    shipping_field_customer_house = models.TextField(blank=True, null=True)
    payment_field_customer_apartments = models.TextField(blank=True, null=True)
    shipping_field_customer_apartments = models.TextField(blank=True, null=True)
    field23 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_order_simple_fields'


class OcOrderStatus(models.Model):
    order_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_order_status'
        unique_together = (('order_status_id', 'language_id'),)


class OcOrderTotal(models.Model):
    order_total_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=4)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_order_total'


class OcOrderVoucher(models.Model):
    order_voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    voucher_id = models.IntegerField()
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'oc_order_voucher'


class OcProduct(models.Model):
    product_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=64, default='')
    sku = models.CharField(max_length=64, default='')
    upc = models.CharField(max_length=12, default='')
    ean = models.CharField(max_length=14, default='')
    jan = models.CharField(max_length=13, default='')
    isbn = models.CharField(max_length=17, default='')
    mpn = models.CharField(max_length=64, default='')
    location = models.CharField(max_length=128, default='')
    quantity = models.IntegerField(default=0)
    stock_status_id = models.IntegerField(default=-1)
    image = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_id = models.IntegerField(default=-1)
    shipping = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    points = models.IntegerField(default=0)
    tax_class_id = models.IntegerField(default=-1)
    date_available = models.DateField(auto_now_add=True)
    weight = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    weight_class_id = models.IntegerField(default=0)
    length = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    width = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    height = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    length_class_id = models.IntegerField(default=0)
    subtract = models.IntegerField(default=1)
    minimum = models.IntegerField(default=1)
    sort_order = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    viewed = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'oc_product'
# class OcProduct(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     model = models.CharField(max_length=64)
#     sku = models.CharField(max_length=64)
#     upc = models.CharField(max_length=12)
#     ean = models.CharField(max_length=14)
#     jan = models.CharField(max_length=13)
#     isbn = models.CharField(max_length=17)
#     mpn = models.CharField(max_length=64)
#     location = models.CharField(max_length=128)
#     quantity = models.IntegerField()
#     stock_status_id = models.IntegerField()
#     image = models.CharField(max_length=255, blank=True, null=True)
#     manufacturer_id = models.IntegerField()
#     shipping = models.IntegerField()
#     price = models.DecimalField(max_digits=15, decimal_places=4)
#     points = models.IntegerField()
#     tax_class_id = models.IntegerField()
#     date_available = models.DateField()
#     weight = models.DecimalField(max_digits=15, decimal_places=2)
#     weight_class_id = models.IntegerField()
#     length = models.DecimalField(max_digits=15, decimal_places=2)
#     width = models.DecimalField(max_digits=15, decimal_places=2)
#     height = models.DecimalField(max_digits=15, decimal_places=2)
#     length_class_id = models.IntegerField()
#     subtract = models.IntegerField()
#     minimum = models.IntegerField()
#     sort_order = models.IntegerField()
#     status = models.IntegerField()
#     viewed = models.IntegerField()
#     date_added = models.DateTimeField()
#     date_modified = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'oc_product'


class OcProductAttribute(models.Model):
    product_id = models.IntegerField(primary_key=True)
    attribute_id = models.IntegerField()
    language_id = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_product_attribute'
        unique_together = (('product_id', 'attribute_id', 'language_id'),)


class OcProductDescription(models.Model):
    product_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField(default=1)
    name = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_h1 = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_product_description'
        unique_together = (('product_id', 'language_id'),)


class OcProductDiscount(models.Model):
    product_discount_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    quantity = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_product_discount'


class OcProductFilter(models.Model):
    product_id = models.IntegerField(primary_key=True)
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_filter'
        unique_together = (('product_id', 'filter_id'),)


class OcProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'oc_product_image'


class OcProductOption(models.Model):
    product_option_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    value = models.TextField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_option'


class OcProductOptionValue(models.Model):
    product_option_value_id = models.AutoField(primary_key=True)
    product_option_id = models.IntegerField()
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    option_value_id = models.IntegerField()
    quantity = models.IntegerField()
    subtract = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    price_prefix = models.CharField(max_length=1)
    points = models.IntegerField()
    points_prefix = models.CharField(max_length=1)
    weight = models.DecimalField(max_digits=15, decimal_places=2)
    weight_prefix = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'oc_product_option_value'


class OcProductRecurring(models.Model):
    product_id = models.IntegerField(primary_key=True)
    recurring_id = models.IntegerField()
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_recurring'
        unique_together = (('product_id', 'recurring_id', 'customer_group_id'),)


class OcProductRelated(models.Model):
    product_id = models.IntegerField(primary_key=True)
    related_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_related'
        unique_together = (('product_id', 'related_id'),)


class OcProductReward(models.Model):
    product_reward_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_reward'


class OcProductSpecial(models.Model):
    product_special_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'oc_product_special'


class OcProductToCategory(models.Model):
    product_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()
    main_category = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_category'
        unique_together = (('product_id', 'category_id'),)


class OcProductToDownload(models.Model):
    product_id = models.IntegerField(primary_key=True)
    download_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_download'
        unique_together = (('product_id', 'download_id'),)


class OcProductToLayout(models.Model):
    product_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_layout'
        unique_together = (('product_id', 'store_id'),)


class OcProductToStore(models.Model):
    product_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_store'
        unique_together = (('product_id', 'store_id'),)


class OcRecurring(models.Model):
    recurring_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    frequency = models.CharField(max_length=10)
    duration = models.PositiveIntegerField()
    cycle = models.PositiveIntegerField()
    trial_status = models.IntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial_frequency = models.CharField(max_length=10)
    trial_duration = models.PositiveIntegerField()
    trial_cycle = models.PositiveIntegerField()
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_recurring'


class OcRecurringDescription(models.Model):
    recurring_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_recurring_description'
        unique_together = (('recurring_id', 'language_id'),)


class OcReturn(models.Model):
    return_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    product = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    opened = models.IntegerField()
    return_reason_id = models.IntegerField()
    return_action_id = models.IntegerField()
    return_status_id = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_ordered = models.DateField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_return'


class OcReturnAction(models.Model):
    return_action_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_return_action'
        unique_together = (('return_action_id', 'language_id'),)


class OcReturnHistory(models.Model):
    return_history_id = models.AutoField(primary_key=True)
    return_id = models.IntegerField()
    return_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_return_history'


class OcReturnReason(models.Model):
    return_reason_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_return_reason'
        unique_together = (('return_reason_id', 'language_id'),)


class OcReturnStatus(models.Model):
    return_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_return_status'
        unique_together = (('return_status_id', 'language_id'),)


class OcReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    author = models.CharField(max_length=64)
    text = models.TextField()
    rating = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_review'


class OcSetting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    code = models.CharField(max_length=32)
    key = models.CharField(max_length=64)
    value = models.TextField()
    serialized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_setting'


class OcSimpleBlogArticle(models.Model):
    simple_blog_article_id = models.IntegerField()
    simple_blog_author_id = models.IntegerField()
    allow_comment = models.IntegerField()
    image = models.TextField()
    featured_image = models.TextField()
    article_related_method = models.CharField(max_length=64)
    article_related_option = models.TextField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article'


class OcSimpleBlogArticleDescription(models.Model):
    simple_blog_article_description_id = models.IntegerField()
    simple_blog_article_id = models.IntegerField()
    language_id = models.IntegerField()
    article_title = models.CharField(max_length=256)
    description = models.TextField()
    meta_description = models.CharField(max_length=256)
    meta_keyword = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_description'


class OcSimpleBlogArticleDescriptionAdditional(models.Model):
    simple_blog_article_id = models.IntegerField()
    language_id = models.IntegerField()
    additional_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_description_additional'


class OcSimpleBlogArticleProductRelated(models.Model):
    simple_blog_article_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_product_related'


class OcSimpleBlogArticleToCategory(models.Model):
    simple_blog_article_id = models.IntegerField()
    simple_blog_category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_to_category'


class OcSimpleBlogArticleToLayout(models.Model):
    simple_blog_article_id = models.IntegerField()
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_to_layout'


class OcSimpleBlogArticleToStore(models.Model):
    simple_blog_article_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_article_to_store'


class OcSimpleBlogAuthor(models.Model):
    simple_blog_author_id = models.IntegerField()
    name = models.CharField(max_length=256)
    image = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_author'


class OcSimpleBlogAuthorDescription(models.Model):
    simple_blog_author_description_id = models.IntegerField()
    simple_blog_author_id = models.IntegerField()
    language_id = models.IntegerField()
    description = models.TextField()
    meta_description = models.CharField(max_length=256)
    meta_keyword = models.CharField(max_length=256)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_author_description'


class OcSimpleBlogCategory(models.Model):
    simple_blog_category_id = models.IntegerField()
    image = models.TextField()
    parent_id = models.IntegerField()
    top = models.IntegerField()
    blog_category_column = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_category'


class OcSimpleBlogCategoryDescription(models.Model):
    simple_blog_category_description_id = models.IntegerField()
    simple_blog_category_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=256)
    description = models.TextField()
    meta_description = models.CharField(max_length=256)
    meta_keyword = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_category_description'


class OcSimpleBlogCategoryToLayout(models.Model):
    simple_blog_category_id = models.IntegerField()
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_category_to_layout'


class OcSimpleBlogCategoryToStore(models.Model):
    simple_blog_category_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_category_to_store'


class OcSimpleBlogComment(models.Model):
    simple_blog_comment_id = models.IntegerField()
    simple_blog_article_id = models.IntegerField()
    simple_blog_article_reply_id = models.IntegerField()
    author = models.CharField(max_length=64)
    comment = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_comment'


class OcSimpleBlogRelatedArticle(models.Model):
    simple_blog_related_article_id = models.IntegerField()
    simple_blog_article_id = models.IntegerField()
    simple_blog_article_related_id = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_related_article'


class OcSimpleBlogView(models.Model):
    simple_blog_view_id = models.IntegerField()
    simple_blog_article_id = models.IntegerField()
    view = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_blog_view'


class OcSimpleCart(models.Model):
    simple_cart_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=96, blank=True, null=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    telephone = models.CharField(max_length=32, blank=True, null=True)
    products = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_simple_cart'


class OcSocnetauth2Customer2Account(models.Model):
    customer_id = models.CharField(max_length=100)
    identity = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    provider = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_socnetauth2_customer2account'


class OcSocnetauth2Records(models.Model):
    state = models.CharField(max_length=100)
    redirect = models.CharField(max_length=300)
    cdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_socnetauth2_records'


class OcStockStatus(models.Model):
    stock_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_stock_status'
        unique_together = (('stock_status_id', 'language_id'),)


class OcStore(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)
    ssl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_store'


class OcTaxClass(models.Model):
    tax_class_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_tax_class'


class OcTaxRate(models.Model):
    tax_rate_id = models.AutoField(primary_key=True)
    geo_zone_id = models.IntegerField()
    name = models.CharField(max_length=32)
    rate = models.DecimalField(max_digits=15, decimal_places=4)
    type = models.CharField(max_length=1)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rate'


class OcTaxRateToCustomerGroup(models.Model):
    tax_rate_id = models.IntegerField(primary_key=True)
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rate_to_customer_group'
        unique_together = (('tax_rate_id', 'customer_group_id'),)


class OcTaxRule(models.Model):
    tax_rule_id = models.AutoField(primary_key=True)
    tax_class_id = models.IntegerField()
    tax_rate_id = models.IntegerField()
    based = models.CharField(max_length=10)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rule'


class OcTheme(models.Model):
    theme_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    theme = models.CharField(max_length=64)
    route = models.CharField(max_length=64)
    code = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_theme'


class OcTmNewsletter(models.Model):
    tm_newsletter_id = models.AutoField(primary_key=True)
    tm_newsletter_email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_tm_newsletter'


class OcTranslation(models.Model):
    translation_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    language_id = models.IntegerField()
    route = models.CharField(max_length=64)
    key = models.CharField(max_length=64)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_translation'


class OcUlogin(models.Model):
    user_id = models.PositiveIntegerField()
    identity = models.CharField(max_length=255)
    network = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_ulogin'


class OcUpload(models.Model):
    upload_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_upload'


class OcUrlAlias(models.Model):
    url_alias_id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_url_alias'


class OcUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_group_id = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    image = models.CharField(max_length=255)
    code = models.CharField(max_length=40)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_user'


class OcUserGroup(models.Model):
    user_group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    permission = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_user_group'


class OcVoucher(models.Model):
    voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_voucher'


class OcVoucherHistory(models.Model):
    voucher_history_id = models.AutoField(primary_key=True)
    voucher_id = models.IntegerField()
    order_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_voucher_history'


class OcVoucherTheme(models.Model):
    voucher_theme_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_voucher_theme'


class OcVoucherThemeDescription(models.Model):
    voucher_theme_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_voucher_theme_description'
        unique_together = (('voucher_theme_id', 'language_id'),)


class OcWeightClass(models.Model):
    weight_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_weight_class'


class OcWeightClassDescription(models.Model):
    weight_class_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'oc_weight_class_description'
        unique_together = (('weight_class_id', 'language_id'),)


class OcZone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=32)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_zone'


class OcZoneToGeoZone(models.Model):
    zone_to_geo_zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    geo_zone_id = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_zone_to_geo_zone'
