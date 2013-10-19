# -*- coding: utf-8 -*-
from django.db import models

class Tweets(models.Model):
    #id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=135, db_column='User', blank=True) # Field name made lowercase.
    text = models.CharField(max_length=240, db_column='Text', blank=True) # Field name made lowercase.
    tweetdate = models.CharField(max_length=135, db_column='TweetDate', blank=True) # Field name made lowercase.
    location = models.CharField(max_length=135, db_column='Location', blank=True) # Field name made lowercase.
    profilecreated = models.CharField(max_length=135, db_column='ProfileCreated', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=250, db_column='Description', blank=True) # Field name made lowercase.
    favorites = models.IntegerField(null=True, db_column='Favorites', blank=True) # Field name made lowercase.
    followers = models.IntegerField(null=True, db_column='Followers', blank=True) # Field name made lowercase.
    friends = models.IntegerField(null=True, db_column='Friends', blank=True) # Field name made lowercase.
    tweets = models.IntegerField(null=True, db_column='Tweets', blank=True) # Field name made lowercase.
    retweets = models.IntegerField(null=True, db_column='Retweets', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Tweets'

