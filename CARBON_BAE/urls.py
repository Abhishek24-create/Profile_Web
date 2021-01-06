"""CARBON_BAE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from Webapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    # path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
    # name='logout'),
    # path('accounts/', include('allauth.urls')),
    path('register/', views.Registration),
    path('', views.Login_Just),
    path('base/', views.Base, name='base'),
    path('login/', views.Login, name='login'),
    path('saveregister/', views.SaveRegister),
    path('logout/', views.Logout, name='logout'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    # path('google/', views.GoogleView.as_view(), name='google'),  # add path for google authentication
    path('build/',views.Build_Ur_Profile, name='build'),
    path('indho/', views.index, name="home"),
    path('profile/',views.Profile, name='profile')

]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)