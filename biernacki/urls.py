"""biernacki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from store import views as store
from data import views as data

from rest_framework import routers
from store import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'books', store.BookViewSet)

urlpatterns = [
    # dodane na lab 7
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # http://localhost:8000/api/users.json/
    # http://localhost:8000/api/users/

    url(r'^admin/', admin.site.urls),

    # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^$', store.home, name="home"),
    url(r'^store$', store.sklep, name="store"),

    # url(r'^store$', store.store, name="store"),
    # url(r'^store$', data.store, name="store"),

    url(r'^books$', store.books, name="books"),

    url(r'^page$', data.page, name="page"),
    url(r'^data$', data.data, name="data"),
    url(r'^myname$', data.myname, name="myname"),

    # facebook
    url('', include('social.apps.django_app.urls', namespace='social')),
]
