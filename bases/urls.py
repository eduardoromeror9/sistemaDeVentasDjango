from django.contrib import admin
from django.urls.conf import path
from bases.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
