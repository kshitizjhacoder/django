from django.db import models

# Create your models here.


class Stock(models.Model):
    stock_id = models.IntegerField(primary_key=True, default=0)
    stock_name = models.CharField(max_length=30)
    stock_sname = models.CharField(max_length=10)
    sector_name = models.CharField(max_length=20)
    about = models.CharField(max_length=1024, default="nothing")


class Promotor_holding(models.Model):
    quarterly = models.CharField(max_length=25)
    promotor = models.FloatField(default=0.0)
    fii = models.FloatField(default=0.0)
    dii = models.FloatField(default=0.0)
    government = models.FloatField(default=0.0)
    public = models.FloatField(default=0.0)
    promotor_holding_id = models.ForeignKey(Stock, on_delete=models.CASCADE)


class Price(models.Model):
    mark_cap = models.CharField(max_length=30)
    curr_value = models.FloatField(default=0.0)
    face_value = models.FloatField(default=0.0)
    book_value = models.FloatField(default=0.0)
    high = models.FloatField(default=0.0)
    low = models.FloatField(default=0.0)
    dividend = models.FloatField(default=0.0)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


class PNL(models.Model):
    quaterly = models.CharField(max_length=25)
    sales = models.FloatField(default=0.0)
    expense = models.FloatField(default=0.0)
    # operating_profit = sales - expense
    #opm_perc = op/sales * 100
    other_income = models.FloatField(default=0.0)
    interest = models.FloatField(default=0.0)
    deprication = models.FloatField(default=0.0)
    profit_before_tax = models.FloatField(default=0.0)
    tax_percent = models.FloatField(default=0.0)
    # net_profit = pbt - tax%
    # eps = net_profit/(mar_cap/curr_value)
    # roi = net_profit/100
    # pe = curr_value/eps
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
