var app = app || {};

app.CardListView = Backbone.View.extend({
    el: '#cards',
    new_card: new app.Card(),

    initialize: function( initialCards ) {
        this.collection = new app.CardList( initialCards );
        this.render();
        this.listenTo( this.collection, 'add', this.renderCard);
    },

    // render card list by rendering each card in its collection
    render: function() {
        this.collection.each(function( item ) {
            this.renderCard( item );
        }, this );
    },

    // render a card by creating a CardView and appending the
    // element it renders to the card list's element
    renderCard: function( item ) {
        var cardView = new app.CardView({
            model: item
        });
        this.$el.append( cardView.render().el );
    },

    events: {
    'click #add':'addCard'
    },

    addCard: function( e ) {
        console.log("adding card");
        e.preventDefault();

        var formData = {};

        $( '#addCard div' ).children( 'input' ).each( function( i, el ) {
            if( $( el ).val() !== '' )
            {
                formData[ el.id ] = $( el ).val();
            }
        });
        new_card = new app.Card(formData);
        var card_name = new_card.attributes.charity_name;
        var card_amount = new_card.attributes.donation_amount;
        var card_date = new Date(new_card.attributes.donation_date)
        var card_date_py = new_card.attributes.donation_date;
        console.log(card_name);
        console.log(card_amount);
        console.log(card_date);
        console.log(new_card);
        console.log(card_date_py);
        dataJson = {'charity' : card_name, 'amount' : card_amount, 'date' : card_date_py};
        console.log(dataJson);

        this.collection.add( new_card );
        $.ajax( {
          url: 'add_donation/',
          dataType: 'json',
          data: dataJson, //{'charity' : card_name, 'amount' : card_amount, 'date' : card_date},
          success: function() {
            console.log(new_card.charity_name);
            console.log("added to backend");
          }
        });
    },

    returnCard: function() {
        return new_card;
    },

});
