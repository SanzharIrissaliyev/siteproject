from django.contrib import admin
from main.models import *
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    pass


admin.site.register(About, AboutAdmin)


class AboutUsAdmin(admin.ModelAdmin):
    pass


admin.site.register(AboutUs, AboutUsAdmin)


class CountAdmin(admin.ModelAdmin):
    pass


admin.site.register(Count, CountAdmin)


class ServiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Service, ServiceAdmin)


class TeamAdmin(admin.ModelAdmin):
    pass


admin.site.register(Team, TeamAdmin)


class BlogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)


class AboutCountAdmin(admin.ModelAdmin):
    pass


admin.site.register(AboutCount, AboutCountAdmin)


class InformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Information, InformationAdmin)