import urllib2
from rest_framework import serializers
from bs4 import BeautifulSoup
from django.utils import timezone

from .models import Quote, Article
from .parser import ParseData


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = ('id', 'author', 'text')


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'url', 'title', 'image_url', 'tags', 'short_description', 'user', 'date')
        read_only_fields = ('title', 'image_url', 'tags', 'short_description', 'user', 'date')

    def create(self, validated_data):
        if self.context['request'].user:
            validated_data['user'] = self.context['request'].user
        self.item = super(ArticleSerializer, self).create(validated_data)
        data_parser = ParseData(self.item)
        data_parser.update_article()
        self.item.send_mail()
        return self.item
