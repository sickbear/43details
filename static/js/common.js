$(document).ready(function(){

    var width_screen = $(window).width()
    if (width_screen <= 768) {
        $('.aside_fast_call').html('Звонок в 2 касания!<br>');
    }
      
    $(window).resize(function() {		
		if ($(window).width() < 770) {			
			$('.nav_menu').css('display','none');
        };
	});
    
    $('.nav_icon').click(function() {
        $('.nav_menu').toggle("slow");
    });
    
    $(window).resize(function() {		
		if ($(window).width() > 770) {			
			$('.nav_menu').css('display','flex');
        }
	});
    
    $(function($) {
        $('tr[data-href]').addClass('clickable').click( function() {
    window.location = $(this).attr('data-href');
        });
    });

    $(function($) {
       $('.phone').mask('+7 (999) 999-9999');
    });
    
    $(window).resize(function() {
        if ($(window).width() < 768) {
            $('.aside_fast_call').html('Звонок в 2 касания!<br>');
        } else {
            $('.aside_fast_call').html();
        };
    });
    
    $(window).resize(function() {
        if ($(window).width() > 641) {
            $('.aside_fast_call').html('');
        }
    });
    
});