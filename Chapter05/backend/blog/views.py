from django.http import HttpResponse
from rest_framework import views
from rest_framework import response
from rest_framework import generics
from rest_framework import status
from rest_framework import filters

from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog import models
from blog import serializers as serializer

# Create your views here.


class BlogGetCreateView(views.APIView):
    def get(self, request):
        blogs_obj_list = models.Blog.objects.all()
        blogs = serializer.BlogSerializer(blogs_obj_list, many=True)
        return response.Response(blogs.data)

    def post(self, request):
        input_data = request.data
        b_obj = serializer.BlogSerializer(data=input_data)
        if b_obj.is_valid():
            b_obj.save()
            return response.Response(b_obj.data, status=status.HTTP_201_CREATED)
        return response.Response(b_obj.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogGetUpdateView(generics.ListCreateAPIView):
    serializer_class = serializer.BlogSerializer

    def get_queryset(self):
        blogs_queryset = models.Blog.objects.filter(id__gt=1)
        return blogs_queryset


class BlogGetUpdateFilterView(generics.ListAPIView):
    serializer_class = serializer.BlogSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["title"]


# ============================================================================ #


def update_blog_title(request):
    blog_id = request.GET.get("id")
    blog = models.Blog.objects.get(id=blog_id)
    if request.user.has_perm("blog.update_title"):
        # perform operation
        return HttpResponse("User has permission to update title")
    return HttpResponse("User does not have permission to update title")


def check_permission(user, group_name):
    return user.groups.filter(name=group_name).exists()


@api_view(["POST"])
def blog_view(request):
    if not check_permission(request.user, "can_view_blog"):
        return Response(status=403)
    print("User has permission to view blog")
    return Response(status=200)
