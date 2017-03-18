$('.sidebar-link').click(function(e){
  e.preventDefault();
  const hash = e.target.hash;

  // scroll to the 'hash' variable, which will be different for every link 
  $('html,body').animate({
    scrollTop: $(hash).offset().top
  }, 'slow');
});
