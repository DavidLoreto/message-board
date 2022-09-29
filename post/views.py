from django.views.generic import ListView
from django.shortcuts import render

from post.models import Message

class HomePageView(ListView):
    model = Message
    template_name = 'home.html'
    context_object_name = 'messages_list'
