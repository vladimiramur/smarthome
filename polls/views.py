from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader
from .forms import PostForm, RelayForm
import requests


def index(request):
    
    return render(request, 'polls/index.html')


def post_form_upload(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleanded_data['created_at']
            post = m.Post.objects.create(content=content, created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail', kqargs={'post_id': post.id}))

    return render(request, 'polls/post_form_upload.html', {'form': form})

def my_view(request):
    if request.method == 'POST':
        if form.is_valid():
            return HttpResposeRedirect(reverse('polls/index.html'))

    form = RelayForm()
    return render(request, 'polls/quad_relay.html', {})

def my_swich(request):
    r = requests.get("http://amur.info")
    return render(request, 'polls/my_swich.html', {})

