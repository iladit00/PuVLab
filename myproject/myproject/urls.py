"""
URL configuration for myproject project.

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
from django.urls import path, re_path
from myapp.views import hello_world
from myapp.views import hello
from .swagger import schema_view
from myapp.views import get_item_by_name, update_item, delete_item, get_all_items, add_item

urlpatterns = [
    path('', hello),
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/shopping/<str:name>/', get_item_by_name, name='get_item_by_name'),
    path('api/shopping/<str:name>/update', update_item, name='update_item'),
    path('api/shopping/<str:name>/delete', delete_item, name='delete_item'),
    path('api/shopping/', get_all_items, name='get_all_items'),
    path('api/shopping/create', add_item, name='add_item'),
]
