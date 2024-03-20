function addRankSuffix(rank) {
    if (rank % 100 >= 11 && rank % 100 <= 13) {
        return rank + "th";
    }
    switch (rank % 10) {
        case 1:
            return rank + "st";
        case 2:
            return rank + "nd";
        case 3:
            return rank + "rd";
        default:
            return rank + "th";
    }
}

function showRanks() {
    // Get the elements containing ranks
    var easyRankElement = document.getElementById("easyRank");
    var mediumRankElement = document.getElementById("mediumRank");
    var hardRankElement = document.getElementById("hardRank");
    
    // Parse ranks to integers
    var easyRank = parseInt(easyRankElement.textContent.split(">>")[1]);
    var mediumRank = parseInt(mediumRankElement.textContent.split(">>")[1]);
    var hardRank = parseInt(hardRankElement.textContent.split(">>")[1]);
    
    // Add suffixes to ranks
    easyRankElement.textContent = "Easy >> " + addRankSuffix(easyRank) + " place";
    mediumRankElement.textContent = "Medium >> " + addRankSuffix(mediumRank) + " place";
    hardRankElement.textContent = "Hard >> " + addRankSuffix(hardRank) + " place";
}

function showRankLeaderBoard() {

    var rankElement = document.getElementById("rank");

    var rank = parseInt(rankElement.textContent.split(" ")[0]);

    rankElement.textContent = addRankSuffix(rank) + " Place";
}
