from django.shortcuts import render
from django.views.generic import View
from django.views.generic import View
from django.views.generic import View

# Create your views here.

class helloworldview(View):
    def get(self,request,*args,**kwargs):

        return render(request,'hello_world.html')
    
    
    
class GoodMorning(View):
    def get(self,request,*args,**kwargs):

        return render(request,'Good_Morning.html')
    

    
class FeedBackView(View):


    def get(self,request,*args,**kwargs):
        
        return render(request,"feedback.html")
    
    
    def post(self,request,*args,**kwargs):
        print("inside post method=====")

        mail=request.POST.get("email")
        message=request.POST.get("message")

        print(mail)
        print(message)
        return render(request,"feedback.html")

        

