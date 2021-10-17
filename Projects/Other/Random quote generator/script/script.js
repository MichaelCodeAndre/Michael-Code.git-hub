var quotes = [
'Quote 1',
'Quote 2',
'Quote 3',
'Quote 4',
'Quote 5',
'Quote 6',
'Quote 7',
'Quote 8',
'Quote 9',
'Quote 10'
]
var voiceQuotes = [
    'sound1',
    'sound2',
    'sound3',
    'sound4',
    'sound5',
    'sound6',
    'sound7',
    'sound8',
    'sound9',
    'sound10'
]

//Fetched from the internet, used for playing/pausing.
var myAudio = document.getElementById('myAudio');
var isPlaying = false;

function togglePlay() {
    isPlaying ? myAudio.pause() : myAudio.play();
};

myAudio.onplaying = function() {
    isPlaying = true;
};

myAudio.onpause = function() {
    isPlaying = flase;
};
//end of fetched from internet.

function newQuote() {
    var randomNumber = Math.floor(Math.random() * (quotes.length));
    document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber];
}