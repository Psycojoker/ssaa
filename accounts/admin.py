# encoding: utf-8

from django.contrib import admin
from django.conf.locale.en import formats as en_formats

from reversion.admin import VersionAdmin

from .models import Movement

en_formats.DATE_FORMAT = "Y-m-d"


class MovementAdmin(VersionAdmin):
    fieldsets = (
        (None, {
            "fields": (("date", "amount"), ("title", "kind"), ("comment",))
        }),
    )

    list_display = ("date", "title", "credit_column", "debit_column")

    def debit_column(self, obj):
        if obj.kind == "debit":
            return obj.amount
        return ""

    debit_column.short_description = "Débit"

    def credit_column(self, obj):
        if obj.kind == "credit":
            return obj.amount
        return ""

    credit_column.short_description = "Crédit"

admin.site.register(Movement, MovementAdmin)
