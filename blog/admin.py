from django.contrib import admin

# Register your models here.
from blog.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title']
admin.site.register(Post,PostAdmin)

