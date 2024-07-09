from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
# for class defin 
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from first_app import models


# Create your views here.

class IndexView(ListView):
    context_object_name ='musicians_list'  # it will be the name of the list in the template
    model = models.Musician
    template_name = 'first_app/index.html'


class MusicianDetails(DetailView):
    context_object_name ='musician'  # it will be the name of the object in the template
    model = models.Musician
    template_name = 'first_app/musician_details.html'


class AddMusician(CreateView):
    fields = ('first_name', 'last_name','instrument') 
    model = models.Musician
    template_name = 'first_app/musician_form.html'





# Class based views
# def index_test(request):
#     return render(request, 'template', context={})



# inherit the view class
# class IndexView(TemplateView):
#     template_name = 'first_app/index.html'

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context['sample_text_1'] = "Hay i am Number ONE!"
#         context['sample_text_2'] = "Hay i am Number TWO!"
#         return context



# class IndexView(View):
    # class er vitor function define korle self lekha lage.
    # def get(self, request):
    #     return HttpResponse("Hello,  index page!")

