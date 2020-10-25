from django.contrib import admin

from .models import ViewCounter, View


class ViewCounterAdmin(admin.ModelAdmin):
    pass


class ViewAdmin(admin.ModelAdmin):
    pass


admin.site.register(ViewCounter, ViewCounterAdmin)
admin.site.register(View, ViewAdmin)
