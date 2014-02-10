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

	actions=['really_delete_selected']


	def get_actions(self, request):
		actions = super(imageAdminView, self).get_actions(request)
		del actions['delete_selected']
		return actions

	def really_delete_selected(self, request, queryset):

		for obj in queryset:
			print "deleting this object"
			print obj
			obj.remove()
			obj.delete()


		if queryset.count() == 1:
			message_bit = "1 photoblog entry was"
		else:
			message_bit = "%s photoblog entries were" % queryset.count()
		self.message_user(request, "%s successfully deleted." % message_bit)

	really_delete_selected.short_description = "Delete selected entries - custom"



admin.site.register(Image,imageAdminView)