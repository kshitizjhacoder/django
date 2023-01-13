from django.shortcuts import render
from .models import Stock, Promotor_holding, Price, PNL
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def stockvalue(request):
    if request.method == "POST":
        sch = request.POST['search']
        s_list = []
        s_marketcapital = []
        s_pe = []
        s_currentvalue = []
        s_divyeild = []
        s_np = []
        s_sales = []
        s_roce = []
        S_stock = Stock.objects.filter(stock_sname=sch)
        for s in S_stock:
            sid = s.stock_id
            sname = s.stock_name
            sabout = s.about
            sector_name = s.sector_name
        S_price = Price.objects.filter(stock=sid)
        S_prom = Promotor_holding.objects.filter(promotor_holding_id=sid)
        S_pnl = PNL.objects.filter(stock=sid)
        querry = Stock.objects.filter(sector_name=sector_name)
        print(querry)
        for s in querry:
            col = []
            temp_stock = Stock.objects.filter(stock_id=s.stock_id)
            print(temp_stock)
            for t in temp_stock:
                col.append(t.stock_sname)
            temp_stock = Price.objects.filter(stock_id=s.stock_id)
            print(temp_stock)
            for t in temp_stock:
                col.append(t.mark_cap)
                col.append(t.curr_value)
                col.append(t.dividend)
            temp_stock = PNL.objects.filter(
                stock_id=s.stock_id, quaterly='dec 2022')
            print(temp_stock)
            for t in temp_stock:
                col.append(t.sales)
            s_list.append(col)
            print(col, s_list)

    return render(request, 'stockvalue.html', {'sabout': sabout, 'sname': sname, 'S_price': S_price,
                                               'S_prom': S_prom, 'S_pnl': S_pnl, 'S_list': s_list})
