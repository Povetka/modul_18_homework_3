from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'hp.html'


class Shop(TemplateView):
    template_name = 'shp.html'

    def get(self, request):
        games = [
            {"name": "Atomic Heart"},
            {"name": "Cyberpunk 2077"},
            {"name": "Psychonauts 2"},
        ]
        return render(request, self.template_name, {'games': games})


class Basket(TemplateView):
    template_name = 'basket.html'

    def get(self, request):
        shopping_list = []
        context = {
            'shopping_list': shopping_list,
        }
        return render(request, self.template_name, context)
