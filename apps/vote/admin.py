from django.contrib import admin

from .models import VoteQuestion, VoteVariant, VoteAnswer


class VoteVariantTabularInline(admin.TabularInline):
    model = VoteVariant
    extra = 1


@admin.register(VoteQuestion)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date', 'created_at']
    inlines = [VoteVariantTabularInline, ]


admin.site.register(VoteAnswer)
