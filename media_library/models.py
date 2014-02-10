from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.template.defaultfilters import slugify
import os
import os.path
from easy_thumbnails.files import get_thumbnailer




class Image(models.Model):
	title = models.CharField(max_length=600)

	description = models.TextField(max_length=4000, blank=True)
	date = models.DateField(auto_now=True)
	slug = models.SlugField(blank=True)
	image = ThumbnailerImageField(upload_to='static/images', blank=True)
	carousel = models.BooleanField(default=False)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Image, self).save(*args, **kwargs)

	def showImage(self):
		if self.image:
			return '<img style="width:200px;height:auto;" src="/%s"/>' % get_thumbnailer(self.image)['preview'].url
		return "not an image"

	showImage.short_description = "current image"
	showImage.allow_tags = True

	def delete(self):
		print "delete the files"
		# find all the images nad eldelagw f0

	def __unicode__(self):
		return self.title
