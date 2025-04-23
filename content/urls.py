"""
URL configuration for content project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from ngo import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('base/', views.base, name='base'),
    path('', views.body, name='dashboard'),
    path('extra', views.extra, name='extra'),
    path('story', views.story, name='story'),
    path('partner', views.partner, name='partner'),
    path('story_details/<int:id>/', views.story_details, name='story_details'),
    path("donate/", views.donate, name="donate"),
    path('ujjwal/',views.ujjwal),
    path('shiksha/',views.shiksha),
    path('fly/',views.fly),
    path('volenteer/',views.volenteer),
    path('volunteer_form/', views.volunteer_form, name="volunteer_form"),
    path("submit-volunteer-form/", views.submit_volunteer_form, name="submit_volunteer_form"),

] 



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 