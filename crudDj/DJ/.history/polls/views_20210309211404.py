from django.shortcuts import render , HttpResponseRedirect
# from django.http import HttpResponse
from .forms  import DjCrud
from .models import User
# Create your views here.
def index(request):
  return render(request, 'polls/starter.html')

#adding and retrieving data

def add_show(request):
  if request.method == 'POST': 
    fm = DjCrud(request.POST)
    if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      pw = fm.cleaned_data['password']
      reg= User(name=nm, email=em, password=pw)
      reg.save()
      fm = DjCrud()
  else:
      fm = DjCrud()
      Dj = User.objects.all()
      return render(request, 'polls/add.html', {'form':fm})
    
 #delete function
 
 def update_data(request,id) : 
   if request.method == 'POST':
     pi = User.objects.get(pk=id) 
     fm = DjCrud(instance=pi)
 return render(request, 'polls/update.html', {'form':fm})    