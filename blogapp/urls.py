"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as users_views
from notes import views as notes_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogapp/user/',users_views.register_API.as_view(),name="register"),
    path('blogapp/user/auth/', users_views.login_API.as_view(), name="login"),
    path('blogapp/sites/list/',notes_views.ListAPI.as_view(), name="list"),
    path('blogapp/sites/addnote/',notes_views.Save_Note.as_view(), name="save")
]
