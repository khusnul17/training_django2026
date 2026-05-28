from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import BlogForm
from .models import Blogs, Transaksi
from django.contrib import messages
from django.shortcuts import redirect
from .serializers import BlogSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def blog_list (request):
    data = Blogs.objects.all()
    print(data)
    templates = loader.get_template("blog_list.html")
    return HttpResponse(templates.render({'data':data}, request))
@ensure_csrf_cookie
def create_blog (request):
    form = BlogForm()
    return render(request, "create_blog.html", {'form':form})

def create_blog_action(request):
    print(request.POST)
    forms = BlogForm(request.POST)
    if forms.is_valid():
        forms.save()
    else:
        messages.error(request, 'data is not valid')
        return redirect('/create-blog')
    templates = loader.get_template("blog_list.html")
    return HttpResponse(templates.render())

def edit_blog (request,id):
    blog = get_object_or_404(Blogs,pk=id)
    form = BlogForm(instance=blog)
    return render(request, "edit_blog.html", {'form':form})

def edit_blog_action(request,id):
    print(request.POST)
    forms = BlogForm(request.POST, instance=get_object_or_404(Blogs,pk=id))
    if forms.is_valid():
        forms.save()
    else:
        messages.error(request, 'data is not valid')
        return redirect('/edit-blog')
    return redirect('/blogs')

class BlogViewSet(APIView):
    def get(self, request):
    
        queryset = Blogs.objects.all()

        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)  
#from django.core.serializers.json import DjangoJSONEncoder
#import json

def get_dashboard(request):
    # Agregasi data penjualan per bulan
    #from django.db.models.functions import TruncMonth
    #from django.db.models import Sum
    
    penjualan = (
        Transaksi.objects
        .annotate(bulan=TruncMonth('tanggal'))
        .values('bulan')
        .annotate(total=Sum('jumlah'))
        .order_by('bulan')
    )
    
    labels = [p['bulan'].strftime('%b %Y') for p in penjualan]
    data = [float(p['total']) for p in penjualan]
    
    context = {
        'labels': json.dumps(labels, cls=DjangoJSONEncoder),
        'data': json.dumps(data),
    }
    return render(request, 'dashboard.html', context)
def register(request):
    if request.method=='GET':
        form = UserCreationForm()
        context = {'form':form}
        return render(request, 'register.html', context)
    data = {'username':request.POST['username'], 'password':request.POST['password1']}
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        print(request.POST)
        print(form.errors)
        messages.error(request, 'data is not valid')
        return redirect('/register')
    
