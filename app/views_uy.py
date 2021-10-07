from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.forms import RsamForm
from app.models import Uylar, Tumanlar, UserData, Rasmlar
from app.serializers import UySerializers

@api_view(['GET'])
def Search_products(request):
    # try:
    data = request.GET.get("data")
    if data is None:
        return JsonResponse({'status': 500})
    products = Uylar.objects.all()
    a = []
    for i in products:
        if (str(i.xona_soni)+str(i.narx)).lower().find(data.lower()) != -1:
            a.append(i)
    serial = UySerializers(a, many=True)
    # except:
    #     return redirect('app:home')
    return Response(serial.data)
class Instruction(View):
    def get(self,request):
        return render(request,"contact.html")
    def post(self,request):
        pass
