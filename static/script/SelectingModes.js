$(document).ready(function(){
    // Event listener for mode buttons
    $(".selectMode").click(function(){

         // Remove 'selected' class from all buttons
         $(".selectMode").removeClass("selected");
         // Add 'selected' class to the clicked button
         $(this).addClass("selected");

        var mode = $(this).data("mode");
        $.ajax({
            url: "/typerush/update_leaderboard/",
            type: "POST",
            data: {
                'mode': mode
            },
            success: function(response){
                updateLeaderboard(response, mode);
            },
            error: function(xhr, status, error){
                console.error(error);
            }
        });
    });

    // Function to update the leaderboard
    function updateLeaderboard(response, mode) {
        var leaderboardBody = $("#leaderboard tbody");
        leaderboardBody.empty(); // Clear the existing leaderboard content
        // Append the new leaderboard data to the DOM
        $.each(response.top_games, function(index, game){
            console.log(game.user.profile_picture)
            leaderboardBody.append(
                `<tr>
                    <td>${index + 1}</td>
                    <td><img src="${MEDIA_URL}${game.profile_picture}" alt="profile-img"/> ${game.user}</td>
                    <td>${game.score}</td>
                </tr>`
            );
        });
        var rankElement = $("#rank");
        rankElement.empty(); // Clear the existing rank
        // Append the new rank
        rankElement.append(response.rank)
        showRankLeaderBoard()

        var scoreElement = $("#score");
        scoreElement.empty(); // Clear the existing score
        // Append the new score
        scoreElement.append(response.score + " WPM")

    }
});