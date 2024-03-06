$(document).ready(function() {
    window.onbeforeunload = function() {
        return "Are you sure you want to leave?";
    };

    $(".get-started-button").click(function() {
        $(this).animate({opacity: 0}, 100);
        $(this).css("margin-left", "1000px"); 
    });
});
