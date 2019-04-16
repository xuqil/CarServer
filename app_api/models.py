from django.db import models


class Park(models.Model):
    park_id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=None)
    license_number = models.CharField(max_length=10, null=True)
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "park"


class AntiPark(models.Model):
    license_number = models.CharField(max_length=10, null=True)
    anti_num = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "anti_park"


class ParkTwo(models.Model):
    park_id = models.AutoField(primary_key=True, verbose_name=u"ID")
    inside = models.IntegerField(default=1, null=True, verbose_name=u"是否为校内车牌")
    license_number = models.CharField(max_length=10, null=True, unique=True, verbose_name=u"车牌号")
    create_time = models.DateTimeField(auto_now=True, null=True, verbose_name=u"创建时间")

    class Meta:
        db_table = "park_two"
        ordering = ['-create_time']
        verbose_name = u"校内车牌表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.license_number


class Card(models.Model):
    card_id = models.AutoField(primary_key=True, verbose_name=u"ID")
    card_number = models.CharField(default=None, unique=True, max_length=25, verbose_name=u"卡号")

    class Meta:
        db_table = "card"
        verbose_name = u"卡号表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.card_number


class InPark(models.Model):
    park_id = models.AutoField(primary_key=True, verbose_name=u"ID")
    inside = models.IntegerField(default=1, null=True, verbose_name=u"是否为校内车牌")
    license_number = models.CharField(max_length=10, null=True, unique=True, verbose_name=u"车牌号")
    create_time = models.DateTimeField(auto_now=True, null=True, verbose_name=u"创建时间")

    class Meta:
        db_table = "in_park"
        ordering = ['-create_time']
        verbose_name = u"校内停车场表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.license_number
