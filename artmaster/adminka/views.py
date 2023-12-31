from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
# Create your views here.
Art = []
Frames = []
Thing = []


def userLogin(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['login'], password=request.POST['password'])
        
        if user is not None:
            login(request,user)
            global a
            a = request.POST['login']
            return redirect('/admin/')

        return render (request, 'autor.html', {'error' : "Nepravilniy daniy"})
    else:
        return render(request, 'autor.html')

@login_required(login_url="/admin/authorization")
def menyu(request):
    return render(request, "menyu.html")

@login_required(login_url="/admin/authorization")
def userLogout(request):
    logout(request)
    return redirect("/admin/authorization")

@login_required(login_url="/admin/authorization")
def listframe(request):
    # data = {
    #     "frames": Frames.objects.all().order_by('-id')
    # }
    return render(request, 'listframe.html')

@login_required(login_url="/admin/authorization")
def listart(request):
    data = {
        "frames": Frames.objects.all().order_by('-id')
    }
    return render(request, 'listart.html', data)

@login_required(login_url="/admin/authorization")
def listsomething(request):
    data = {
        "frames": Frames.objects.all().order_by('-id')
    }
    return render(request, 'listsomething.html',  data)

@login_required(login_url="/admin/authorization")
def addart(request):
    data = {
        "input1": 'nomi',
        "input2": 'turi',
        "input3": 'sana',
        "input4": 'nomi',
    }
    if request.method == 'POST':
        art = Art()
        art.name = request.POST["input1"]
        art.type = request.POST["input2"]
        art.soni = request.POST["input3"]
        art.collor = request.POST["input4"]
        art.data

        fs = FileSystemStorage()
        image =  request.FILES['imageUrl']

        fs.save(image.name, image)
        art.photo = fs.url(image)
        art.save() 
        return HttpResponseRedirect('/admin/listart/')
    return render(request, 'add.html', data)

@login_required(login_url="/admin/authorization")
def addframe(request):
    data = {
        "input1": 'nomi',
        "input2": 'turi',
        "input3": 'soni',
        "input4": 'nom',
    }
    if request.method == 'POST':
        frame = Frames()
        frame.name = request.POST["input1"]
        frame.type = request.POST["input2"]
        frame.soni = request.POST["input3"]
        frame.collor = request.POST["input4"]
        frame.data

        fs = FileSystemStorage()
        image =  request.FILES['imageUrl']

        fs.save(image.name, image)
        frame.photo = fs.url(image)
        frame.save() 
        return HttpResponseRedirect('/admin/listart/')
    return render(request, 'add.html', data)


@login_required(login_url="/admin/authorization")
def addsomething(request):
    data = {
        "input1": 'name',
        "input2": 'type',
        "input3": 'soni',
        "input4": 'collor',
    }
    if request.method == 'POST':
        thing = Thing()
        thing.name = request.POST["input1"]
        thing.type = request.POST["input2"]
        thing.soni = request.POST["input3"]
        thing.collor = request.POST["input4"]
        thing.data
        
        fs = FileSystemStorage()
        image =  request.FILES['imageUrl']

        fs.save(image.name, image)
        thing.photo = fs.url(image)
        thing.save() 
        return HttpResponseRedirect('/admin/listart/')
    return render(request, 'add.html', data)