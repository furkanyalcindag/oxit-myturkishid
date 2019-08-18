from django.contrib import admin

from inoks.models import City, Job, District


class InoksAdminCity(admin.ModelAdmin):
    class Meta:
        City


class InoksAdminJob(admin.ModelAdmin):
    class Meta:
        Job


class InoksAdminDistrict(admin.ModelAdmin):
    class Meta:
        District


admin.site.register(City, InoksAdminCity)
admin.site.register(Job, InoksAdminJob)
admin.site.register(District, InoksAdminDistrict)
