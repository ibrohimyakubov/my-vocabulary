from mptt.admin import DraggableMPTTAdmin
from django.contrib import admin

from .models import BigDepartment, Unit, Vocabulary


class VocabularyAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_uz', 'type', 'unit']
    list_filter = ['type']
    search_fields = ['title_en', 'title_uz', 'unit']


class UnitAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',)
    list_display_links = ('indented_title',)


admin.site.register(
    Unit,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
# admin.site.register(Unit, UnitAdmin1)
admin.site.register(BigDepartment)
admin.site.register(Vocabulary, VocabularyAdmin)
