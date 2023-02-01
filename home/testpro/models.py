from django.db import models

# Create your models here.


class Personal(models.Model):
    email = models.EmailField(max_length=25, primary_key=True)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    phone = models.BigIntegerField(unique=True, default=91)
    street = models.CharField(max_length=40, default='something')
    city = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    bday = models.IntegerField()
    bmonth = models.CharField(max_length=10, default='januwary')
    byear = models.IntegerField(default=2000)

    def __str__(self):
        return self.email


class Station(models.Model):
    station_id = models.IntegerField(primary_key=True)
    station_name = models.CharField(max_length=30)
    station_platforms = models.IntegerField()


class Train(models.Model):
    PNR = models.CharField(max_length=30, primary_key=True)
    name_of_train = models.CharField(max_length=30)
    no_of_coach = models.IntegerField(default=0)
    no_of_seats_in_general = models.IntegerField(default=0)
    no_of_seats_in_Sleeper = models.IntegerField(default=0)
    no_of_seats_in_AC = models.IntegerField(default=0)
    dept_time = models.TimeField()
    dept_date = models.DateField()
    arriv_time = models.TimeField()
    Source = models.CharField(max_length=50, default=None)
    Destination = models.CharField(max_length=50, default=None)
    arriv_date = models.DateField()

    def __str__(self):
        return self.PNR


class Cld(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    amt = models.IntegerField(default=0)
    class_at = models.CharField(max_length=20)
    seat_no = models.CharField(max_length=5, default=None)
    aval = models.CharField(max_length=10, default='TRUE')
    train = models.ForeignKey(Train, on_delete=models.CASCADE)


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=10)
    seat_no = models.CharField(max_length=5, default=None)


class Payment(models.Model):
    tno = models.ForeignKey('Train', on_delete=models.CASCADE)
    personal = models.ForeignKey('Personal', on_delete=models.CASCADE)
    cld = models.ForeignKey('Cld', on_delete=models.CASCADE, default=None)
    pnr = models.CharField(max_length=50)
    amt = models.IntegerField(default=0)
    cancel = models.CharField(max_length=50)
