from django.shortcuts import render,redirect
from .models import waiter

# Create your views here.
def showdata(request):

    data = waiter.objects.all()
    return render(request,'show.html',{'data':data})

def deletedata(request,id):
    waiter.objects.get(id=id).delete()
    return redirect(showdata)

def add(request):
    if request.method=="GET":
        return render(request,"form.html")
    else:
        Name=request.POST['name']
        Age=request.POST['age']
        Phone=request.POST['Phone']
        Email=request.POST['Email']
        Address=request.POST['Address']
        data=waiter(name=Name,age=Age,Phone=Phone,Email=Email,Address=Address)
        data.save()
        return render(request,'form.html')
    

def edit(request,id):
    if request.method=="GET": #jive hi edit button click kra ge phla if chlegaa and show karu gaa page
        after=waiter.objects.get(id=id)
        return render(request,"form.html",{"after":after}) 
    else:
        Name=request.POST['name']  #ferr else chlu gaa jive hi appa data add kraa ge
        Age=request.POST['age']
        Phone=request.POST['Phone']
        Email=request.POST['Email']
        Address=request.POST['Address']
        data=waiter(id=id,name=Name,age=Age,Phone=Phone,Email=Email,Address=Address)
        data.save()
        
        return redirect(showdata)
    

    

    
    




    