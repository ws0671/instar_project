from django.contrib import admin
from .models import Article, Photo,Comment,Tag
# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo

# Article 클래스는 해당하는 Photo 객체를 리스트로 관리한다. 
class ArticleAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]

# Register your models here.
admin.site.register(Article, ArticleAdmin)

admin.site.register(Comment)
admin.site.register(Tag)