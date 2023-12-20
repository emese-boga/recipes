from django.contrib import admin

from .models import Unit


class UnitAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "short_name", "unit_type")
    readonly_fields = ("id", "name", "short_name", "unit_type")

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Unit, UnitAdmin)
