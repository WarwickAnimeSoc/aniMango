from django.contrib import admin, messages
from django.core.exceptions import ValidationError

from .models import Song, Request, ArchivedRequest


class RequestAdmin(admin.ModelAdmin):
    readonly_fields = (
        'ultrastar_url',
    )

    list_display = (
        'title',
        'artist',
        'ultrastar_url'
    )

    actions = (
        'complete',
        'cancel'
    )

    search_fields = (
        'artist',
        'title'
    )

    def complete(self, request, queryset):
        for request_obj in queryset:
            try:
                request_obj.complete()
            except ValidationError:
                messages.error(request, "{0} has an invalid AniList link".format(request_obj))

    complete.short_description = "Complete the request"

    def cancel(self, request, queryset):
        for request_obj in queryset:
            request_obj.remove()

    cancel.short_description = "Cancel the request"


class ArchivedRequestAdmin(admin.ModelAdmin):

    list_display = (
        'ultrastar_url',
        'status'
    )

class SongAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'artist',
        'series'
    )

    search_fields = (
        'artist',
        'title'
    )


admin.site.register(Song, SongAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(ArchivedRequest, ArchivedRequestAdmin)
