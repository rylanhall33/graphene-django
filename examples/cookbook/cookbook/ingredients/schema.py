from cookbook.ingredients.models import Category, Ingredient
from graphene import ObjectType, Field, AbstractType, Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):

    class Meta:
        model = Category
        interfaces = (Node, )
        filter_fields = ['name', 'ingredients']
        filter_order_by = ['name']


class IngredientNode(DjangoObjectType):

    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        interfaces = (Node, )
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        filter_order_by = ['name', 'category__name']


class Query(AbstractType):
    category = Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)
