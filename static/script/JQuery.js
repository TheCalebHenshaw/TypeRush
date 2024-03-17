$(".get-started-button").click(function() {

    
    $(this).animate({opacity: 0}, 100);
    $(this).css("margin-left", "1001px"); 
});

$("#logoutButton").on('click', function(event){
    window.onbeforeunload = () => {
        return "Are you sure you want to log out?";
    };
});
