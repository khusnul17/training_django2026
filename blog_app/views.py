from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
def blog_list (request):
    templates = loader.get_template("blog_list.html")
    return HttpResponse(templates.render())
@ensure_csrf_cookie
def create_blog (request):
    return render(request, "create_blog.html")

def create_blog_action(request):
    print(request.POST)
    templates = loader.get_template("blog_list.html")
    return HttpResponse(templates.render())