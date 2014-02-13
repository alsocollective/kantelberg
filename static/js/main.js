var nav,navH,footer,footerH,loadArea,loadingScreen,rootHash,slideMenu,map;

$(document).ready(function() {

/*
  __ ___ __  _ ___ ___  __  _
 / _] __|  \| | __| _ \/  \| |
| [/\ _|| | ' | _|| v / /\ | |_
 \__/___|_|\__|___|_|_\_||_|___|

*/
	nav = $('nav'),
	footer = $("footer"),
	loadArea = $("#loaded-content"),
	loadingScreen = $("#loading-screen"),
	productPage = $("#product-page"),
	rootHash = "",
	phone = $("body").hasClass('phone');

/*$
 __  _  __   _   _
|  \| |/  \ | \ / |
| | ' | /\ |`\ V /'
|_|\__|_||_|  \_/

*/

	/*
	  __ _____ _  ____  ___ __  _  __
	/' _/_   _| |/ _/ |/ / |  \| |/ _]
	`._`. | | | | \_|   <| | | ' | [/\
	|___/ |_| |_|\__/_|\_\_|_|\__|\__/

	*/
		if(!phone){
			nav.height($('nav ul').height()); //This will break if font loads in late
			nav.waypoint(function(direction){
				if(direction == "down"){
					$(this).addClass('nav-fixed');
					$(this.parentNode).height($(this).outerHeight())
				} else {
					$(this).removeClass('nav-fixed');
				}
			},
			{
				triggerOnce: true
			}
			);

			footer.waypoint(function(direction){
				if(direction == "down"){
					$(footer).removeClass('normal-footer')
					$(this).addClass('fixed-footer');
					$(this.parentNode).height($(this).outerHeight())
				} else {
					$(this).removeClass('fixed-footer');
				}
			},{
				offset: $(window).height()-$(footer).outerHeight(),
				triggerOnce: true
			});

			$("#contact").waypoint(function(direction){
				if(direction == "up"){
					footer.removeClass('normal-footer')
					footer.addClass('fixed-footer')
				} else {
					footer.addClass('normal-footer')
					footer.removeClass('fixed-footer')
				}
			},{
				offset: $(window).height()-$(footer).outerHeight(),
			});

			$("#about").waypoint(function(direction){
				if(direction == "up"){
					nav.removeClass('nav-fixed')
				} else {
					nav.addClass('nav-fixed')
				}
			},{
				offset: nav.height()
			});

		} else {
			footer.addClass('normal-footer');
			slideMenu = $("nav").pullSlider({inmode:true,debug:true});
		}

	/*
	 _  _ ___ _  __ _  _ _   _  __ _  _ _____
	| || | __| |/ _] || | | | |/ _] || |_   _|
	| >< | _|| | [/\ >< | |_| | [/\ >< | | |
	|_||_|___|_|\__/_||_|___|_|\__/_||_| |_|

	*/
		var points = ["#about","#projects","#products","#whats-new","#contact"];
		if(!phone){
			for(var a = 0, max = points.length; a < max; ++a){
				$(points[a]).waypoint(heighLighting,{
					offset: $(nav).outerHeight()+100
				});
			}
		} else {
			for(var a = 0, max = points.length; a < max; ++a){
				$(points[a]).waypoint(heighLighting,{
					offset: $("nav .last-button").outerHeight()+100
				});
			}
		}

	/*
	 __   __  _   _  __  _     __  ___ ___  __  _   _
	| _\ /__\| | | ||  \| |__ /  \| _ \ _ \/__\| | | |
	| v | \/ | 'V' || | ' |__| /\ | v / v / \/ | 'V' |
	|__/ \__/!_/ \_!|_|\__|  |_||_|_|_\_|_\\__/!_/ \_!

	*/
		$("#down-arrow").waypoint(function(){
			this.parentNode.removeChild(this);
		},
		{
			triggerOnce: true
		});
		$("#down-arrow").click(function(){
			animateScroll($("#about")[0]);
		})

	/*
	  ____   _  ____  __
	 / _/ | | |/ _/ |/ /
	| \_| |_| | \_|   <
	 \__/___|_|\__/_|\_\

	*/
		function NavClickEvent(event){
			event.preventDefault();
			animateScroll($(this.href.split("/").pop())[0]);
			if(phone){
				slideMenu.refindHeight();
			}
			closeLoaded();
			closeLoaded();
			return false;
		}
		$("nav a:not(#instagram)").click(NavClickEvent).on("touchend",NavClickEvent);

/*
  __  __   __ __   __     ___   __
 /  \|_ \ /  \\ \_/ /_ __| _ \/' _/
| /\ |_\ | /\ |> , <__|__| v /`._`.
|_||_/___|_||_/_/ \_\    |_|_\|___/

*/
	var tempLink; //remove this when in production...
	$("#projects .coloum a").click(loadSeqProjects)
	$("#products .coloum a").click(loadSeqProducts);
	$("#whats-new a").click(loadSeqProduct)
	$("#media table a").click(loadSeqMagazine);



// Sub category navigation
	$("#products .left-button").click(scrollLeftForSection);
	$("#products .right-button").click(scrollRightForSection);

	$("#projects .left-button").click(scrollLeftForProject)
	$("#projects .right-button").click(scrollRightForProject);




loadGoogleScript();
resizeSections();
$("#font-loaded").ready(resizeSections);
$(window).resize(resizeSections);
setTimeout(resizeSections,1000);
//Exit view!!!! with esc
$(document).keyup(function(e) {
	if (e.keyCode == 27) {
		$($(".loaded-closer")[0]).click();
	}
});

});


/*
 ___ _  _ __  _  ________ _  __  __  _   __
| __| || |  \| |/ _/_   _| |/__\|  \| |/' _/
| _|| \/ | | ' | \__ | | | | \/ | | ' |`._`.
|_|  \__/|_|\__|\__/ |_| |_|\__/|_|\__||___/
*/

	/*
	  __  __   __ __   __
	 /  \|_ \ /  \\ \_/ /
	| /\ |_\ | /\ |> , <
	|_||_/___|_||_/_/ \_\

	*/

		function loadSeqMagazine(){
			event.preventDefault();
			showLoading();
			tempLink = this.href;
			setTimeout(function(){
				loadArea.load(tempLink,loadMagazine);
				setState(rootHash+"/"+tempLink.split("/").pop());
			},1000)
			return false;
		}

		function loadMagazine(response, status){
			if(status == "error"){
				ajaxLoadError();
			}
			scrolllocation = $(window).scrollTop();
			hideLoading();
			loadArea[0].className = "load-active magazine-loaded";
			$(".sub-head").height(navH);
			$(".rsmagazines").height($(window).height()-(navH*2)-footerH);
			$(".loaded-closer").click(closeLoaded);
			$(".loaded-closer").on("touchstart",closeLoaded);
			$(".rsmagazines").royalSlider({
				controlNavigation:'none',
				imageScaleMode:"fit",
				navigation:"none",
				keyboardNavEnabled: true
			});
			openLoaded();
		}

		function loadSeqProjects(event){
			event.preventDefault();
			if(!phone){
				animateScroll(this.parentNode);
			}
			showLoading();
			tempLink = this.href;
			setTimeout(function(){
				loadArea.load(tempLink,loadProjects);
				setState(rootHash+"/"+tempLink.split("/").pop());
			},1000)
			return false;
		}

		function loadProjects(response, status){
			if(status == "error"){
				ajaxLoadError();
			}
			scrolllocation = $(window).scrollTop();
			hideLoading();
			loadArea[0].className = "load-active projects-loaded";
			$(".sub-head").height(navH);
			$(".rsprojects").height($(window).height()-(navH*2)-footerH);
			$(".loaded-closer").click(closeLoaded);
			$(".loaded-closer").on("touchstart",closeLoaded);
			$(".rsprojects").royalSlider({
				imageScaleMode:"fill",
				controlNavigation:'none',
				keyboardNavEnabled: true
			});
			openLoaded();
		}

		function loadSeqProducts(event){
			event.preventDefault();
			if(!phone){
				animateScroll(this.parentNode);
			}
			showLoading();
			tempLink = this.href;
			setTimeout(function(){
				loadArea.load(tempLink,loadProducts);
				setState(rootHash+"/"+tempLink.split("/").pop());
			},1000)
			return false;
		}

		function loadProducts(response, status){
			if(status == "error"){
				ajaxLoadError();
			}
			scrolllocation = $(window).scrollTop();
			hideLoading();
			loadArea[0].className = "load-active products-loaded";
			$(".sub-head").height(navH);
			$(".products-loaded .loaded-closer").click(closeLoaded)
			$(".products-loaded .loaded-closer").on("touchstart",closeLoaded);
			$("#products-content .image-container").click(loadSeqProduct).on("touchstart",loadSeqProduct);
			openLoaded();
			$("#products-content .left-button").click(scrollLeftForProductsLoaded);
			$("#products-content .right-button").click(scrollRightForProductsLoaded);
		}

		function loadSeqProduct(event){
			event.preventDefault();
			if(!phone){
				animateScroll(this.parentNode);
			}
			showLoading();
			tempLink = this.href;
			setTimeout(function(){
				productPage.load(tempLink,loadProduct);
				setState(rootHash+"/"+tempLink.split("/").pop());
			},1000)
			return false;
		}

		var slider;
		function loadProduct(response, status){
			if(status == "error"){
				ajaxLoadError();
			}
			scrolllocation = $(window).scrollTop();
			hideLoading();
			productPage[0].className = "load-active product-loaded";
			if(phone){
				productPage.height($(window).height()-navH);
				$(".sub-head").addClass('absolute-head')
				$(".rs-special").height("100%");
			} else {
				productPage.height("100%");
				$(".product-loaded .left, .product-loaded .right").height($(window).height()-(navH*3)-footerH);
				$(".sub-head").height(navH);
			}
			$(".product-loaded .loaded-closer").click(closeLoaded);
			$(".product-loaded .loaded-closer").on("touchstart",closeLoaded);
			var controllNav = function(){ if(!phone){return 'thumbnails'} else {return "none"}};
			slider = $(".rs-special").royalSlider({
				controlNavigation: controllNav(),
				thumbs: {
					// orientation: 'vertical',
					fitInViewport: true,
					// spacing: 0,
					// appendSpan:true
				},
				globalCaption: false,
				fadeinLoadedSlide: true,
				imageAlignCenter: true,
				imageScaleMode: 'fill',
				autoScaleSlider: false,
				arrowsNav: true,
				arrowsNavAutoHide:false,
				keyboardNavEnabled: true
			});

			if(!phone){
				var subNav = $(".rs-special .rsNav")
				$("#product-page .left")[0].appendChild(subNav[0])
				subNav.find(".rsThumbsContainer").css({"height":"auto"});
				// $(".rs-special .rsArrowLeft").css({"position":"fixed"});
				// $(".rs-special .rsArrowRight").css({"position":"fixed"});
			}
			openLoaded();
		}

		function ajaxLoadError(){
			alert("bad Ajax call");
			window.location.replace("");
			window.location.href = "";
		}

	/*
	 _   __   __  __  _ __  _  __
	| | /__\ /  \| _\| |  \| |/ _]
	| || \/ | /\ | v | | | ' | [/\
	|___\__/|_||_|__/|_|_|\__|\__/
	*/
		function showLoading(){
			// loadingScreen.removeClass('hidden');
			loadingScreen.fadeIn('400');
		}
		function hideLoading(){
			// loadingScreen.addClass('hidden');
			loadingScreen.fadeOut('400');
		}
		function closeLoaded(event){
			if(event){
				event.preventDefault();
			}
			setState(rootHash);

			if(productPage[0].className){
				productPage[0].className = "";
				productPage[0].innerHTML = "";
				if(!loadArea[0].className){
					$(window).off("scroll",noscroll);
					$(window).off("touchstart",noTouch);
					removeInSubPage();
				}
			} else {
				loadArea[0].className = "";
				loadArea[0].innerHTML = "";
				$(window).off("scroll",noscroll);
				$(window).off("touchstart",noTouch);
				removeInSubPage();
			}
			return false;
		}

		// Noscroll and No title Changes
		function openLoaded(){
			console.log("no more touching!");
			$(window).on("scroll",noscroll);
			$(window).on("touchstart",noTouch);
			setAsInSubPage();
		}

	/*
	  __   ______  __  _   _
	/' _/ / _/ _ \/__\| | | |
	`._`.| \_| v / \/ | |_| |_
	|___/ \__/_|_\\__/|___|___|

	*/
		var scrolllocation = 0;
		function noscroll(event){
			window.scroll(0,scrolllocation);
			event.preventDefault();
			return false;
		}
		function noTouch(event){
			window.scroll(0,scrolllocation);
			event.preventDefault();
			return false;
		}

		var scrolling = false;
		function animateScroll(element){
			if(element){
				$('html, body').animate({scrollTop :  $(element).offset().top-navH+$(element).outerHeight()-$(element).height()},500);
			} else {
				console.log("ERROR: No element passed into animateScroll");
			}
		}

		var productsLoadedScroll = 0,
		productsLoadedScreens = 0;
		function scrollRightForProductsLoaded(event){
			event.preventDefault();
			animateScroll(this.parentNode);
			var container = $(this.parentNode).find(".container");
			console.log(productsLoadedScroll,productsLoadedScreens);
			if(productsLoadedScroll-1 <= productsLoadedScreens){
				productsLoadedScroll = 0;
			} else {
				--productsLoadedScroll;
			}
			console.log(productsLoadedScroll,productsLoadedScreens);
			container.css({"left":(productsLoadedScroll*100)+"%"});
			return false;
		}
		function scrollLeftForProductsLoaded(event){
			event.preventDefault();
			animateScroll(this.parentNode);
			var container = $(this.parentNode).find(".container");
			console.log(productsLoadedScroll,productsLoadedScreens);
			if(productsLoadedScroll+1 > 0 ){
				productsLoadedScroll = productsLoadedScreens+1;
			} else {
				++productsLoadedScroll;
			}
			console.log(productsLoadedScroll,productsLoadedScreens);
			container.css({"left":(productsLoadedScroll*100)+"%"});
			return false;
		}

		var productScroll = 0,
		productScreens = 0;
		function scrollRightForSection(event){
			event.preventDefault();
			animateScroll(this.parentNode);
			var container = $(this.parentNode).find(".container");

			if(productScreens === 0){
				productScreens = container[0].style.width
				productScreens = parseInt(productScreens.slice(0,-3))*-1
			}

			console.log(productScroll-1 , productScreens)
			if(productScroll-1 <= productScreens){
				productScroll = 0;
			} else {
				--productScroll;
			}
			console.log(productScroll);
			container.css({"left":(productScroll*100)+"%"});

			return false;
		}
		function scrollLeftForSection(event){
			event.preventDefault();
			animateScroll(this.parentNode);
			var container = $(this.parentNode).find(".container");

			if(!productScreens === 0){
				productScreens = container[0].style.width
				productScreens = parseInt(productScreens.slice(0,-3))*-1
			}

			if(productScroll+1 > 0){
				productScroll = productScreens+1;
			} else {
				++productScroll;
			}
			console.log(productScroll);
			container.css({"left":(productScroll*100)+"%"});

			return false;
		}

		var projectScroll = 0,
		prodjectScreens = 0;
		function scrollRightForProject(event){
			event.preventDefault();
			animateScroll(this.parentNode);
			var container = $(this.parentNode).find(".container");
			if(prodjectScreens === 0){
				prodjectScreens = container[0].style.width
				prodjectScreens = parseInt(prodjectScreens.slice(0,-3))*-1
			}
			if(projectScroll-1 <= prodjectScreens){
				projectScroll = 0;
			} else {
				--projectScroll;
			}
			container.css({"left":(projectScroll*100)+"%"});
			return false;
		}
		function scrollLeftForProject(event){
			event.preventDefault();
			animateScroll(this.parentNode);
			var container = $(this.parentNode).find(".container");
			if(!prodjectScreens === 0){
				prodjectScreens = container[0].style.width
				prodjectScreens = parseInt(prodjectScreens.slice(0,-3))*-1
			}
			if(projectScroll+1 > 0){
				projectScroll = prodjectScreens+1;
			} else {
				++projectScroll;
			}
			container.css({"left":(projectScroll*100)+"%"});
			return false;
		}



function resizeSections(){
	if(!phone){
		navH = nav.outerHeight(),
		footerH = footer.outerHeight();
	} else {
		navH = $("nav .last-button").outerHeight();
		footerH = 0;
	}
	var height = $(window).height()-footerH-navH;

	if(!phone){
		$("#projects").height(height);
		$("#products").height(height);
		// $("#whats-new").height(height);
		$(productPage).height("100%");
	}else{
		slideMenu.refindHeight();
		$(productPage).height($(window).height()-navH);
	}
		// $("#contact").height("auto");

	$("#contact").height($(window).height()-navH-footerH);
	// if(map){
	// 	console.log("yep");
	// 	google.maps.event.trigger(map, "resize");
	// }
	$("#loaded-content").height(height);
	$("#loaded-content").css({"top":navH})
	$(productPage).css({"top":navH})
}

	/*
	 _   __   ___ __ _____ _  __  __  _
	| | /__\ / _//  \_   _| |/__\|  \| |
	| || \/ | \_| /\ || | | | \/ | | ' |
	|___\__/ \__/_||_||_| |_|\__/|_|\__|

	*/

		function setAsInSubPage(){
			$("body").addClass('in-sub-page');
		}

		function removeInSubPage(){
			$("body").removeClass('in-sub-page');
		}

		function heighLighting(direction){
			if($("body").hasClass('in-sub-page')){
				return false;
			}

			if(direction == "down"){
				$(".heighlight").removeClass('heighlight');
				$("#nav-"+this.id).addClass('heighlight');
				rootHash = this.id;
				setState(rootHash);
			} else {
				var el = $($("#nav-"+this.id).parent()[0]).prev().children()[0];
				if(el){
					rootHash = el.id.split(/-(.+)?/)[1];
					setState(rootHash);
				} else {
					rootHash = "";
					setState();
				}
				$(".heighlight").removeClass('heighlight');
				$(el).addClass('heighlight');
			}
		}

		function setState(address){
			if (history && history.pushState) {
				if(address){
					history.pushState("","","/"+address+"/");
				} else {
					history.pushState("","","/");
				}
			} else {
				if(address){
					window.location.hash = address;
				} else {
					window.location.hash = "";
				}
			}
		}


/*
  __  __   __   __ _   ___ __ __  __  ___   __
 / _]/__\ /__\ / _] | | __|  V  |/  \| _,\/' _/
| [/\ \/ | \/ | [/\ |_| _|| \_/ | /\ | v_/`._`.
 \__/\__/ \__/ \__/___|___|_| |_|_||_|_|  |___/

*/
	var marker;
	function initialize() {
		var myLatlng = new google.maps.LatLng(43.7003146,-79.4538919);

		var mapOptions = {
			zoom: 16,
			center: myLatlng,
			scrollwheel: false,
			navigationControl: false,
			mapTypeControl: false,
			scaleControl: false,
			draggable: false,
			streetViewControl: false,
			streetViewControl: false,
			panControl:false,
			rotateControl:false,
			zoomControl:false,
			styles:[
					{
						"featureType": "landscape",
						"stylers": [
							{ "color": "#808080" }
						]
					},{
						"featureType": "poi",
						"stylers": [
							{ "visibility": "off" }
						]
					},{
						"featureType": "road",
						"elementType": "geometry",
						"stylers": [
							{ "color": "#aaaaaa" }
						]
					},{
						"elementType": "labels.text.stroke",
						"stylers": [
							{ "visibility": "off" }
						]
					},{
						"elementType": "labels.text",
						"stylers": [
							{ "color": "#393b37" }
						]
					}
				]
		};



		var contentString = " Kantelberg & Co 1150 Castlefield Ave York, ON M6B 1E9 Kantelberg & Co 1150 Castlefield AveYork, ON M6B 1E9 kantelbergco.com (416) 964-0192"

		map = document.getElementById('googlemap');
		$(map).height($(window).height()-navH-footerH);

		map = new google.maps.Map(map, mapOptions);

		// google.maps.event.addDomListener(window, "resize", function() {
		// 	var center = map.getCenter();
		// 	google.maps.event.trigger(map, "resize");
		// 	map.setCenter(center);
		// 	console.log("resizeing!!");
		// });

		var infowindow = new google.maps.InfoWindow({
			content: contentString,
			display:false
		});

		setTimeout(function(){
			infowindow.open(map);
		},1000);

		var image = {
			url:'/static/assets/map-icon.png',
			size: new google.maps.Size(50, 50),
			origin: new google.maps.Point(0,0),
			anchor: new google.maps.Point(50,50),
			scaledSize: new google.maps.Size(50,50)
		}

		marker = new google.maps.Marker({
			position: myLatlng,
			map: map,
			title: 'Kantelberg',
			icon: image//'/img/map-icon.png'
		});


		// google.maps.event.addListener(marker, 'click', function() {
		// 	infowindow.open(map,marker);
		// 	console.log(infowindow.display);
		// 	console.log("bohdan is awesome");
		// });
		//google.maps.event.addListener(marker, 'click', toggleBounce);
	}



	function loadGoogleScript() {
		var script = document.createElement('script');
		script.type = 'text/javascript';
		script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyAsprgq2AfDNOAr9zdeizAbhG_FNGyP8-4&v=3.exp&sensor=false&' + 'callback=initialize';
		document.body.appendChild(script);
	}

