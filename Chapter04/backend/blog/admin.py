from django.contrib import admin
from django.core import paginator
from django.utils.functional import cached_property
from django.contrib.admin.models import LogEntry

from blog import models

# ================================ BLOG ADMIN ================================ #


class BlogAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Blog, BlogAdmin)


# ============================= BLOG CUSTOM ADMIN ============================ #


class BlogCustomAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    show_full_result_count = True
    list_filter = ["title"]
    list_display = ["title", "created_at"]
    date_hierarchy = "created_at"


# admin.site.register(models.Blog, BlogCustomAdmin)


# ============================ BLOG CUSTOM 2 ADMIN =========================== #


class BlogCustom2Admin(admin.ModelAdmin):
    list_display = ("email", "word_count", "id")


# admin.site.register(models.Blog, BlogCustom2Admin)


# ============================ BLOG CUSTOM 3 ADMIN =========================== #


class BlogCustom3Admin(admin.ModelAdmin):
    filter_horizontal = ["tags"]


# admin.site.register(models.Blog, BlogCustom3Admin)

# ============================ BLOG CUSTOM 4 ADMIN =========================== #


class BlogCustom4Admin(admin.ModelAdmin):
    list_display = ["title", "created_at", "author_full_name"]

    def author_full_name(self, obj):
        return f"{obj.author.user.first_name} {obj.author.user.last_name}"

    def get_queryset(self, request):
        default_qs = super().get_queryset(request)
        improved_qs = default_qs.select_related("author", "author__user")
        return improved_qs


# admin.site.register(models.Blog, BlogCustom4Admin)


# ============================== LOG ENTRY ADMIN ============================= #


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


# ============================= CUSTOM PAGINATOR ============================= #


# Idea referred from
# https://hakibenita.com/optimizing-the-django-admin-paginator
class CustomPaginator(paginator.Paginator):
    @cached_property
    def count(self):
        return 9999999


class BlogCustom5Admin(admin.ModelAdmin):
    paginator = CustomPaginator


# admin.site.register(models.Blog, BlogCustom5Admin)


# ============================ BLOG CUSTOM 6 ADMIN =========================== #


class BlogCustom6Admin(admin.ModelAdmin):
    raw_id_fields = ("author",)


# admin.site.register(models.Blog, BlogCustom6Admin)


# ============================ BLOG CUSTOM 7 ADMIN =========================== #


class BlogCustom7Admin(admin.ModelAdmin):
    list_display = ["title", "created_at", "author_full_name"]
    list_select_related = ["author", "author__user"]

    def author_full_name(self, obj):
        return obj.author.name


# admin.site.register(models.Blog, BlogCustom7Admin)


# ============================ BLOG CUSTOM 8 ADMIN =========================== #


class BlogCustom8Admin(admin.ModelAdmin):
    actions = ("print_blogs_titles",)

    @admin.action(description="Prints title")
    def print_blogs_titles(self, request, queryset):
        for data in queryset.all():
            print(data.title)


# admin.site.register(models.Blog, BlogCustom8Admin)

# ============================= COVER IMAGE ADMIN ============================ #


class CoverImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.CoverImage, CoverImageAdmin)


# ================================= TAG ADMIN ================================ #


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Tag, TagAdmin)

# ============================================================================ #
