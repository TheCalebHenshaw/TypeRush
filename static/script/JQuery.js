$(document).ready(function() {
    $(".get-started-button").click(function() {
        $(this).animate({opacity: 0}, 100);
        $(this).css("margin-left", "1001px"); 
    });

    var logoutButton = document.getElementById('logoutButton');

    if (logoutButton && !logoutButton.hasEventListener) {
        logoutButton.hasEventListener = true; 
        logoutButton.addEventListener('click', function(event) {
            if (!confirm('Are you sure you want to logout?')) {
                event.preventDefault();
                event.stopPropagation(); 
            }
        });
    }
});