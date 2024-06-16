from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/',include('author.urls')),
    # path('',views.base),
    path('category/',include('categories.urls')),
    path('post/',include('posts.urls')),
    path('profile/',include('profiles.urls')),
]
