from django.shortcuts import render
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("<h1>This is my music App</h1>")


def index(request):
    return render(request,'music/index.html')

def picture(request):
    return render(request,'music/Pictures.html')
def link(request):
    return render(request,'music/Link.html')
def about(request):
    return render(request,'music/About.html')

