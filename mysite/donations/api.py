from tastypie.resources import ModelResource
from .models import Card

class CardResource(ModelResource):
    class Meta:
        queryset = Card.objects.all()
        resource_name = 'card'
        # excludes = ["product_type", "price"]
        # allowed_methods = ['get']
        # authentication = CustomApiKeyAuthentication()
    #
    # def dehydrate(self, bundle):
    #     bundle.data["name"] = bundle.data["name"].upper()
    #     return bundle


# class OrderResource(ModelResource):
#     class Meta:
#         queryset = Order.objects.all()
#         resource_name = 'order'
#         allowed_methods = ['get', 'post', 'put']
#         authentication = CustomApiKeyAuthentication()
