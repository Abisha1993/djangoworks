from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class AdditionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):
        form_data=request.POST

        num1=form_data.get("num1")#"10"
        num2=form_data.get("num2")#"20"
        result=int(num1)+int(num2)
        print(result)
        data={"output":result
              
        }
        return render(request,"add.html",data)
    


class Bmiview(View):
    def get(self,request,*args,**kwargs):
        form_instance=Bmiview()
        context={
            "form":form_instance

        }
        return render(request,"bmi.html",context)
    
    
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=BmiForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            print(data)

        return render(request,"bmi.html",{"form":form_instance})
    