var app = app || {};

app.AddCardView = Backbone.ModalView.extend({

	name: "AddCardView",
	model: "Card",
	templateHtml: _.template( $( '#modal-template' ).html() ),

	initialize: function() {
		_.bindAll(this, "render");
		//this.template = _.template( $( '#modal-template' ).html() );
	},

	events: {
		"submit form": "addCard"
	},

	getCurrentFormValues: function() {
		return {
			charity_name: $("#new_charity").val(),
			donation_amount: $("donation_amount").val(),
			donation_date: $("donation_date").val()
		};
	},

	addCard: function(e) {
		e.preventDefaul();

		if (this.model.set(this.getCurrentFormValues())) {
			this.hideModal();
			app.collection.add(this.model);
		}
	},

	render: function() {
		$(this.el).html(this.templateHtml);
		this.$form = {
			charity_name: this.$("#new_charity"),
			donation_amount: this.$("donation_amount"),
			donation_date: this.$("donation_date")
		}
		return this;
	}

})