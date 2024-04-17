from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from main.models import Category, Post, Tag, PostTags


class PostTagsInlineFormSet(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get("is_main"):
                count += 1
            if count > 1:
                raise ValidationError('Только один тэг может быть основным')
        if count == 0:
            raise ValidationError("Хотя бы один тэг должен быть основным")
        return super().clean()


class PostTagInline(admin.TabularInline):
    model = PostTags
    fields = ["tag", "is_main"]
    formset = PostTagsInlineFormSet


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostTagInline]
    list_display = ["title", "category", "created_at"]
    list_filter = ["category"]
    search_fields = ["title"]


admin.site.register(Category)
# admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

