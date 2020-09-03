from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from twitterStreamApp import templates
from django.http.response import JsonResponse

import json
import requests
import oauth2 as oauth
from .apps import TwitterstreamappConfig
#index page
def index(request):
    return render(request, "index.html", context = None)

def getHashTag(request):
    return render(request, "getHashTag.html", context = None)

def getUserTweets(request):
    return render(request, "getUserTweets.html", context = None)

def call_twitter_api(endpoint):
    oauth_consumer = oauth.Consumer(key=TwitterstreamappConfig.consumer_key, secret=TwitterstreamappConfig.consumer_secret)
    oauth_token = oauth.Token(key=TwitterstreamappConfig.access_token, secret=TwitterstreamappConfig.access_token_secret)
    client = oauth.Client(oauth_consumer, oauth_token)
    response, data = client.request(endpoint)

    return response, json.loads(data)

# def get_user_tweets(request):
#
#     timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Seekers Tweet&count=20"
#     resp, tweets = call_twitter_api(timeline_endpoint)
#     context = {'tweet': tweets}
#     if resp.status != 200:
#         print("status exception get_user_tweets", resp.status)
#         return HttpResponseServerError(twitter_exception)
#     else:
#         print("status working get_user_tweets", resp.status)
#         return render(request, 'TwitterApi/getusertweet.html', context)
#
# def get_id_based_tweets(request):
#     timeline_endpoint = "https://api.twitter.com/1.1/statuses/show.json?id=1049869614321000448"
#     resp, id_tweets = call_twitter_api(timeline_endpoint)
#
#     # print('\nTweet Id : ', id_tweets['id'], '\nTweet : ', id_tweets['text'], '\nTweet ScreenName : ',
#     #       id_tweets['user']['screen_name'], '\nTweet Created At : ', id_tweets['user']['created_at'])
#     context = {'id_tweet': id_tweets}
#     if resp.status != 200:
#         print("status exception get_id_based_tweets", resp.status)
#         return HttpResponseServerError(twitter_exception)
#     else:
#         print("status working get_id_based_tweets", resp.status)
#         return render(request, 'TwitterApi/getidbasedtweet.html', context)

def getHashTagInfo(request):
    # https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular
    if request.method == 'POST':
        hashTag = request.POST.get('hashTag', None)
        timeline_endpoint = "https://api.twitter.com/1.1/search/tweets.json?q="+hashTag+"&result_type=popular"
        resp, tweets = call_twitter_api(timeline_endpoint)




    return JsonResponse({"tweet" : tweets})

def getUserTweetInfo(request):
    if request.method == 'POST':
        userId = request.POST.get('userId', None)
        timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+userId+"&count=20"
        resp, tweets = call_twitter_api(timeline_endpoint)
        return JsonResponse({'tweet': tweets})
