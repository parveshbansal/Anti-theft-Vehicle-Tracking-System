from django.contrib import admin
from testapp.models import gadi
class VTSAdmin(admin.ModelAdmin):
	list_display=['username','gadicompanyname','gadiname','gadino','phoneno']
admin.site.register(gadi,VTSAdmin)	

