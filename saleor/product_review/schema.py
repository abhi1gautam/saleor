import graphene
from graphene_django import DjangoObjectType

from saleor.product_review.models import ProductReview

class Review(DjangoObjectType):
    class Meta:
        model= ProductReview


class Query(graphene.ObjectType):
    all_reviews = graphene.List(Review)

    def resolve_all_reviews(root, info):
        return ProductReview.objects.all()

schema = graphene.Schema(query=Query)
