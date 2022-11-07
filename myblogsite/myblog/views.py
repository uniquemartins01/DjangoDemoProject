import re
from django.shortcuts import render
from django.template import context

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def reversed_prg(request):
    if request.method=="POST":
        get_input=request.POST.get('inp')
        print(get_input)
        output=get_input[::-1]
        print(output)
        context={"get_input":get_input,"output":output}


    return render(request,'about.html',context)