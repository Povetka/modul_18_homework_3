from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def homepage(request):
    return render(request, 'for_task2_f.html')


class HomePage(TemplateView):
    template_name = 'for_task2_c.html'
