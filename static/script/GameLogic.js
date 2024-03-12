let count = 60;
let timer;
let totalChars = 0;

// in case we feel like doing accuracy which we probably wont.
let correct = 0;
let wrong = 0;

function startTimer() {
    let minutes = Math.floor(count/60);
    let seconds = count%60;

    if (seconds < 10) {
        seconds = '0' + seconds;
    }

    // write code to display on screen
    document.getElementById("idkidonthaveatemplatetoworkwith").textContent = minutes + ":" + seconds;

    if (count === 0) {
        clearInterval(timer);
        endGame();
    } else {
        count--;
        // display next word
    }
 
}



fetch('static/data/words.json')
    .then(response => response.json())
    .then(wordsToType => {
        document.addEventListener('keypress', function(event) {

            var charTyped = String.fromCharCode(event.which);


            if (charTyped === '\n' || charTyped === '\r') {
                //This should listen if they press enter
                //startTimer();
                startGame();

            }
        });
    })


// answer is whatever the user types into the textbox
// 'word' is given word
function checkSpelling(answer, word) {
    if (answer === word) {
        correct++;
        countChars(randomWord);
    } else {
        wrong++;
    }
}
    

function startGame() {
    timer = setInterval(startTimer, 1000);
    // note to self and edu: write function to display words onto box


    /*while (count != 0) {
        checkSpelling(answer, word);
        startGame();
    }*/

}
         
function endGame() {
    // end game logic
    calculateWPM();
}


function getWord() {
    // get the current word from list of words in random order
}


// counts no. of chars for each correctly typed word
function countChars(word) {
    totalChars += word.length;
}

// formula for calculating wpm for a 1 min typing test
function calculateWPM() {
    return (totalChars / 5);
}