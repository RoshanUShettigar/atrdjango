from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy



class IndexView(generic.ListView):
    pass

class CreatData(generic.CreateView):
    pass
