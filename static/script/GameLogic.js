document.addEventListener("DOMContentLoaded", function() {
    let count = 59;
    let timer = null;
    let totalChars = 0;
    let wordsToType = [];
    let currentCategory = 'easy'; 
    let currentWordIndex = 0;
    let gameStarted = false;
    let timerStarted = false;

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
    }

    function displayWords() {
        
        if (count > 0 && wordsToType.length > 0) {
            let currentWord = wordsToType[currentWordIndex];
            document.getElementById("words").textContent = currentWord;
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
});
