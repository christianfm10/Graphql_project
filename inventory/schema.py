import graphene

from graphene_django.types import DjangoObjectType

from .models import Family , Location , Product , Transaction 

#from .models import Product ,Family ,Location ,Transaction  

class FamilyType(DjangoObjectType):
    class Meta:
        model = Family 

class LocationType(DjangoObjectType):
    class Meta:
        model = Location 

class ProductType(DjangoObjectType):
    class Meta:
        model = Product 

class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction


class Query(graphene.AbstractType):
    all_families = graphene.List(FamilyType)
    all_locations = graphene.List(LocationType)
    all_products = graphene.List(ProductType)
    all_transactions = graphene.List(TransactionType)
    
    product = graphene.Field(ProductType,id=graphene.Int())
    location = graphene.Field(LocationType,id=graphene.Int())
    family = graphene.Field(FamilyType,id=graphene.Int())

    def resolve_all_families(self, info):
        return Family.objects.all()

    def resolve_all_locations(self, info):
        return Location.objects.all()

    def resolve_all_products(self, info):
        return Product.objects.all()

    def resolve_all_transactions(self, info):
        return Transaction.objects.all()

    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Product.objects.get(pk=id)

        return None

    def resolve_family(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Family.objects.get(pk=id)

        return None

    def resolve_location(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Location.objects.get(pk=id)

        return None