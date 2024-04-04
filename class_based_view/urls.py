from django.contrib import admin
from django.urls import path, include
from class_based_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('class_based_app.urls')),
    
    ]
