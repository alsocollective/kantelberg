from django.db import models
from django.template.defaultfilters import slugify
from easy_thumbnails.files import get_thumbnailer

from media_library.models import Image


class Product(models.Model):
	title = models.CharField(max_length=600)
	description = models.TextField(max_length=2000,blank=True)
	specification = models.TextField(max_length=2000,blank=True)
	price = models.TextField(max_length=2000,blank=True)

	# cover_image = models.ManyToManyField(Image,related_name="product-cover-image+")
	cover_image = models.ForeignKey(Image, null=True, blank=True, default = None,related_name="r-product-cover-image+")
	images = models.ManyToManyField(Image,related_name="product-shots+")

	whats_new = models.BooleanField(default=True)
	whats_new_date = models.DateField(auto_now=True)
	def cover_image_show(self):
		# return '<p>yep</p>'
		out = "No Image"
		if self.cover_image:
			out = '<img style="width:300px;height:auto;" src="/%s"/>' % get_thumbnailer(self.cover_image.image)['preview'].url
		return out
	cover_image_show.short_description = "Servies one image"
	cover_image_show.allow_tags = True

	slug = models.SlugField(blank=True)

	order = models.IntegerField(default=99)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Product, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class ProductCat(models.Model):
	title = models.CharField(max_length=600)
	description = models.TextField(max_length=2000,blank=True)

	# cover_image = models.ManyToManyField(Image,related_name="cover-image+")
	cover_image = models.ForeignKey(Image, null=True, blank=True, default = None,related_name="r-cover-image+")
	products = models.ManyToManyField(Product,related_name="products+")

	slug = models.SlugField(blank=True)
	order = models.IntegerField(default=99)

	def cover_image_show(self):
		# return '<p>yep</p>'
		out = "No Image"
		if self.cover_image:
			out = '<img style="width:300px;height:auto;" src="/%s"/>' % get_thumbnailer(self.cover_image.image)['preview'].url
		return out
	cover_image_show.short_description = "Servies one image"
	cover_image_show.allow_tags = True

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(ProductCat, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Press(models.Model):
	title = models.CharField(max_length=600)
	date = models.CharField(max_length=300)
	images = models.ManyToManyField(Image,related_name="press-images+")
	slug = models.SlugField(blank=True)
	order = models.IntegerField(default=99)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Press, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Project(models.Model):
	title = models.CharField(max_length=600)
	description = models.TextField(max_length=2000)
	# cover_image = models.ManyToManyField(Image,related_name="project-cover-image+")
	cover_image = models.ForeignKey(Image, null=True, blank=True, default = None,related_name="r-project-cover-image+")
	images = models.ManyToManyField(Image,related_name="project-images+")
	slug = models.SlugField(blank=True)
	order = models.IntegerField(default=99)

	def cover_image_show(self):
		# return '<p>yep</p>'
		out = "No Image"
		if self.cover_image:
			out = '<img style="width:300px;height:auto;" src="/%s"/>' % get_thumbnailer(self.cover_image.image)['preview'].url
		return out
	cover_image_show.short_description = "Servies one image"
	cover_image_show.allow_tags = True

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Project, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class WhatsNew(models.Model):
	title = models.CharField(max_length=600)
	whats_new_products = models.ManyToManyField(Product,related_name="w_n_products+")
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(WhatsNew, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class About(models.Model):
	class Meta:
		verbose_name_plural = "About"
	title = models.CharField(max_length=600)

	company_info_title = models.CharField(max_length=300)
	company_info = models.TextField(max_length=2000)

	services_title = models.CharField(max_length=300)
	services_one_title = models.CharField(max_length=600)
	services_one_image = models.ForeignKey(Image, null=True, blank=True, default = None,related_name="r-services_one_image+")
	# services_one_image = models.ManyToManyField(Image,related_name="services_one_image+")
	def showImageone(self):
		return '<img style="width:300px;height:auto;" src="/%s"/>' % get_thumbnailer(self.services_one_image.all()[0].image)['preview'].url
	showImageone.short_description = "Servies one image"
	showImageone.allow_tags = True

	services_one_description = models.TextField(max_length=2000)
	services_two_title = models.CharField(max_length=600)
	services_two_image = models.ForeignKey(Image, null=True, blank=True, default = None,related_name="r-services_two_image+")
	# services_two_image = models.ManyToManyField(Image,related_name="services_two_image+")
	def showImagetwo(self):
		return '<img style="width:300px;height:auto;" src="/%s"/>' % get_thumbnailer(self.services_two_image.all()[0].image)['preview'].url
	showImagetwo.short_description = "Servies two image"
	showImagetwo.allow_tags = True
	services_two_description = models.TextField(max_length=2000)

	team_title = models.CharField(max_length=300)
	team_one_name = models.CharField(max_length=300)
	team_one_image = models.ForeignKey(Image, null=True, blank=True, default = None,related_name="r-team_one_image+")
	# team_one_image = models.ManyToManyField(Image,related_name="team_one_image+")
	team_one_description = models.TextField(max_length=2000)
	def showTeamone(self):
		return '<img style="width:300px;height:auto;" src="/%s"/>' % get_thumbnailer(self.team_one_image.all()[0].image)['preview'].url
	showTeamone.short_description = "Servies two image"
	showTeamone.allow_tags = True

	team_two_name = models.CharField(max_length=300)
	team_two_image = models.ForeignKey(Image, null=True, blank=True, default = None,related_name="r-team_two_image+")
	# team_two_image = models.ManyToManyField(Image,related_name="team_two_image+")
	team_two_description = models.TextField(max_length=2000)
	def showTeamtwo(self):
		return '<img style="width:300px;height:auto;" src="/%s"/>' % get_thumbnailer(self.team_two_image.all()[0].image)['preview'].url
	showTeamtwo.short_description = "Servies two image"
	showTeamtwo.allow_tags = True

	team_three_name = models.CharField(max_length=300)
	team_three_image = models.ForeignKey(Image, null=True, blank=True, default = None,related_name="r-team_three_image+")
	# team_three_image = models.ManyToManyField(Image,related_name="team_three_image+")
	team_three_description = models.TextField(max_length=2000)
	def showTeamthree(self):
		return '<img style="width:300px;height:auto;" src="/%s"/>' % get_thumbnailer(self.team_three_image.all()[0].image)['preview'].url
	showTeamthree.short_description = "Servies two image"
	showTeamthree.allow_tags = True

	media_title = models.CharField(max_length=300)
	media_press = models.ManyToManyField(Press,related_name="about-media+")

	slug = models.SlugField(blank=True)

	street = models.CharField(max_length=300)
	city = models.CharField(max_length=300)
	province = models.CharField(max_length=300)
	country = models.CharField(max_length=300)
	postal_code = models.CharField(max_length=300)
	phone_number = models.CharField(max_length=300)
	email_address = models.CharField(max_length=400)

	log_lag = models.CharField(max_length=400)
	map_info_bubble = models.TextField(max_length=2000)

	show_main_carousel_phone = models.BooleanField(default=True)
	show_main_carousel_tablet = models.BooleanField(default=True)
	show_main_carousel_desktop = models.BooleanField(default=True)

	show_about_company_info_phone = models.BooleanField(default=True)
	show_about_company_info_tablet = models.BooleanField(default=True)
	show_about_company_info_desktop = models.BooleanField(default=True)

	show_about_services_phone = models.BooleanField(default=True)
	show_about_services_tablet = models.BooleanField(default=True)
	show_about_services_desktop = models.BooleanField(default=True)

	show_about_team_phone = models.BooleanField(default=True)
	show_about_team_tablet = models.BooleanField(default=True)
	show_about_team_desktop = models.BooleanField(default=True)

	show_about_media_phone = models.BooleanField(default=True)
	show_about_media_tablet = models.BooleanField(default=True)
	show_about_media_desktop = models.BooleanField(default=True)

	show_projects_phone = models.BooleanField(default=True)
	show_projects_tablet = models.BooleanField(default=True)
	show_projects_desktop = models.BooleanField(default=True)

	show_products_phone = models.BooleanField(default=True)
	show_products_tablet = models.BooleanField(default=True)
	show_products_desktop = models.BooleanField(default=True)

	show_whatsnew_phone = models.BooleanField(default=True)
	show_whatsnew_tablet = models.BooleanField(default=True)
	show_whatsnew_desktop = models.BooleanField(default=True)

	show_map_phone = models.BooleanField(default=True)
	show_map_tablet = models.BooleanField(default=True)
	show_map_desktop = models.BooleanField(default=True)



	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(About, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title


