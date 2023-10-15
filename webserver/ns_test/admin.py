from django.contrib import admin
from ns_test.models import Ips, Comment  # noqa


# Register your models here.
class IpsAdmin(admin.ModelAdmin):
    list_display = ['ip', 'mac', 'name', 'status', 'comment']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['ip', 'comment']


admin.site.register(Ips, IpsAdmin)
admin.site.register(Comment, CommentAdmin)
