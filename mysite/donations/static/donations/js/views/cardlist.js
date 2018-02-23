var app = app || {};

app.CardListView = Backbone.View.extend({
    el: '#cards',

    initialize: function( initialCards ) {
        this.collection = new app.CardList( initialCards );
        this.render();
        this.getTotalDonated();
        this.listenTo( this.collection, 'add', this.renderCard);
        this.listenTo( this.collection, 'destroy', this.getTotalDonated);
        this.listenTo( this.collection, 'change:donation_amount', this.getTotalDonated);
    },

    // render card list by rendering each card in its collection
    render: function() {
        this.collection.each(function( item ) {
            this.renderCard( item );
        }, this );
    },

    changeCard: function() {
        this.render();
        this.getTotalDonated();
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
    'click #add':'addCard',
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
        this.getTotalDonated();

        $.ajax( {
          url: 'add_donation/',
          dataType: 'json',
          data: dataJson, 
          success: function(data) {
            console.log(new_card.charity_name);
            console.log("added to backend");
            new_card.attributes.donation_id = data.donation_id;
            console.log(new_card);
          }
        });
    },

    getTotalDonated: function() {
        console.log("entered getTotalDonated");
        var total = 0;
        this.collection.each(function(item) {
            total = total + parseFloat(item.attributes.donation_amount);
        });
        console.log(total);
        var totalModel = new app.Total({total_amount: total});
        console.log(totalModel);
        this.renderTotal(totalModel);
    },

    renderTotal: function( item ) {
        console.log("entered renderTotal");
        var totalView = new app.TotalView({
            model: item
        });
        $('#footer').append(totalView.render().el);
    },


});
