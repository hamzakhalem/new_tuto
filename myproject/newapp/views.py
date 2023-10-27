from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Registration
from django.core.mail import send_mail
import json

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
    return render(request, 'newapp/index.html')
def subscribe(request):
    if request.method == "GET":
        return render(request, 'newapp/subscribe.html')
    elif request.method == "POST":
        email = request.POST['email']
        print(email)
        return redirect('index')

def displayEmployee(request):
    emp = {
        'eid' : "2",
        'ename' : "chedjra",
        'ecity' : "alger",
    }
    reuslt = json.dumps(emp)
    return HttpResponse(reuslt, content_type="application/json")

from django.views.generic import View

class JasonClass(View):
    def get(self, request, *args, **kwargs):
         emp = {
                'eid' : "2",
                'ename' : "chedjra",
                'ecity' : "alger",
            }
         return JsonResponse(emp)
    def post(self, request, *args, **kwargs):
        result={
            "msg" : "true"
        }
        return JsonResponse(result)