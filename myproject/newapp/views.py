from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Registration

class RegistrationCreate(CreateView):
    model = Registration
    fields = ['fname', 'lname', 'city', "email"]
    success_url = 'create'
class RegistrationList(ListView):
    model = Registration
    fields = ['fname', 'lname', 'city', "email"]
    success_url = 'list'
class RegistrationDetail(DetailView):
    model = Registration
    fields = ['fname', 'lname', 'city', "email"]
    success_url = 'detail'
class RegistrationUpdate(UpdateView):
    model = Registration
    fields = ['fname', 'lname', 'city', "email"]
    success_url = '/list'

class RegistrationDelete(DeleteView):
    model = Registration
    success_url = '/list'

# Create your views here.
def index(request):
    return HttpResponse("inside")
