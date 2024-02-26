    /* mv's notes:
       this is very shit bc i havent changed the 
       listener thing from enter key to
       space bar yet. im lazy.
    */

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  var count = 60;
  var timer = setInterval(update, 1000);
  var correct = 0;
  var wrong = 0;
  var totalChars = 0;

const words = [
    "apple", "banana", "orange", "grape", "kiwi", "pineapple", "strawberry", "blueberry", "watermelon", "peach",
    "carrot", "broccoli", "potato", "cucumber", "lettuce", "spinach", "tomato", "onion", "garlic", "pepper",
    "dog", "cat", "rabbit", "hamster", "goldfish", "parrot", "turtle", "snake", "lizard", "frog",
    "house", "apartment", "mansion", "cabin", "tent", "castle", "bungalow", "igloo", "villa", "condo",
    "car", "bicycle", "motorcycle", "bus", "train", "airplane", "helicopter", "boat", "ship", "submarine",
    "computer", "phone", "tablet", "television", "keyboard", "mouse", "monitor", "printer", "scanner", "laptop",
    "book", "newspaper", "magazine", "journal", "dictionary", "encyclopedia", "novel", "storybook", "textbook", "poetry",
    "music", "art", "painting", "sculpture", "photography", "dance", "theater", "film", "animation", "fashion",
    "sun", "moon", "star", "planet", "galaxy", "nebula", "comet", "asteroid", "meteor", "constellation",
    "football", "basketball", "soccer", "tennis", "volleyball", "golf", "baseball", "cricket", "rugby", "hockey",
    "school", "university", "college", "preschool", "kindergarten", "classroom", "library", "gymnasium", "cafeteria", "playground",
    "tree", "flower", "grass", "bush", "weed", "fern", "mushroom", "cactus", "succulent", "ivy","beach", "sandcastle", "seashell", "wave", 
    "surfboard", "sunscreen", "umbrella", "flip-flops", "snorkel", "palm", "mountain", "hiking", "campfire", "tent", "backpack", 
    "trail", "summit", "waterfall", "wildlife", "landscape", "coffee", "espresso", "latte", "cappuccino", 
    "mocha", "macchiato", "americano", "frappuccino", "decaf", "chai",
    "bicycle", "helmet", "pedal", "gear", "handlebar", "chain", "brake", "tire", "spoke", "bell",
    "pizza", "pasta", "lasagna", "spaghetti", "ravioli", "gnocchi", "penne", "fettuccine", "linguine", "cannelloni",
    "ocean", "whale", "dolphin", "shark", "octopus", "jellyfish", "coral", "seahorse", "starfish", "squid",
    "guitar", "piano", "violin", "drums", "trumpet", "flute", "saxophone", "accordion", "banjo", "ukulele",
    "sunny", "cloudy", "rainy", "windy", "stormy", "foggy", "snowy", "icy", "hot", "cold",
    "garden", "flowerbed", "greenhouse", "vegetable", "shrub", "perennial", "annual", "compost", "fertilizer", "mulch",
    "camera", "lens", "tripod", "flash", "memory", "shutter", "aperture", "focus", "zoom", "exposure",
    "passport", "visa", "boarding", "departure", "arrival", "customs", "immigration", "luggage", "baggage", "check-in",
    "chocolate", "vanilla", "strawberry", "caramel", "mint", "cookie", "brownie", "fudge", "marshmallow", "candy",
    "forest", "treehouse", "cabin", "campsite", "trail", "wildlife", "hiking", "birdwatching", "stream", "lake"
  ];


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


//askQuestion();

function getReturnVal() {
    return
    true;
}

console.log(getReturnVal())