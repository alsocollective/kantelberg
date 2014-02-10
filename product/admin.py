from django.contrib import admin
from product.models import *

# Register your models here.
# class imageAdminView(admin.ModelAdmin):

# 	readonly_fields = ('showImage',)
# 	fieldsets = [
# 		('',{
# 			'fields':[('title','description','showImage','image','carousel')]}
# 		),]
# 	list_display = ('title','showImage','carousel')
# 	list_editable = ('carousel',)

admin.site.register(Product)
admin.site.register(Press)
admin.site.register(ProductCat)
admin.site.register(Project)
admin.site.register(About)
