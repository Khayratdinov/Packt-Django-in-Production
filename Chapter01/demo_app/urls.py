from django.urls import path
from demo_app import views


urlpatterns = [
    path("hello-world/", views.hello_world),
    path("hello-world-drf/", views.hello_world_drf),
    # ============================================================================ #
    path("demo-version/", views.demo_version),
    path("custom-version/", views.DemoView.as_view()),
    path("another-custom-version/", views.AnotherView.as_view()),
    # ============================================================================ #
    path("hello-world-functional-view/", views.hello_world_functional_view),
    path("apiview-class/", views.DemoAPIView.as_view()),
]
