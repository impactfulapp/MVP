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
        'click .delete': 'deleteCard',
        'click .edit_button': 'edit',
        'click .save_edits': 'save'
        // 'dblclick .edit_space': 'edit',
        // 'keypress .edit': 'updateOnEnter',
        // 'blur .edit': 'close'
    },


    deleteCard: function() {
        //Delete model
        console.log(this.model);
        $.ajax( {
          url: 'delete_donation/',
          dataType: 'json',
          data: {'id': this.model.attributes.donation_id}, //{'charity' : card_name, 'amount' : card_amount, 'date' : card_date},
          success: function() {
            console.log("deleted from backend");
          }
        });

        this.model.destroy();

        //Delete view
        this.remove();
        //

    },

    edit: function() {
      // this.$el.addClass('editing');
      // this.$input.focus();
      console.log("entered edit function");
      this.template = _.template( $( '#editTemplate' ).html() );
      //autocomplete charity name input field
      
      this.render();

    },

    // Close the `"editing"` mode, saving changes to the todo.
    save: function() {
        console.log("entered save function");

      var formData = {};
      $( '.input_values div' ).children( 'input' ).each( function( i, el ) {
            console.log($(el).val());
            if( $( el ).val() !== '' )
            {
                formData[ el.id ] = $( el ).val();
            }
        });

      console.log(formData);
      console.log(this.model.attributes.donation_id);


      //this.model.attributes.donation_id = this.id;
      this.model.attributes.charity_name = formData["charity_name"];
      this.model.attributes.donation_amount = formData["donation_amount"];
      this.model.attributes.donation_date = formData["donation_date"];
      //this.model.save(formData);
      console.log(this.model.attributes);

      this.template = _.template( $( '#cardTemplate' ).html() );
      this.render();
        
      dataJson = this.model.attributes;

        //Update from backend
        $.ajax( {
          url: 'update_donation/',
          dataType: 'json',
          data: dataJson, //{'charity' : card_name, 'amount' : card_amount, 'date' : card_date},
          success: function() {
            //console.log(new_card.charity_name);
            console.log("updated in backend");
          }
        });

    },

    // If you hit `enter`, we're through editing the item.
    updateOnEnter: function( e ) {
      if ( e.which === ENTER_KEY ) {
        this.close();
      }
    }


});
