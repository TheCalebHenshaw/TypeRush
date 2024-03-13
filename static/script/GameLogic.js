document.addEventListener("DOMContentLoaded", function() {
    let count = 60;
    let timer;
    let totalChars = 0;
    let wordsToType = [];
    let currentCategory = 'easy'; 

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

    fetch('../data/words.json')
    .then(response => response.json())
    .then(data => {
        wordsToType = data[currentCategory]; 
        displayWords();
        document.addEventListener('keypress', function(event) {
            var charTyped = String.fromCharCode(event.which);
            if (charTyped === '\n' || charTyped === '\r') {
                startGame();
            }
        });
    });


    function startGame() {
        timer = setInterval(startTimer, 1000);
    }

    function displayWords() {
        if (count > 0 && wordsToType.length > 0) {
            let currentWord = wordsToType[Math.floor(Math.random() * wordsToType.length)];
            document.getElementById("words").textContent = currentWord;
        }
    }

    function endGame() {
        calculateWPM();
    }

    function countChars(word) {
        totalChars += word.length;
    }

    function calculateWPM() {
        return (totalChars / 5);
    }
});
