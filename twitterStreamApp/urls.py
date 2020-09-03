from django.urls import path, include
from twitterStreamApp import views
# from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
        path("", views.index, name = "index"),
        path("getHashTag", views.getHashTag, name = "getHashTag"),
        path("getUserTweets", views.getUserTweets, name = "getUserTweets"),
        path("getHashTagInfo", views.getHashTagInfo, name = "getHashTagInfo"),
        path("getUserTweetInfo", views.getUserTweetInfo, name = "getUserTweetInfo"),

]
