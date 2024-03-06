let count = 60;
let timer;


function startTimer() {
    timer = setInterval(update, 1000);
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