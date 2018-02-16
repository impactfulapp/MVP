var app = app || {};

console.log('entered card.js');

app.Card = Backbone.Model.extend({
    defaults: {
        donation_id: '',
        charity_name: 'No title',
        donation_amount: '0',
        donation_date: new Date(0),
    }
});
