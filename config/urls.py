"""gamestone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("", include("homepage.urls")),
    path("admin/", admin.site.urls),
    path("gamestone/", include("gamestone.urls")),
    path("accounts/", include("open_id.urls")),
    path("skyrim-helper/", include("skyrim_helper.urls")),
    path("resource-tracker/", include("resource_tracker.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(), name="redoc"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(), name="swagger"),
    path('__debug__/', include('debug_toolbar.urls')),
]
