from django.conf.urls import url, include

from .api import UserList, UserDetail, BookList, BookDetail, BookRatingList, BookRatingDetail
# from .api import PostList, PostDetail, PostImageList
# from .api import ImageList, ImageDetail, ImageAPIView

user_urls = [
    url(r'^$', UserList.as_view(), name='user-list'),
    url(r'^/(?P<pk>\d+)$', UserDetail.as_view(), name='user-detail'),
]

book_urls = [
    url(r'^$', BookList.as_view(), name='book-list'),
    url(r'^/(?P<pk>\d+)$', BookDetail.as_view(), name='book-detail'),
]

book_rating_urls = [
    url(r'^$', BookRatingList.as_view(), name='book-rating-list'),
    url(r'^/(?P<pk>\d+)$', BookRatingDetail.as_view(), name='book-rating-detail'),
]

urlpatterns = [
    url(r'^users', include(user_urls)),
    url(r'^books', include(book_urls)),
    url(r'^book-ratings', include(book_rating_urls)),
]
