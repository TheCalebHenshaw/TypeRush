$(document).ready(function(){
    var mode;

    $(".selectMode").click(function(){
        $(".selectMode").removeClass('selected');
        $(this).addClass('selected');
        $(".submit-mode").show();
        mode = $(this).data("mode");

        $("h4").text("you selected " + mode);
    });

    $(".submit-mode").click(function(){
        // Make the AJAX request
        $.ajax({
            url: "/typerush/game/",
            type: "POST",
            data: {
                'mode': mode
            },
            success: function(response){
                
            },
            error: function(xhr, status, error){
                console.error(error);
            }
        });
    });
});
