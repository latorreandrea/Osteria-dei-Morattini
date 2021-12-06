from django.shortcuts import render

# Create your views here.
def index(request):
    #redirect to index view
    return render(request, 'index.html')