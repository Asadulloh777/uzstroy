from django.shortcuts import render
from myfiles.models import Loyiha, Murojat, Obuna


# Create your views here.

def index(matn):
    if matn.method == "POST":
       name = matn.POST.get('name')
       pochta = matn.POST.get('pochta')
       Obuna(name=name, pochta=pochta).save()
    pro = Loyiha.objects.all().order_by('-id')[0:2]
    return render(matn, 'index.html',{'pro': pro})
def about(matn):
    if matn.method == "POST":
       name = matn.POST.get('name')
       pochta = matn.POST.get('pochta')
       Obuna(name=name, pochta=pochta).save()
    return render(matn, 'about.html')
def blog(matn):
    if matn.method == "POST":
       name = matn.POST.get('name')
       pochta = matn.POST.get('pochta')
       Obuna(name=name, pochta=pochta).save()
    return render(matn, 'blog.html')
def contact(matn):
    if matn.method == "POST":
       ism1 = matn.POST.get('ism1')
       pochta = matn.POST.get('pochta')
       Obuna(ism1=ism1, pochta=pochta).save()

    if matn.method == "POST":
        ism = matn.POST.get('ism')
        fam = matn.POST.get('fam')
        mail = matn.POST.get('mail')
        text = matn.POST.get('text')
        vaqt = matn.POST.get('vaqt')
        Murojat(ism=ism,fam=fam,mail=mail,text=text,vaqt=vaqt).save()
    return render(matn, 'contact.html')
def main(matn):
    if matn.method == "POST":
       name = matn.POST.get('name')
       pochta = matn.POST.get('pochta')
       Obuna(name=name, pochta=pochta).save()
    return render(matn, 'main.html')
def project(matn):
    if matn.method == "POST":
       name = matn.POST.get('name')
       pochta = matn.POST.get('pochta')
       Obuna(name=name, pochta=pochta).save()
    pro = Loyiha.objects.all().order_by('-id')
    return render(matn, 'project.html', {'pro': pro})

def services(matn):
    if matn.method == "POST":
       name = matn.POST.get('name')
       pochta = matn.POST.get('pochta')
       Obuna(name=name, pochta=pochta).save()
    return render(matn, 'services.html')
def single(matn):
    if matn.method == "POST":
       name = matn.POST.get('name')
       pochta = matn.POST.get('pochta')
       Obuna(name=name, pochta=pochta).save()
    return render(matn, 'single.html')