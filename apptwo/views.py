from django.shortcuts import render
# from apptwo.models import user
from apptwo.form import newuser
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    form = newuser()

    if request.method  == "POST":
        form = newuser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'apptwo/user.html',{'form':form})
    