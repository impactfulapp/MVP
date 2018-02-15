//var app = app || {};

console.log('entered app.js');
function init_donations(donations_list) {
    //var app = app || {};
    var cards = [];

    for (var donation in donations_list) {        //console.log("Inside the init_donations function");
        //var donation = element;
        var charity = donations_list[donation].donation_charity;
        var amount = donations_list[donation].donation_amount;
        var date = donations_list[donation].donation_date;
        console.log(donations_list[donation]);
        console.log(charity);
        console.log(amount);
        console.log(date);
        //console.log(donation.toJSON());
        cards.push({ charity_name: charity, donation_amount: amount, donation_date: date } );
    }

    new app.CardListView( cards );
    console.log('end of init_donations function')

    // var cards = [
    //   { charity_name: 'Against Melania Foundation', donation_amount: '10', donation_date: 'Dec 12 1920'},
    //   { charity_name: 'Salvation Army', donation_amount: '50', donation_date: 'Jan 19 1980'}
        // { title: 'JavaScript: The Good Parts', author: 'Douglas Crockford', releaseDate: '2008', keywords: 'JavaScript Programming' },
        // { title: 'The Little Book on CoffeeScript', author: 'Alex MacCaw', releaseDate: '2012', keywords: 'CoffeeScript Programming' },
        // // { title: 'Scala for the Impatient', author: 'Cay S. Horstmann', releaseDate: '2012', keywords: 'Scala Programming' },
        // // { title: 'American Psycho', author: 'Bret Easton Ellis', releaseDate: '1991', keywords: 'Novel Splatter' },
        // // { title: 'Eloquent JavaScript', author: 'Marijn Haverbeke', releaseDate: '2011', keywords: 'JavaScript Programming' }
    //];

    //new app.CardListView( cards );
}
