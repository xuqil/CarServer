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
    park_id = models.AutoField(primary_key=True)
    inside = models.IntegerField(default=None, null=True)
    license_number = models.CharField(max_length=10, null=True)
    create_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "park_two"
