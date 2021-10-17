var quotes = ['This is the first quote.',
'This is the second quote.', 
'This is the third quote.', 
'I wanna do more coding it\'s so cool.']

function newQuote() {
    var randomNumber = Math.floor(Math.random() *(quotes.lenght));
    document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber];
}