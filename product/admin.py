from django.contrib import admin
from product.models import *

class aboutPage(admin.ModelAdmin):
	readonly_fields = ('showImageone','showImagetwo','showTeamone','showTeamtwo','showTeamthree')
	filter_horizontal = ('services_one_image','services_two_image','team_one_image','team_two_image','team_three_image','media_press',)
	fieldsets = (
		('Company Info', {
			'classes': ('collapse',),
			'fields': ('company_info_title', 'company_info')
		}),
		('Services', {
			'classes': ('collapse',),
			'fields': ('services_title', 'services_one_title',('services_one_image','showImageone'),'services_one_description','services_two_title',('services_two_image','showImagetwo'),'services_two_description')
		}),
		('Team', {
			'classes': ('collapse',),
			'fields': ('team_title', 'team_one_name',('team_one_image','showTeamone'),'team_one_description','team_two_name',('team_two_image','showTeamtwo'),'team_two_description','team_three_name',('team_three_image','showTeamthree'),'team_three_description',)
		}),
		('Media', {
			'classes': ('collapse','bohdan_is_awesome'),
			'fields': ('media_title', 'media_press',)
		}),
		('Address', {
			'classes': ('collapse',),
			'fields': ('street', 'city','province','country','postal_code','phone_number','email_address')
		}),
		('Map Options', {
			'classes': ('collapse',),
			'fields': ('log_lag','map_info_bubble')
		}),
		('Display Options', {
			'classes': ('collapse','display-options'),
			'fields': (('show_main_carousel_phone','show_main_carousel_tablet','show_main_carousel_desktop'),
				('show_about_company_info_phone','show_about_company_info_tablet',"show_about_company_info_desktop"),
				('show_about_services_phone','show_about_services_tablet','show_about_services_desktop'),
				('show_about_team_phone','show_about_team_tablet','show_about_team_desktop'),
				('show_about_media_phone','show_about_media_tablet','show_about_media_desktop'),
				('show_projects_phone','show_projects_tablet','show_projects_desktop'),
				('show_products_phone','show_products_tablet','show_products_desktop'),
				('show_whatsnew_phone','show_whatsnew_tablet','show_whatsnew_desktop'),
				('show_map_phone','show_map_tablet','show_map_desktop'))
		}),
	)

class PressPage(admin.ModelAdmin):
fieldsets = (
		('Company Info', {
			'classes': ('collapse',),
			'fields': ('company_info_title', 'company_info')
		}),
		)


admin.site.register(Press,PressPage)
admin.site.register(Product)
admin.site.register(ProductCat)
admin.site.register(Project)
admin.site.register(About,aboutPage)
