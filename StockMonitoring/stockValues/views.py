from django.shortcuts import render
from .models import Stock, Promotor_holding, Price, PNL
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def convertstrtoint(s):
    print(s)
    ch = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    st = ''
    for i in s:
        # print(i)
        if i in ch:
            st = st+i
    print(st)
    return int(st)


def stockvalue(request):
    if request.method == "POST":
        sch = request.POST['search']
        s_list = []
        operating_profit = []
        opm = []
        net_profit = []
        eps = []
        stock_pe = []
        # roe = []
        S_stock = Stock.objects.filter(stock_sname=sch)

        for s in S_stock:
            sid = s.stock_id
            sname = s.stock_name
            sabout = s.about
            sector_name = s.sector_name
            temp_stock = PNL.objects.filter(
                stock_id=sid)
            S_price = Price.objects.filter(stock=sid)
            for t in S_price:
                marcap = t.mark_cap
                currvalue = t.curr_value
                marcap = convertstrtoint(marcap)
                print(marcap)
            mark_curr = marcap/currvalue
            print(marcap, currvalue)
            for t in temp_stock:
                operating_profit.append(t.sales - t.expense)
                opm.append(
                    round(float(((t.sales-t.expense)/t.sales) * 100), 2))
                net_profit.append(
                    round(float(t.profit_before_tax-(t.profit_before_tax*t.tax_percent/100)), 2))
                print(net_profit[-1], mark_curr)
                eps.append(
                    round(float((net_profit[-1])/(mark_curr)), 2))
                stock_pe.append(round(float(currvalue/eps[-1]), 2))
        # promotor holding of the company
        S_prom = Promotor_holding.objects.filter(promotor_holding_id=sid)
        # profit and lost of the company
        S_pnl = PNL.objects.filter(stock=sid)
        # sector name peer distribution
        querry = Stock.objects.filter(sector_name=sector_name)
        print(querry)

        for s in querry:
            col = []
            # short name of different  company
            temp_stock = Stock.objects.filter(stock_id=s.stock_id)
            for t in temp_stock:
                col.append(t.stock_sname)
            # market capital,current value of share,dividend yeild of different  company
            temp_stock = Price.objects.filter(stock_id=s.stock_id)
            for t in temp_stock:
                col.append(t.mark_cap)
                col.append(t.curr_value)
                col.append(t.dividend)
            # sales of different  company
            temp_stock = PNL.objects.filter(
                stock_id=s.stock_id, quaterly='dec 2022')
            for t in temp_stock:
                col.append(t.sales)

            s_list.append(col)

    return render(request, 'stockvalue.html', {'sabout': sabout, 'sname': sname, 'S_price': S_price,
                                               'S_prom': S_prom, 'S_pnl': S_pnl, 'S_list': s_list,
                                               'S_operating_profit': operating_profit, 'S_opm': opm,
                                               'S_net_profit': net_profit, 'S_eps': eps,
                                               'S_stock_pe': stock_pe, 'S_init_pe': stock_pe[-1]})
