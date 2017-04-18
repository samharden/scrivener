

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404




def home_page(request):
    # if this is a POST request we need to process the form data


    return render(request, 'main/home.html')
