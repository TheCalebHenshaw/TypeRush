var count = 60;
var timer = setInterval(update, 1000);
var correct = 0;
var wrong = 0;
var totalChars = 0;


// functions

function getRandomWord() {
    return words[Math.floor(Math.random() * words.length)];
}

function checkSpelling(answer, randomWord) {
    if (answer === randomWord) {
        correct++;
        countChars(randomWord);
    } else {
        wrong++;
        //console.log(wrong);
    }
}

function askQuestion() {
    const randomWord = getRandomWord();
    rl.question(randomWord + "\n", (answer) => {
        checkSpelling(answer, randomWord);
        if(count > 0) {
            askQuestion(); 
        }
        
    });
}

function update() {
    if (count > 0) {
        --count;
    } else {
        clearInterval(timer);
        rl.close(); 
        console.log("\n-----------");
        console.log("correct: " + correct);
        console.log("wrong: " + wrong);
        console.log(calculateWPM());
    }
}


function countChars(word) {
    totalChars += word.length;
}


function calculateWPM() {
    return (totalChars / 5);
}


askQuestion();
