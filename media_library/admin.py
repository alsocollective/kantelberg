from django.contrib import admin
from media_library.models import *

# Register your models here.
class imageAdminView(admin.ModelAdmin):

	readonly_fields = ('showImage',)
	fieldsets = [
		('',{
			'fields':[('title','showImage','image','carousel')]}
		),]
	list_display = ('title','showImage','carousel')
	list_editable = ('carousel',)

admin.site.register(Image,imageAdminView)