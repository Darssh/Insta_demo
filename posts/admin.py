from django.contrib import admin

from .models import Posts, UsersPosts
# Register your models here.

admin.site.register(Posts)
admin.site.register(UsersPosts)
