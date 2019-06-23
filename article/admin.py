from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article,ArticleType,ReadNum
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_time', 'last_updated_time','create_month')

@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')