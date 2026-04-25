from django.contrib import admin
from django.urls import path
from blog_app.views import blog_list, create_blog, create_blog_action

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs', blog_list),
    path('create-blog', create_blog),
    path('create-blog-action', create_blog_action)
]