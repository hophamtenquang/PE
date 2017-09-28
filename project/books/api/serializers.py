from rest_framework import serializers

from .models import BxUsers, BxBooks, BxBookRatings


class BXUserSerializer(serializers.ModelSerializer):
    # posts = serializers.HyperlinkedIdentityField(view_name='userpost-list')

    class Meta:
        model = BxUsers
        fields = ('pk', 'user_id', 'location', 'age')


class BxBooksSerializer(serializers.ModelSerializer):
    # posts = serializers.HyperlinkedIdentityField(view_name='userpost-list')

    class Meta:
        model = BxBooks
        fields = '__all__'

class BxBookRatingsSerializer(serializers.ModelSerializer):
    author = BXUserSerializer(required=False)

    class Meta:
        model = BxBookRatings
        fields = '__all__'
