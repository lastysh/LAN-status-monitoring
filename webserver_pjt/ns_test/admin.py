from django.contrib import admin
from ns_test.models import Ips

# Register your models here.
class IpsAdmin(admin.ModelAdmin):
	list_display = ['ip', 'mac', 'name', 'status', 'comment']


admin.site.register(Ips, IpsAdmin)