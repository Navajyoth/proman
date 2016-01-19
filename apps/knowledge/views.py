import random

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .models import Article
from .models import Quote
from .serializers import ArticleSerializer
from .serializers import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()

    @list_route(methods=['GET'])
    def random(self, request):
        quote = random.choice(self.queryset.all())
        slz = QuoteSerializer(quote)
        return Response(slz.data)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
