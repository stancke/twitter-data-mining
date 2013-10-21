# -*- coding: utf-8 -*-
from django.db import models

class Tweets(models.Model):
    id = models.IntegerField(primary_key=True)
    usuarioid = models.BigIntegerField(null=True, db_column='UsuarioID', blank=True) # Field name made lowercase.
    usuarionome = models.CharField(max_length=1500, db_column='UsuarioNome', blank=True) # Field name made lowercase.
    text = models.CharField(max_length=1500, db_column='Text', blank=True) # Field name made lowercase.
    tweetdate = models.DateTimeField(null=True, db_column='TweetDate', blank=True) # Field name made lowercase.
    location = models.CharField(max_length=1500, db_column='Location', blank=True) # Field name made lowercase.
    profilecreated = models.CharField(max_length=1500, db_column='ProfileCreated', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1500, db_column='Description', blank=True) # Field name made lowercase.
    origem = models.CharField(max_length=1500, db_column='Origem', blank=True) # Field name made lowercase.
    favorites = models.IntegerField(null=True, db_column='Favorites', blank=True) # Field name made lowercase.
    followers = models.IntegerField(null=True, db_column='Followers', blank=True) # Field name made lowercase.
    friends = models.IntegerField(null=True, db_column='Friends', blank=True) # Field name made lowercase.
    tweets = models.IntegerField(null=True, db_column='Tweets', blank=True) # Field name made lowercase.
    retweets = models.IntegerField(null=True, db_column='Retweets', blank=True) # Field name made lowercase.
    respostaastatusid = models.BigIntegerField(null=True, db_column='RespostaAStatusID', blank=True) # Field name made lowercase.
    respostaausuarioid = models.BigIntegerField(null=True, db_column='RespostaAUsuarioID', blank=True) # Field name made lowercase.
    idstatus = models.BigIntegerField(null=True, db_column='IDStatus', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Tweets'
        
        
class TwitterTestDataEnglish(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    feed = models.TextField(db_column='Feed', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Twitter_Test_Data_English'

class TwitterTrainingDataEnglish(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    feed = models.TextField(db_column='Feed', blank=True) # Field name made lowercase.
    sentiment = models.CharField(max_length=765, db_column='Sentiment', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Twitter_Training_Data_English'