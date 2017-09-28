from rest_framework import generics, status, views


from .serializers import BXUserSerializer, BxBooksSerializer, BxBookRatingsSerializer
from .models import BxUsers, BxBooks, BxBookRatings
from rest_framework.response import Response


class UserMixin(object):
    model = BxUsers
    queryset = BxUsers.objects.all()
    serializer_class = BXUserSerializer


class UserList(UserMixin, generics.ListCreateAPIView):
    pass


class UserDetail(UserMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'


class BookMixin(object):
    model = BxBooks
    queryset = BxBooks.objects.all()
    serializer_class = BxBooksSerializer


class BookList(BookMixin, generics.ListCreateAPIView):
    pass


class BookDetail(BookMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class BookRatingsMixin(object):
    model = BxBookRatings
    queryset = BxBookRatings.objects.all()
    serializer_class = BxBookRatingsSerializer


class BookRatingList(BookRatingsMixin, generics.ListAPIView):
    pass


class BookRatingDetail(BookRatingsMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class UserRatingsList(generics.ListAPIView):
    model = BxBookRatings
    queryset = BxBookRatings.objects.all()
    serializer_class = BxBookRatingsSerializer

    def get_queryset(self):
        queryset = super(UserRatingsList, self).get_queryset()
        return queryset.filter(author__pk=self.kwargs.get('pk'))
