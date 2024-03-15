document.addEventListener("DOMContentLoaded", function() {
    let count = 59;
    let timer;
    let totalChars = 0;
    let wordsToType = [];
    let currentCategory = 'hard'; 
    let currentWordIndex = 0;
    let gameStarted = false;
    var correct = 0;
    var wrong = 0;
    var userInput = '';
    let currentWord;
    let spelling;

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
        document.getElementById("timer").innerText = '1' + ":" + '00';
        document.addEventListener('keydown', function(event) {
            if (!gameStarted) {
                startGame();
            } else {
                if (event.key === ' ') {
                    if (checkSpelling(userInput,currentWord)) {
                        correct++;
                        countChars(currentWord);
                    } else {
                        wrong++;
                    }
                    event.preventDefault();
                    var userInputField = document.getElementById('user-input');
                    userInputField.value = '';
                    document.getElementById("words").style.color = ""
                    advanceWord();
                }
            }
        });
    });

    document.getElementById('user-input').addEventListener('input', function() {
        
        modifyWord();
    });


    function startGame() {
        timer = setInterval(startTimer, 1000);
        gameStarted = true;
    }

    function displayWords() {
        
        currentWord = wordsToType[currentWordIndex];
        if (count > 0 && wordsToType.length > 0) {
            document.getElementById("words").textContent = currentWord;
        }
        
    }

    function modifyWord() {
        userInput = document.getElementById('user-input').value;
        spelling = checkSpelling(userInput, currentWord.substring(0, userInput.length));
        
        if (!spelling) {
            document.getElementById("words").style.color = "red";
        } else {
            document.getElementById("words").style.color = ""; 
        }

    }


    function advanceWord(){
        
        currentWordIndex +=1;
        displayWords();
    }

    
    function endGame() {
        document.getElementById("timer").innerText = calculateWPM();

        // will display this properly latr when we figure out where to put results
        gameStarted = false;
    }

    function countChars(word) {
        totalChars += word.length;
    }

    function calculateWPM() {
        return (totalChars / 5);
    }

    function checkSpelling(input,word) {
        
        if (input === word) {
            return true;
            
        } else {
            return false;
        }
    }
});
