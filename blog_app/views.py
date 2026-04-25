from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
def blog_list (requests):
    templates = loader.get_template("blog_list.html")
    return HttpResponse(templates.render())
@ensure_csrf_cookie
def create_blog (requests):
    templates = loader.get_template("create_blog.html")
    return HttpResponse(templates.render())

def create_blog_action(requests):
    print(requests.POST)
    templates = loader.get_template("blog_list.html")
    return HttpResponse(templates.render())