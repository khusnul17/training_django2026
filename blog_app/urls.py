from django.contrib import admin
from django.urls import path
from blog_app.views import blog_list, create_blog, create_blog_action, edit_blog, edit_blog_action, BlogViewSet, get_dashboard, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs', blog_list),
    path('create-blog', create_blog, name="create_page"),
    path('create-blog-action', create_blog_action),
    path('edit-blog/<int:id>', edit_blog),
    path('edit-blog-action/<int:id>', edit_blog_action),
    path('api/blogs/', BlogViewSet.as_view()),
    path('dashboard', get_dashboard),
    path('register', register),
]
