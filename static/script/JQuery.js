$(".get-started-button").click(function() {

    window.onbeforeunload = () => {
        return "Are you sure you want to leave?";
    };
    $(this).animate({opacity: 0}, 100);
    $(this).css("margin-left", "1001px"); 
});
