from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from store.models import Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        permission_classes = [IsAuthenticatedOrReadOnly]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('url', 'title', 'author', 'description', 'publish_date', 'price', 'stock', 'year')
        permission_classes = [IsAuthenticatedOrReadOnly]