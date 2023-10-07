from django.contrib import admin
from .models import Ad,Comment
# Register your models here.

admin.site.register(Ad)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display=['text']