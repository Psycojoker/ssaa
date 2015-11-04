from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import Movement


class MovementAdmin(VersionAdmin):
    fieldsets = (
        (None, {
            "fields": (("date", "amount"), ("title", "kind"), ("comment",))
        }),
    )

    list_display = ("date", "title", "amount", "kind")

admin.site.register(Movement, MovementAdmin)
