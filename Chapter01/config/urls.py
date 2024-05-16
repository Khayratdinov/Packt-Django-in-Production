from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("demo-app/", include("demo_app.urls")),
    path("<version>/demo-app-version/", include("demo_app.urls")),
]
