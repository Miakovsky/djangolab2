from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django import forms
import random

results = ['cats', 'rats']
images_cats = ['cat2', 'cat3', 'cat4', 'cat5']
images_rats = ['rat2',  'rat3', 'rat4', 'rat5']

class NameForm(forms.Form):
    name = forms.CharField(label='')


class IndexView(FormView):
    template_name = 'index.html'
    form_class = NameForm
    #success_url = '/'

    def post(self, request, *args, **kwargs):
        form: NameForm = self.get_form()
        print(form.data)
        print(form.is_valid())
        print(form.cleaned_data)
        print(*kwargs)
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        choice = random.choice(results)
        if choice == 'rats':
            image = random.choice(images_rats)
        else:
            image = random.choice(images_cats)
        self.success_url = reverse(choice, args=[name, image])

        return super().form_valid(form)
    
    

def index(request):
    return render(request, 'base.html')

def cats(request, name, image):
    return render(request, 'cats.html', {'name': name, 'image': image})

def rats(request, name, image):
    return render(request, 'rats.html', {'name': name, 'image': image})