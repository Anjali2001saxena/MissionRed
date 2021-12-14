from django.contrib import admin
from users.models import Posts, Schedule, Users

# Register your models here.
admin.site.register(Users)
admin.site.register(Schedule)
admin.site.register(Posts)