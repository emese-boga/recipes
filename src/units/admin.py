from django.contrib import admin

from .models import Unit


class UnitAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "short_name", "unit_type")
    readonly_fields = ("id", "name", "short_name", "unit_type")

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Unit, UnitAdmin)
