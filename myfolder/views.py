import datetime

from django.shortcuts import render
from myfolder.models import Portfolio,Services,Team,Contact,Subscribe


# Create your views here.
def index(requst):
    if 'subscribe' in requst.POST:
        gmail = requst.POST.get('subscribe')
        Subscribe(Email=gmail).save()
    elif requst.method == "POST":
        name = requst.POST.get('name')
        email = requst.POST.get('email')
        subject = requst.POST.get('subject')
        text = requst.POST.get('message')
        date = datetime.datetime.now()
        Contact(Ism=name,email=email,subject=subject,matn=text,created_at=date).save()
    our_work = Portfolio.objects.all()
    our_works = Services.objects.all()
    our_work_Team = Team.objects.all()
    context = {
        "works": our_work,
        "services": our_works,
        "team": our_work_Team,
    }
    return render(requst, 'index.html', context)


def portfolio(requst):
    return render(requst, 'portfolio-details.html')






