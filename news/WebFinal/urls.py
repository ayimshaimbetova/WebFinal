from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')), 
    path("articles/", include("articles.urls")), 
    path("", include("pages.urls")), 
    path("apis/", include("apis.urls")),
    path("api-auth/", include("rest_framework.urls")), 
]
