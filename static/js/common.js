$(document).ready(function(){
      
    $(window).resize(function() {		
		if ($(window).width() < 770) {			
			$('.nav_menu').css('display','none');
        }
	});
    
    $('.nav_icon').click(function(){
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

    $(function($){
       $('.phone').mask('+7 (999) 999-9999');
    });
});