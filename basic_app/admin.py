from django.contrib import admin
# from embed_video.admin import AdminVideoMixin
from basic_app import models

# Register your models here.
# class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
#     pass
admin.site.register(models.Mark)

# admin.site.register(models.Video, AdminVideo)
