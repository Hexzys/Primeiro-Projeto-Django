from django.contrib import admin
from .models import *
# Register your models here.

class CaregoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','description','url','add_date')
    search_fields=('title',)



class PostAdmin(admin.ModelAdmin):
    list_display=['image_tag','title','url','cat']
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=50

    class Media:
        js=("https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js",'js/script.js',)

admin.site.register(Category,CaregoryAdmin)
admin.site.register(Post,PostAdmin)
