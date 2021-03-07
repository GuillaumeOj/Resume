from django.contrib import admin

from resume.models import about
from resume.models import portfolio
from resume.models import project
from resume.models import social


class AboutAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Identity", {"fields": [("first_name", "last_name"), "contact"]}),
        ("Place", {"fields": [("place", "country")]}),
        ("Biography", {"fields": ["description"]}),
    ]

    list_display = ("first_name", "last_name")


class SocialInline(admin.TabularInline):
    model = social.Social
    fields = ["url", "title", "icon"]
    extra = 1
    classes = ["collapse"]


class SocialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Link", {"fields": ["url", "title"]}),
        ("Icon", {"fields": ["icon"]}),
    ]

    list_display = ["title"]


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Details", {"fields": [("number", "name", "pending", "achieved")]}),
    ]

    list_display = ["number", "name", "pending", "achieved"]


admin.site.register(about.About, AboutAdmin)
admin.site.register(social.Social, SocialAdmin)
admin.site.register(project.Project, ProjectAdmin)
admin.site.register(portfolio.PortfolioCategory)
admin.site.register(portfolio.Portfolio)
