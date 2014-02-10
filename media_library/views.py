from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
# from  also.models import Project,Category,Page
from media_library.models import *

from easy_thumbnails.files import get_thumbnailer


def home(request):
	images = Image.objects.all()
	print images
	# thumb_url = "ss"
	thumb_url = get_thumbnailer(images[0].image)['thumb'].url
	return render_to_response('index.html',{'images':thumb_url})
