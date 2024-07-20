# mock/views.py

import requests
from django.shortcuts import render
from .forms import LoginForm

def index(request):
    iframe_url = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userId = form.cleaned_data['userId']
            cic = form.cleaned_data['cic']
            api_url = 'http://localhost:3000/api/ledgerInquiry/login'
            data = {'userId': userId, 'cic': cic}
            response = requests.post(api_url, data=data)
            if response.status_code == 200:
                iframe_url = response.url
    else:
        form = LoginForm()
    
    return render(request, 'mock/index.html', {'form': form, 'iframe_url': iframe_url})

def iframe(request):
    iframe_url = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userId = form.cleaned_data['userId']
            cic = form.cleaned_data['cic']
            api_url = 'http://localhost:3000/api/ledgerInquiry/login'
            data = {'userId': userId, 'cic': cic}
            response = requests.post(api_url, data=data)
            if response.status_code == 200:
                iframe_url = response.url
    else:
        form = LoginForm()
    
    return render(request, 'mock/iframe.html', {'form': form, 'iframe_url': iframe_url})

def new_tab_post_view(request):
    form = LoginForm()
    return render(request, 'mock/new_tab_post.html', {'form': form})

def new_tab_get_view(request):
    form = LoginForm()
    return render(request, 'mock/new_tab_get.html', {'form': form})

def new_tab_test_view(request):
    form = LoginForm()
    return render(request, 'mock/new_tab_test.html', {'form': form})

def token_test_view(request):
    form = LoginForm()
    return render(request, 'mock/token_test.html', {'form': form})
