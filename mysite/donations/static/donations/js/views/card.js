var app = app || {};

app.CardView = Backbone.View.extend({ 
    tagName: 'div',
    className: 'cardContainer',
    template: _.template( $( '#cardTemplate' ).html() ),

    render: function() {
        //this.el is what we defined in tagName. use $el to get access to jQuery html() function
        this.$el.html( this.template( this.model.attributes ) );

        return this;
    },

    events: {
        'click .delete': 'deleteCard'
    },

    deleteCard: function() {
        //Delete model
        this.model.destroy();

        //Delete view
        this.remove();
    },
});
