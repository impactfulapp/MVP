var app = app || {};

app.TotalView = Backbone.View.extend({ 
    el: '.footer',
    template: _.template( $( '#totalTemplate' ).html() ),

    initialize: function() {
        this.render();
    },

    render: function() {
        console.log("entered total render");

        //this.el is what we defined in tagName. use $el to get access to jQuery html() function
        this.$el.html( this.template( this.model.attributes ) );

        return this;
    },

});
