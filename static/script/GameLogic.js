document.addEventListener("DOMContentLoaded", function() {
    let count = 59;
    let timer;
    let totalChars = 0;
    let wordsToType = [];
    let currentCategory = 'easy'; 
    let currentWordIndex = 0;
    let gameStarted = false;
    let correct = 0;
    let wrong = 0;
    let userInput = '';
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

    $(".selectMode").click(function(){
        if (gameStarted) {
            alert("you cannot change difficulty mid-game, sorry :)");
            return;
        }

        $(".selectMode").removeClass('selected');
        $(this).addClass('selected');
        let mode = $(this).data("mode");
        currentCategory = mode;
        getData('/get-json-data/');
    })

    function getData(url) {
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                'mode': currentCategory
            },
            success: function(data) {
                wordsToType = data[currentCategory];
                displayWords();
                document.getElementById("timer").innerText = '1' + ":" + '00';
    
                // Event listener for keyboard input
                document.addEventListener('keydown', function(event) {
                    if (!gameStarted) {
                        startGame();
                        window.onbeforeunload = () => {
                            return "Are you sure you want to leave?";
                        };
                    } else {
                        if (event.key === ' ') {
                            if (checkSpelling(userInput, currentWord)) {
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
            },
            error: function(xhr, status, error) {
                console.error('Error fetching JSON data:', error);
            }
        });
    }

    getData('/get-json-data/');

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
        gameStarted = false;
        hideStuff();
        displayResults();

        $.ajax({
            url: '/save_game_results/', 
            type: 'POST',
            data: {
                correct: correct,
                wrong: wrong
            },
            success: function(response) {
                console.log('Results saved successfully', response);
            },
            error: function(xhr, status, error) {
                console.error('Error saving results:', error);
            }
        });
    }

    function countChars(word) {
        totalChars += word.length;
    }

    function calculateWPM() {
        return (totalChars / 5);
    }

    function checkSpelling(input, word) {
        return input === word;
    }

    function hideStuff() {
        document.getElementById("time").style.display = "none";
        document.getElementById("title").style.display = "none";
        document.getElementById("game").style.display = "none";
        var elements = document.getElementsByClassName("select-mode");
            for (var i = 0; i < elements.length; i++) {
                elements[i].style.display = "none";
            }
    }

    function displayResults() {
        const scoreElement = document.querySelector('.score');
        scoreElement.style.display = 'block';
        document.getElementById("wpm").innerText = calculateWPM() + " wpm";
        document.getElementById("accuracy").innerText = calculateAccuracy() + "%";
    }

});
