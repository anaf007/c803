$(function() {
    var oWidth = $(window).width();
    $(".nav li").click(function(event) {
        if ($(this).parent().attr("class") == "nav") {
            $(this).siblings("li").removeClass("active").children(".submenu").hide();
            $(this).siblings("li").find("span.arrow").removeClass("up").addClass("right");
            $(this).addClass("active");
            var arrow = $(this).find("span.arrow");
            if (arrow.hasClass("up")) {
                arrow.removeClass("up");
                arrow.addClass("right")
            } else {
                if (arrow.hasClass("right")) {
                    arrow.removeClass("right");
                    arrow.addClass("up")
                }
            }
            var subMenu = $(this).children(".submenu");
            subMenu.toggle()
        } else {
            event.stopPropagation()
        }
    });
    $(".submenu a").click(function() {
        $(".submenu a").removeClass("on");
        $(this).addClass("on")
    });
    var body = $("body");
    var sidebar = $(".leftBox");
    $(".sidebar_icon").click(function() {
        if (body.hasClass("nav_closed")) {
            body.removeClass("nav_closed")
        } else {
            body.addClass("nav_closed")
        }
    });
    var body = $("body");
    var oWidth = $(window).width();
    if (oWidth < 1200) {
        body.addClass("nav_closed")
    } else {
        body.removeClass("nav_closed")
    }
	
});


function toggle_fullscreen(){
    var fullscreenEnabled = document.fullscreenEnabled || document.mozFullScreenEnabled || document.webkitFullscreenEnabled;
    if(fullscreenEnabled){
    	if(!document.fullscreenElement && !document.mozFullScreenElement && !document.webkitFullscreenElement && !document.msFullscreenElement) {
    		launchIntoFullscreen(document.documentElement);
    	}else{
    		exitFullscreen();
    	}
    }
}

function launchIntoFullscreen(element) {
	if(element.requestFullscreen) {
		element.requestFullscreen();
	} else if(element.mozRequestFullScreen) {
		element.mozRequestFullScreen();
	} else if(element.webkitRequestFullscreen) {
		element.webkitRequestFullscreen();
	} else if(element.msRequestFullscreen) {
		element.msRequestFullscreen();
	}
}

function exitFullscreen() {
	if(document.exitFullscreen) {
		document.exitFullscreen();
	} else if(document.mozCancelFullScreen) {
		document.mozCancelFullScreen();
	} else if(document.webkitExitFullscreen) {
		document.webkitExitFullscreen();
	}
}
