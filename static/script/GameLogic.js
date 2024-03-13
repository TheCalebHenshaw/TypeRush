document.addEventListener("DOMContentLoaded", function() {
    let count = 60;
    let timer;
    let totalChars = 0;

    // in case we feel like doing accuracy which we probably wont.
    let correct = 0;
    let wrong = 0;

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

    fetch('static/data/words.json')
        .then(response => response.json())
        .then(wordsToType => {
            document.addEventListener('keypress', function(event) {
                var charTyped = String.fromCharCode(event.which);
                if (charTyped === '\n' || charTyped === '\r') {
                    startGame();
                }
            });
        });


    function showTextBox() {
        document.getElementById("textbox-container").style.display = "block";
    }

    function startGame() {
        timer = setInterval(startTimer, 1000);
    }

    function displayWords() {
        if (count > 0) {
            // generate a random word or get a word from a list
            let currentWord;
            document.getElementById("we dont have a template to work with").textContent = currentWord;
        }
    }

    function endGame() {
        // end game logic
        calculateWPM();
        // send results to database and bring user to endscreen
    }

    function countChars(word) {
        totalChars += word.length;
    }

    function calculateWPM() {
        return (totalChars / 5);
    }
});
