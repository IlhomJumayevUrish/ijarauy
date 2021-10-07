from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from app.models import Uylar, Tumanlar, UserData, Rasmlar
from django.contrib import messages
from django.urls import reverse,reverse_lazy


def home(request):

    uylar=Uylar.objects.all()
    tumanlar=Tumanlar.objects.all()
    return render(request, 'home.html',context={"uylar":uylar,"tuman":tumanlar})
def detail(request,pk):
    uy=Uylar.objects.get(id=pk)
    return render(request, 'detail.html', context={"uy": uy})


class Uy_index(View):
    def get(self, request, pk):
        xona = Tumanlar.objects.get(id=pk).tumanda.all()
        name=Tumanlar.objects.get(id=pk).name
        tumanlar = Tumanlar.objects.all()
        return render(request, 'index.html', context={"xona": xona,"name":name,"tuman":tumanlar})

class UserD(View):
    def get(self, request):
        return render(request, 'sign-in.html')
    def post(self, request):
        username = request.POST["tel"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("app:home")
        else:
            messages.add_message(request, messages.SUCCESS, "Name yoki password xato!")
            return render(request, "sign-in.html")

class RegistrationUser(View):
    def get(self, request):
        return render(request, 'registration.html')
    def post(self, request):
        userda=request.POST
        if str(userda["password1"])==str(userda["password2"]):
            try:
                user = User.objects.create_user(username=userda["tel"] ,email=userda["email"] ,password= userda["password1"])
                UserData.objects.create(user=user,name=userda["name"],phone=userda["tel"])
                messages.add_message(request, messages.SUCCESS, "Tabrik siz ro'yxatdan o'tdingiz iltimos telefon va parolni terib saytga kiring!")
                return render(request, 'registration.html')
            except:
                messages.add_message(request, messages.SUCCESS, "Siz tanlagan login band yoki bu telefon raqam orqali ro'yxatdan o'tilgan ekan iltimos boshqa login tanlang!")
                return render(request, 'registration.html')
        else:
            messages.add_message(request, messages.SUCCESS, "Parollar mos kelmadi!")
            return render(request, 'registration.html')
def wrapper(request):
    tumanlar=Tumanlar.objects.all()
    return render(request, 'wrapper.html',context={"tuman":tumanlar})
def cat(request):
    return render(request, 'category.html')
class MyAccount(View):
    def get(self, request):
        tumanlar = Tumanlar.objects.all()
        return render(request, 'my-wishlist.html',context={"tuman":tumanlar})
    def post(self, request):
        tuman=Tumanlar.objects.get(id=request.POST["tuman"])
        try:
            uylar=Uylar.objects.create(manzil=request.POST["manzil"], turi=request.POST["turi"], kimga=request.POST["kimga"], remont=request.POST["remont"], qoshimchamalumot=request.POST["qoshimchamalumot"], qoshimchajxozlar=request.POST["text"], user=request.user.userlar, tumanda=tuman, xona_soni=request.POST["soni"], narx=request.POST["narx"], aloqa=request.POST["tel"])
            for i in request.FILES.getlist('files'):
                Rasmlar.objects.create(uy=uylar,image=i)
            messages.add_message(request, messages.SUCCESS, "E'lon yuklandi saytdan ko'ring!")
        except:
            messages.add_message(request, messages.SUCCESS, "E'lon yuklanmadi iltimos qaytadan yuklang!")
        return redirect('app:myaccount')

def uydelete(request,pk):
    Uylar.objects.get(id=pk).delete()
    return redirect('app:myaccount')
def logouts(request):
    logout(request)
    return redirect('app:home')