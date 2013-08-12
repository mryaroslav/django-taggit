from __future__ import unicode_literals

from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import Tag, TaggedItem


class TaggedItemInline(admin.StackedInline):
    model = TaggedItem

class TagAdmin(TranslationAdmin):
    inlines = [
        TaggedItemInline
    ]
    list_display = ["name", "slug"]
    ordering = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Tag, TagAdmin)
