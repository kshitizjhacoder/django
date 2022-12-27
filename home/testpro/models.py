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


class Seat_id(models.Model):
    seat_no = models.CharField(max_length=10)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)


class Reservation(models.Model):
    tno = models.ForeignKey('Train', on_delete=models.CASCADE)
    personal = models.ForeignKey('Personal', on_delete=models.CASCADE)
    nos = models.ForeignKey(Seat_id, on_delete=models.CASCADE)
    amt = models.IntegerField()
    cls = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


class Payment(models.Model):
    tno = models.ForeignKey('Train', on_delete=models.CASCADE)
    personal = models.ForeignKey('Personal', on_delete=models.CASCADE)
    nos = models.ForeignKey(Seat_id, on_delete=models.CASCADE)
    pnr = models.CharField(max_length=50)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    cancel = models.CharField(max_length=50)
