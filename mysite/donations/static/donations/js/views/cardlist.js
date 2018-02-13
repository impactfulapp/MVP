var app = app || {};

app.CardListView = Backbone.View.extend({
    el: '#cards',

    initialize: function( initialCards ) {
        this.collection = new app.CardList( initialCards );
        this.render();
        this.listenTo( this.collection, 'add', this.renderCard);
    },

    // render library by rendering each book in its collection
    render: function() {
        this.collection.each(function( item ) {
            this.renderCard( item );
        }, this );
    },

    // render a book by creating a BookView and appending the
    // element it renders to the library's element
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
        e.preventDefault();

        var formData = {};

        $( '#addCard div' ).children( 'input' ).each( function( i, el ) {
            if( $( el ).val() !== '' )
            {
                formData[ el.id ] = $( el ).val();
            }
        });

        this.collection.add( new app.Card( formData ) );
    },

});
