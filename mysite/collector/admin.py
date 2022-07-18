from django.contrib import admin

from .models import Work, Comment, Exhibit, Gallery

# Register your models here.

admin.site.register(Work)
admin.site.register(Comment)
admin.site.register(Exhibit)
admin.site.register(Gallery)
