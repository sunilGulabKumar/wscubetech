from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersform


def homepage(request):
    data={
        'value':2,
        'f':[10,20,30,40],
        's':[10,30,40,50],
        'v':'''welcom to wscubetech'''
    }     
    return render(request,"index.html")

def submitform(request):
    try:
        if request.method=="POST":
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
           
            #return HttpResponseRedirect(url)
            return HttpResponse(finalans)
    except:
        pass 
        
        return redirect(request,"userform.html")
    


def aboutUS(request):
    if request.method=='GET':
        output=request.GET.get('output')
    return render(request,"aboutus.html",{'output':output})
    
def service(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")

def gallery(request):
    return render(request,"gallery.html")

def fact_us(request):
    return render(request,"fact.html")

def pageus(request):
    return render(request,"page.html")

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n1
    except:
        c="Invalid opr ....."
    print(c)
    return render(request,"calculator.html",{'c':c})
 
def userform(request):
    finalans=0
    fu=usersform()
    data={'form':fu}
    try:
        if request.method=="POST":
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'form':fu,
                'output':finalans
            }
            url="/contant/?output={}".format(finalans)

            return HttpResponseRedirect(url)
            #return redirect(url)
    except:
        pass
    return render(request,"userform.html",data)

def generic(request):
    return render(request,"generic.html")

def elements(request):
    return render(request,"elements.html")

def employeeforms(request):
    return render(request,"forms.html")