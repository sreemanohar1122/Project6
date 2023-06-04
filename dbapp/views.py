from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Reg(View):
    def post(self,request):
        fn=request.POST["t1"]
        ln=request.POST["t2"]
        un=request.POST["t3"]
        pwd=request.POST["t4"]
        cpwd=request.POST["t5"]
        mobno=request.POST["t6"]
        email=request.POST["t7"]
        return HttpResponse("Registration Success")





# Create your views here.
