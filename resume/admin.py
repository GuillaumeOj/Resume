from django.contrib import admin

from .models import About, PathWay, Experience, Social, Project


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 1
    classes = ["collapse"]


class SocialInline(admin.StackedInline):
    model = Social
    extra = 1
    classes = ["collapse"]


class AboutAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Identity", {"fields": ["first_name", "last_name"]}),
        ("Place", {"fields": ["place", "country"]}),
        ("Biography", {"fields": ["description"]}),
    ]

    list_display = ("first_name", "last_name")

    inlines = [SocialInline, ExperienceInline]


class PathWayAdmin(admin.ModelAdmin):
    fields = ["title"]

    list_display = ["title"]


class ExperienceAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Type", {"fields": ["path"]}),
        ("For", {"fields": ["about"]}),
        ("Description", {"fields": ["title", "subtitle", "description"]}),
        ("Dates", {"fields": ["start", "end"]}),
    ]

    list_display = ["title", "path", "about"]


class SocialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("For", {"fields": ["about"]}),
        ("Link", {"fields": ["url", "title"]}),
        ("Icon", {"fields": ["icon"]}),
    ]

    list_display = ["title", "about"]


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("For", {"fields": ["about"]}),
        ("Details", {"fields": [("number", "name", "achieved")]}),
    ]

    list_display = ["number", "name", "achieved", "about"]


admin.site.register(About, AboutAdmin)
admin.site.register(PathWay, PathWayAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Project, ProjectAdmin)
