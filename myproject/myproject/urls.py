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
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Import views from myapp
from myapp import views

# Swagger/OpenAPI Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="Shopping API",
        default_version='v1',
        description="API documentation for the Shopping app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@shoppingapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
    url='http://localhost:8080',
)

# Define URL patterns
urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # Swagger documentation endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # API endpoints for shopping
    path('api/shopping/', views.get_all_items, name='get_all_items'),
    path('api/shopping/create/', views.add_item, name='add_item'),
    path('api/shopping/<str:name>/', views.get_item_by_name, name='get_item_by_name'),
    path('api/shopping/<str:name>/update/', views.update_item, name='update_item'),
    path('api/shopping/<str:name>/delete/', views.delete_item, name='delete_item'),

    # Example endpoints
    path('', views.hello_world, name='hello_world'),
]
