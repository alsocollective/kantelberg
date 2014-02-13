from django.shortcuts import render, render_to_response, get_object_or_404
from media_library.models import *
from product.models import *
import math
from easy_thumbnails.files import get_thumbnailer

def outputType(request):
	# if( request.is_phone is text.show_on_mobile and text.show_on_mobile or request.is_tablet is text.show_on_tablet and text.show_on_tablet or request.is_mobile is not text.show_on_desktop and text.show_on_desktop):	
	if(request.is_phone):
		return "phone"
	elif(request.is_tablet):
		return "tablet"
	return "desktop"

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
		# print "-------------------------"
		# print inVal[a]
		inVal[a].cover_image_link = get_thumbnailer(inVal[a].cover_image.image)[imageVersion].url
		a += 1
	return inVal

def getDoubleBackProjectCover(inVal,imageVersion):
	maxRang = len(inVal)
	a = 0
	out = []
	while a < maxRang:
		inVal[a].cover_image_link = get_thumbnailer(inVal[a].cover_image.image)[imageVersion].url
		a += 1
		if(a<maxRang):
			inVal[a].cover_image_link = get_thumbnailer(inVal[a].cover_image.image)[imageVersion].url
			out.append((inVal[a-1],inVal[a]))
		else:
			out.append((inVal[a-1],None))
		a += 1
	return out

# Create your views here.
def home(request):
	print "==========================="
	print "WE GOT A REQUEST"
	size = outputType(request)
	carousel = getImages(Image.objects.all().filter(carousel = True).order_by('order'),size)
	about = About.objects.select_related("services_one_image",'services_two_image','team_one_image','team_two_image','team_three_image','media_press').all()[:1].get()
	about.services_one_image_link = get_thumbnailer(about.services_one_image.image)[size].url
	about.services_two_image_link = get_thumbnailer(about.services_two_image.image)[size].url
	about.team_one_image_link = get_thumbnailer(about.team_one_image.image)[size].url
	about.team_two_image_link = get_thumbnailer(about.team_two_image.image)[size].url
	about.team_three_image_link = get_thumbnailer(about.team_three_image.image)[size].url
	about.media_press_links = makeTruplets(list(about.media_press.all().order_by('order')))

	projects = getDoubleBackProjectCover(list(Project.objects.prefetch_related('cover_image').all().order_by('order')),size)
	project_width = math.ceil(len(projects)/4.0)
	print "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+="
	print project_width
	project_cell_width = 100
	if(size == "desktop"):
		project_cell_width = 25/project_width
	project_width = project_width*100


	productCat = list(ProductCat.objects.prefetch_related('cover_image').all().order_by('order'))
	products = getDoubleBackProjectCover(productCat,size)
	product_width = math.ceil(len(productCat)/8.0)
	product_cell_width = 100
	if(size == "desktop"):
		product_cell_width = 25/product_width
	product_width = product_width*100

	productW = {
		"width":product_width,
		"cell":product_cell_width
	}
	projectW = {
		"width":project_width,
		"cell":project_cell_width
	}

	productNew = getProjectCover(WhatsNew.objects.all()[0].whats_new_products.prefetch_related('cover_image').all().order_by('order'),size)
	# productNew = getProjectCover(Product.objects.prefetch_related('cover_image').filter(whats_new = True),size)
	return render_to_response('index.html',{'about':about,'projects':projects,'products':products,"productW":productW,"projectW":projectW,'whats_new':productNew,"carousel":carousel,"size":size})






def getImages(inVal,size):
	out = []
	for a in inVal:
		out.append((get_thumbnailer(a.image)[size].url,a.description,get_thumbnailer(a.image)['thumb'].url))
	return out

def press(request,article = None):
	press = Press.objects.select_related("images").get(slug = article)
	press.image_links = getImages(press.images.all(),outputType(request))
	return render_to_response('ajaxmagazine.html',{'data':press})

def project(request,project = None):
	project = Project.objects.select_related("images").get(slug = project)
	project.image_links = getImages(project.images.all(),outputType(request))
	return render_to_response('ajaxprojects.html',{'data':project})

def doubleUP(inpit):
	maxRange = len(inpit)
	out = []
	a = 0
	while a < maxRange:
		if(a+1 < maxRange):
			out.append((inpit[a],inpit[a+1]))
		else:
			out.append((inpit[a],None))
		a += 2
	return out


def productCat(request,product = None):
	size = outputType(request)
	category = ProductCat.objects.get(slug = product)
	products = getProjectCover(category.products.prefetch_related('cover_image').all(),size)
	prodDouble = doubleUP(products)

	width = math.ceil(len(prodDouble*2)/10.0)
	cell_width = 100
	if(size == "desktop"):
		cell_width = 20/width
	width = width*100

	return render_to_response('ajaxproducts.html',{"category":category,'products':prodDouble,"width":width,"cell_width":cell_width})

def product(request,product = None):
	product = Product.objects.prefetch_related('images').get(slug = product)
	product.image_links = getImages(product.images.all(),outputType(request))
	return render_to_response('ajaxproduct.html',{"data":product})






