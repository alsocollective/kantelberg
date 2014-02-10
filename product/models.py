from django.db import models
from django.template.defaultfilters import slugify

from media_library.models import Image


class Product(models.Model):
	title = models.CharField(max_length=600)
	description = models.TextField(max_length=2000,blank=True)
	specification = models.TextField(max_length=2000,blank=True)
	price = models.TextField(max_length=2000,blank=True)

	cover_image = models.ManyToManyField(Image,related_name="product-cover-image+")
	images = models.ManyToManyField(Image,related_name="product-shots+")

	whats_new = models.BooleanField(default=True)
	whats_new_date = models.DateField(auto_now=True)


	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Product, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class ProductCat(models.Model):
	title = models.CharField(max_length=600)
	description = models.TextField(max_length=2000,blank=True)

	cover_image = models.ManyToManyField(Image,related_name="cover-image+")
	products = models.ManyToManyField(Product,related_name="products+")

	slug = models.SlugField(blank=True)

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

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Press, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Project(models.Model):
	title = models.CharField(max_length=600)
	description = models.TextField(max_length=2000)
	cover_image = models.ManyToManyField(Image,related_name="project-cover-image+")
	images = models.ManyToManyField(Image,related_name="project-images+")
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Project, self).save(*args, **kwargs)

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
	services_one_image = models.ManyToManyField(Image,related_name="services_one_image+")
	services_one_description = models.TextField(max_length=2000)
	services_two_title = models.CharField(max_length=600)
	services_two_image = models.ManyToManyField(Image,related_name="services_two_image+")
	services_two_description = models.TextField(max_length=2000)

	team_title = models.CharField(max_length=300)
	team_one_name = models.CharField(max_length=300)
	team_one_image = models.ManyToManyField(Image,related_name="team_one_image+")
	team_one_description = models.TextField(max_length=2000)
	team_two_name = models.CharField(max_length=300)
	team_two_image = models.ManyToManyField(Image,related_name="team_two_image+")
	team_two_description = models.TextField(max_length=2000)
	team_three_name = models.CharField(max_length=300)
	team_three_image = models.ManyToManyField(Image,related_name="team_three_image+")
	team_three_description = models.TextField(max_length=2000)

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

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(About, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title


