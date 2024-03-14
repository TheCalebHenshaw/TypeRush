document.addEventListener("DOMContentLoaded", function() {
    let count = 60;
    let timer;
    let totalChars = 0;
    let wordsToType = [];
    let currentCategory = 'easy'; 
    let currentWordIndex = 0;
    let gameStarted = false;
    var correct = 0;
    var wrong = 0;

    function startTimer() {
        let minutes = Math.floor(count / 60);
        let seconds = count % 60;

        if (seconds < 10) {
            seconds = '0' + seconds;
        }

        document.getElementById("timer").innerText = minutes + ":" + seconds;

        if (count === 0) {
            clearInterval(timer);
            endGame();
        } else {
            count--;
        }
    }

    fetch('/get-json-data/')
    .then(response => response.json())
    .then(data => {
        wordsToType = data[currentCategory]; 
        displayWords();
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Enter'){
                if (!gameStarted){
                    startGame();
                } else {
                    advanceWord();
                }
            }
        });
    });


    function startGame() {
        timer = setInterval(startTimer, 1000);
        gameStarted = true;
    }

    function displayWords() {
        
        let currentWord = wordsToType[currentWordIndex];
        if (count > 0 && wordsToType.length > 0) {
            document.getElementById("words").textContent = currentWord;
        }
        let spelling = checkSpelling(userWord, currentWord);
        
        if (spelling){
            $("words").css("color", "red");
        }

    }


    function advanceWord(){
        
        currentWordIndex +=1;
        displayWords();
    }

    
    function endGame() {
        
        calculateWPM();
        gameStarted = false;
    }

    function countChars(word) {
        totalChars += word.length;
    }

    function calculateWPM() {
        return (totalChars / 5);
    }

    function checkSpelling(answer, word) {
        if (answer === word) {
            correct++;
            return true;
            countChars(word);
        } else {
            wrong++;
            return false
        }
    }
});
