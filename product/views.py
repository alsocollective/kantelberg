from django.shortcuts import render, render_to_response, get_object_or_404
from media_library.models import *
from product.models import *

from easy_thumbnails.files import get_thumbnailer




def makeTruplets(inVal):
	maxRang = len(inVal)
	a = 0
	out = []
	while a < maxRang-1:
		if(inVal[a+1]):
			out.append((inVal[a],inVal[a+1]))
		a += 2
	if(maxRang%2!=0):
		out.append((inVal[a-1],None))
	return out

def getProjectCover(inVal,imageVersion):
	maxRang = len(inVal)
	a = 0
	while a < maxRang:
		inVal[a].cover_image_link = get_thumbnailer(inVal[a].cover_image.all()[0].image)[imageVersion].url
		a += 1
	return inVal
# Create your views here.
def home(request):
	about = About.objects.select_related("services_one_image",'services_two_image','team_one_image','team_two_image','team_three_image','media_press').all()[:1].get()
	about.services_one_image_link = get_thumbnailer(about.services_one_image.all()[:1].get().image)['mobile'].url
	about.services_two_image_link = get_thumbnailer(about.services_two_image.all()[:1].get().image)['mobile'].url
	about.team_one_image_link = get_thumbnailer(about.team_one_image.all()[:1].get().image)['mobile'].url
	about.team_two_image_link = get_thumbnailer(about.team_two_image.all()[:1].get().image)['mobile'].url
	about.team_three_image_link = get_thumbnailer(about.team_three_image.all()[:1].get().image)['mobile'].url
	about.media_press_links = makeTruplets(list(about.media_press.all()))

	projects = getProjectCover(list(Project.objects.prefetch_related('cover_image').all()),"mobile")

	products = getProjectCover(list(ProductCat.objects.prefetch_related('cover_image').all()),"mobile")

	productNew = getProjectCover(Product.objects.prefetch_related('cover_image').filter(whats_new = True),"mobile")
	return render_to_response('index.html',{'about':about,'projects':projects,'products':products,'whats_new':productNew})






def getImages(inVal):
	out = []
	for a in inVal:
		out.append((get_thumbnailer(a.image)['mobile'].url,a.description,get_thumbnailer(a.image)['thumb'].url))
	return out

def press(request,article = None):
	press = Press.objects.select_related("images").get(slug = article)
	press.image_links = getImages(press.images.all())
	return render_to_response('ajaxmagazine.html',{'data':press})

def project(request,project = None):
	project = Project.objects.select_related("images").get(slug = project)
	project.image_links = getImages(project.images.all())
	return render_to_response('ajaxprojects.html',{'data':project})

def productCat(request,product = None):
	category = ProductCat.objects.get(slug = product)
	products = getProjectCover(category.products.prefetch_related('cover_image').all(),"mobile")
	return render_to_response('ajaxproducts.html',{"category":category,'products':products})

def product(request,product = None):
	product = Product.objects.prefetch_related('images').get(slug = product)
	product.image_links = getImages(product.images.all())
	return render_to_response('ajaxproduct.html',{"data":product})






