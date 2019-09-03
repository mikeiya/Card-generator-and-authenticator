from django.contrib.auth.models import Card
from rest_framework import serializers

"""
serializer for our data representations
"""
class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ['user_id', 'card_number','validity','vendor']
