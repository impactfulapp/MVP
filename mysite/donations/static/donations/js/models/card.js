var app = app || {};

app.Card = Backbone.Model.extend({
    defaults: {
        charity_name: 'No title',
        donation_amount: '0',
        donation_date: 'Unknown',
    }
});
