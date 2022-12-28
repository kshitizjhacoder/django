
from .forms import PersonalFrom
from .models import Personal, Train
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

# Create your views here.


def details(request, id):
    if request.method == 'POST':
        searched = (request.POST['pnr_no'])
        id = request.POST['classs_id']
        # src = request.POST['src']
        # dest = request.POST['dest']
        # dat = request.POST['dat']
        # forged = f'Train object({searched})'
        # train object has been searched
        t_name = Train.objects.filter(PNR__contains=searched)
        # t_times = Times.objects.filter(Source__contains=id)

        # related train and there timing will be searched

        # t_times = Times.objects.filter(class_id__contains=id)
        # t_pn = Times.PNR_NO
        # for t in t_name:
        #     tn = t.name_of_train
        #     tc = t.no_of_coach
        # for t in t_times:
        #     # if t.PNR_NO == searched:
        #     t_pn = t.PNR_NO
        #     ts = t.Source
        #     td = t.Destination
        # fog = Times.objects.filter(t_pn__contains=searched)
        return render(request, 'details.html', {})
    else:
        return render(request, 'details.html', {})


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account"
    message = render_to_string('message_to_email.html', {
        'user': user.name,
        # 'domain': get_current_site(request).domain,
        # 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        # 'token': account_activate_token.make_token(user),
        # 'protocol': https if request.is_secure() else http
    })
    email = EmailMessage(mail_subject, message, to={to_email})
    if email.send():
        messages.success(request, 'the mail has been sent')
    else:
        messages.error(request, 'please check your data')


def home(request):
    return render(request, 'index.html', {})


def signup(request):
    if request.method == "POST":
        form = PersonalFrom(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_activate = False
            user.save()
            # form.save()
            name = request.POST['name']
            email = request.POST['email']
            messages.success(
                request, f'NEW ACCOUNT CREATED WE HAVE SEND THE MAIL FOR CONFIRMATION THANK YOU : {name} and your mail is {email}')
            activateEmail(request, user, email)
            return redirect('home')
    else:
        return render(request, 'signup.html', {})


def signin(request):
    if request.method == 'POST':
        # data = form.cleaned_data
        email = request.POST['email']
        password = request.POST['password']
        obj = Personal.objects.filter(
            email=email, password=password)
        for ob in obj:
            em = ob.email
        user = authenticate(request, email=em)
        if user is not None:
            # print(obj.email)
            # if user.is_active:
            #     login(request, user)
            #     return redirect('home', request)
            return redirect('home')

        return HttpResponse('<h1>invalid Data</h1>')
    else:
        return render(request, 'signin.html', {})


def signout(request):
    logout(request)
    return redirect('home')


def pnrsearch(request):
    if request.method == 'POST':
        searched = (request.POST['pnr_no'])
        id = request.POST['classs_id']
        t_name = Train.objects.filter(PNR__contains=searched)
    #     t_times = Times.objects.filter(PNR_NO__contains=searched)
        for t in t_name:
            tn = t.name_of_train
            tc = t.no_of_coach
            t_pn = t.PNR
            ts = t.Source
            td = t.Destination
        return render(request, 'pnrsearch.html', {'searched': searched,
                                                  't_name': tn, 't_coach': tc, 't_pn': t_pn, 't_src': ts, 't_dest': td})
    else:
        return render(request, 'pnrsearch.html', {})


def timesearch(request):
    if request.method == 'POST':
        src = request.POST['src']
        dest = request.POST['dest']
        t_times = Train.objects.filter(
            Source__contains=src, Destination__contains=dest)
        return render(request, 'timesearch.html', {'tt': t_times})
    return render(request, 'timesearch.html', {})

# post = Personal()
    # post.email = request.POST.get("email")
    # post.password = request.POST.get("password")
    # post.name = request.POST.get("Name")
    # post.phone = request.POST.get("phn")
    # post.street = request.POST.get("addr")
    # post.city = request.POST.get("City")
    # post.sex = request.POST.get("gender")
    # post.bday = request.POST.get("day")
    # post.bmonth = request.POST.get("month")
    # post.byear = request.POST.get("year")
