from django.contrib import admin

# Register your models here.
from .models import Contact,Post,Video
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Video)



