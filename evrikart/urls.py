"""evrikart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt import views as jwt_views
from drf_yasg import openapi
from Apps.Auth.views import TokenView
from django.conf import settings
from django.conf.urls.static import static
from Apps.Core import views
from django.conf import settings
from django.conf.urls.static import static
from Apps.Core.views import csv_upload
from .views import check_mail_temp
from Apps.Catalog.Category import urls


schema_view = get_schema_view(
    openapi.Info(
        title="Evrikart API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_urlpatterns = [
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),

    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('Apps.Auth.urls')),
    path('api/token/', TokenView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/catalog/', include('Apps.Catalog.urls', namespace="catalog")),
    path('api/v1/vendor/', include('Apps.Vendors.urls', namespace="vendor")),
    path('api/v1/core/', include('Apps.Core.urls', namespace="core")),
    path('csv_upload/', csv_upload, name="csv_upload"),
    path('check_mail_temp', check_mail_temp, name="check_mail_temp")
]+swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
