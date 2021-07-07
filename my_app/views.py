from django.shortcuts import render
from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = 'menu.html'

# def menu(request):
#     return render(request, 'menu.html')
