"""
URL configuration for phone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from sales import views as v1

urlpatterns = [
    path('', v1.home, name='home'),
    path('admin/', admin.site.urls),
    path('hello/', v1.welcome, name='welcome'),
    path('showphone/<str:phone>/', v1.showphone, name='showphone'),
    path('article/',v1.article, name='article'),
    path('mydashboard/', v1.mydashboard),
    path('productt/',v1.product),
    path('filter/',v1.filter, name='filter'),
    path('create/',v1.create, name='create'),
    path('addproduct/',v1.add_product, name='addproduct'),
    path('deleteitem/<int:id>/',v1.deletitems, name='deleteitem'),
    path('editrecord/<int:id>/',v1.editrecord, name='editrecord'),
]
