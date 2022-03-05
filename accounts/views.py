from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    #success_url = reverse_lazy('login')
    success_url = reverse_lazy('libry')
    template_name = 'registration/signUp.html'