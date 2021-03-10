from django.shortcuts import render , HttpResponseRedirect
# from django.http import HttpResponse
from .forms  import StudentRegistration
from .models import User
# Create your views here.
def index(request):
  return render(request, 'polls/starter.html')