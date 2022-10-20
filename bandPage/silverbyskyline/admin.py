from django.contrib import admin
from .models import Post, Video

# Register your models here.
''' admin.py keeps track of what models are passed to the admin page - namely Post and Video '''

admin.site.register(Post)
admin.site.register(Video)
