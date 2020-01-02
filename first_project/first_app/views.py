from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Destination
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from rest_framework import generics
from .serializers import DRFDestinationSerializer



# Create your views here.

def index(request):
    return render(request, "hello.html")

def post_test(request):
    return render(request, "hello_post.html")

def add(request):
    return render(request, "result.html", {'result': request.GET['num1'] + request.GET['num2']})

def add_post(request):
    return render(request, "result.html", {'result': request.POST['num1'] + request.POST['num2']})

def static_test(request):
    dests = models.Destination.objects.all()
    return render(request, "travello_index.html", { 'dests': dests})

class DestinationList(ListView):
    model = models.Destination

class DestinationDetail(DetailView):
    model = models.Destination

class DestinationCreate(CreateView):
    model = models.Destination
    fields = ['name', 'desc', 'price']
    success_url = reverse_lazy('destination_list')

class DestinationUpdate(UpdateView):
    model = models.Destination
    fields = ['name', 'desc']
    success_url = reverse_lazy('destination_list')

class DestinationDelete(DeleteView):
    model = models.Destination
    fields = ['name', 'desc']
    success_url = reverse_lazy('destination_list')

class DestinationForm(ModelForm):
    class Meta:
        model = models.Destination
        fields = ['name', 'desc']

def Destination_list(request, template_name='first_app/destination_list.html'):
    Destination = models.Destination.objects.all()
    data = {}
    data['object_list'] = Destination
    return render(request, template_name, data)

def Destination_create(request, template_name='first_app/destination_form.html'):
    form = DestinationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('destination_list1')
    return render(request, template_name, {'form':form})

def Destination_update(request, pk, template_name='first_app/destination_form.html'):
    Destination= get_object_or_404(models.Destination, pk=pk)
    form = DestinationForm(request.POST or None, instance=Destination)
    if form.is_valid():
        form.save()
        return redirect('destination_list1')
    return render(request, template_name, {'form':form})

def Destination_delete(request, pk, template_name='first_app/destination_confirm_delete.html'):
    Destination= get_object_or_404(models.Destination, pk=pk)
    if request.method=='POST':
        Destination.delete()
        return redirect('destination_list1')
    return render(request, template_name, {'object':Destination})


#DataFlair #Custom_Validator
def check_size(value):
  if len(value) < 6:
    raise forms.ValidationError("the Password is too short")

#DataFlair #Form
class SignUp(forms.Form):
    first_name = forms.CharField(initial = 'First Name', )
    last_name = forms.CharField(required = False)
    email = forms.EmailField(help_text = 'write your email', required = False)
    Address = forms.CharField(required = False, )
    Technology = forms.CharField(initial = 'Django', disabled = True)
    age = forms.IntegerField(required = False, )
    password = forms.CharField(widget = forms.PasswordInput, validators = [check_size, ])
    re_password = forms.CharField(widget = forms.PasswordInput, required = False)
    #Validation #DataFlair
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password

#DataFlair #Form #View Functions
#DataFlair #Form #View Functions
def regform(request):
    form = SignUp()
    if request.method == 'POST':
        form = SignUp(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html = html + "The Form is Valid"
    else:
        html = 'welcome for first time'
    return render(request, 'signup.html', {'html': html, 'form': form})

class API_objects(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DRFDestinationSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DRFDestinationSerializer