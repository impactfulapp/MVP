var app = app || {};

$(function() {
    var cards = [
      { charity_name: 'Against Melania Foundation', donation_amount: '10', donation_date: 'Dec 12 1920'},
      { charity_name: 'Salvation Army', donation_amount: '50', donation_date: 'Jan 19 1980'}
        // { title: 'JavaScript: The Good Parts', author: 'Douglas Crockford', releaseDate: '2008', keywords: 'JavaScript Programming' },
        // { title: 'The Little Book on CoffeeScript', author: 'Alex MacCaw', releaseDate: '2012', keywords: 'CoffeeScript Programming' },
        // // { title: 'Scala for the Impatient', author: 'Cay S. Horstmann', releaseDate: '2012', keywords: 'Scala Programming' },
        // // { title: 'American Psycho', author: 'Bret Easton Ellis', releaseDate: '1991', keywords: 'Novel Splatter' },
        // // { title: 'Eloquent JavaScript', author: 'Marijn Haverbeke', releaseDate: '2011', keywords: 'JavaScript Programming' }
    ];

    new app.CardListView( cards );
});
