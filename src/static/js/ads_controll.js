(function(){
	var header = $('.header').height();
	var ads_block = $('.ads__container--1');
	$(window).scroll(function () {
	  if ($(this).scrollTop() > header) {
	  	ads_block.addClass('fixed');
	  } else {
	  	ads_block.removeClass('fixed');
	  }
	});
})();

