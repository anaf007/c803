$(function() {
	var oWidth = $(window).width();
	$(".nav li").click(function(event) {
		if($(this).parent().attr("class") == "nav") {
			$(this).siblings('li').removeClass('active').children(".submenu").hide();
			$(this).siblings('li').find("span.arrow").removeClass("up").addClass("right");
			$(this).addClass('active');
			/*箭头*/
			var arrow = $(this).find("span.arrow");
			if(arrow.hasClass("up")) {
				arrow.removeClass("up");
				arrow.addClass("right");
			} else if(arrow.hasClass("right")) {
				arrow.removeClass("right");
				arrow.addClass("up");
			}

			/*箭头 end*/
			var subMenu = $(this).children(".submenu");
			subMenu.toggle();
		} else {
			event.stopPropagation();
			//return false;
		}

	})

	$(".submenu a").click(function() {
		$(".submenu a").removeClass("on")
		$(this).addClass("on");

	})

	//导航 end
	//页面边栏关闭（左边导航收缩）
	var body = $('body');
	var sidebar = $('.leftBox');
	$(".navbar_right .bar_left .diannao i").click(function() {
		$(this).toggleClass('rotate')
		if(body.hasClass("nav_closed")) {
			body.removeClass("nav_closed");
		} else {
			body.addClass("nav_closed");

		}
	})

	//onresize 事件会在窗口或框架被调整大小时发生。
	  // window.onresize = function() {
	var body = $('body');
	var oWidth = $(window).width();
	if(oWidth > 800 && oWidth < 1200) {
		body.addClass("nav_closed");
	} else {
		body.removeClass("nav_closed");
	}
	// }
	//页面边栏关闭（左边导航收缩）end
	//左边高度

	if(oWidth > 979) {
		var leftBox = $('.leftBox');
		var available_height = $(window).height();

		if(leftBox.height() < available_height) {

			$('.leftBox').css({
				"height": available_height
			});

		}

	}
	//左边高度
	//语言
	$(".languageBtn").click(function() {
		$(".language").toggle();
	})
	$(".language a").click(function() {
			$(".language").slideUp()
		})
		//语言 end

	//手机上面导航按钮
	$(".menuBtn").click(function() {
		$(".leftBox").toggle()
		$(this).toggleClass('rotate')
	})

	if(oWidth < 800) {
		$(".nav a").click(function() {
			if($(this).attr("href") != "javascript:void(0)") {
				$(".leftBox").hide();
			}
		});

	}

});