# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")), 
    path("", include("app.urls")), 
    path('api/accounts/',include('accounts_api.urls')),
    path('api/', include('api.urls')),
]
