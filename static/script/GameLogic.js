let count = 60;
let timer;

function startTimer() {
    let minutes = Math.floor(count/60);
    let seconds = count%60;

    if (seconds < 10) {
        seconds = '0' + seconds;
    }

    // write code to display on screen

    if (count === 0) {
        // end game
    } else {
        count--;
    }

    timer = setInterval(startTimer, 1000);
}



fetch('static/data/words.json')
    .then(response => response.json())
    .then(wordsToType => {
        document.addEventListener('keypress', function(event) {

            var charTyped = String.fromCharCode(event.which);


            if (charTyped === '\n' || charTyped === '\r') {
                //This should listen if they press enter
                startTimer();

            }
        });
    })