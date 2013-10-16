# -*- coding: utf-8 -*-
from django.db import models
import MySQLdb

# Create your models here.
class Tweets(object):

    def insert(self, user):
	db = MySQLdb.connect(host="localhost",user="admin",passwd="",db="test")
        cur = db.cursor()

	#print "INSERT INTO Tweets ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')" . format(user['from_user'], user['text'], user['tweet_created_at'], user['location'], user['created_at'], user['description'], user['favourites_count'], user['followers_count'], user['friends_count'], user['statuses_count'], user['retweets'])

	sql = ''
	try:
	    cur.execute(sql)
	    db.commit()
	except:
            db.rollback()
	    print "Erro ao inserir registro no banco!"
    
        db.close()
