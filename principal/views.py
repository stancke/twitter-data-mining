# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response
from django.http import HttpResponse
from api.api import Twitter
from pprint import pprint
from principal.models import *

def index(request):

    return render_to_response('index/index.html')

def grava_csv(request):
    
    caminho = '/home/stancke/Projetos/twitter-to-xml/arquivos/'
    arquivo = caminho + request.REQUEST.get('arquivo')
    tipo =  request.REQUEST.get('tipo')
    sentimento = request.REQUEST.get('sentimento')
    
    import csv
    with open(arquivo, 'rb') as csvfile:
        #spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            print row[2]
            if tipo == 'test':
                try:
                    td = TwitterTestDataEnglish(feed = row[2] )
                    td.save()
                except Exception as e:
                    print '%s (%s)' % (e.message, type(e))
                    
            if tipo == 'training':
                try:
                    tt = TwitterTrainingDataEnglish(id = row[1] , feed = row[0], sentiment = sentimento )
                    tt.save()
                except Exception as e:
                    print '%s (%s)' % (e.message, type(e))

    return HttpResponse("Gravado!")

def busca(request):

    busca = request.REQUEST.get('busca')
    t = Twitter()
    b = t.getBusca(busca)
    
    usuarios = []
    
    for aux in b:
        #pprint(vars(aux.author))
        #pprint(vars(aux))
        #exit()
        #usuario = t.getUserInformation(aux.id)
        
        user = {
                'profile_image_url':aux.author.profile_image_url,
                'from_user':aux.author.name,
                'text':aux.text,
                'tweet_created_at': aux.created_at,
                'geo':aux.geo,
		        'retweets': aux.retweet_count,
                'location':aux.author.location,
                'created_at':aux.author.created_at,
                'favourites_count':aux.author.favourites_count,
                'followers_count':aux.author.followers_count,
                'lang':aux.author.lang,
                'description':aux.author.description,
                'friends_count':aux.author.friends_count,
                'statuses_count':aux.author.statuses_count
        }
        
        usuarios.append(user)
        try:
            t = Tweets(
               usuarionome = aux.author.name,
               usuarioid =  aux.author.id_str,
               tweetdate = aux.created_at,
               text=aux.text,
               location  = aux.author.location,
               profilecreated  = aux.author.created_at,
               description  = aux.author.description,
               favorites  = aux.author.favourites_count,
               followers  = aux.author.followers_count,
               friends  = aux.author.friends_count,
               tweets  = aux.author.statuses_count,
               retweets  = aux.retweet_count,
               respostaastatusid = aux.in_reply_to_status_id_str,
               respostaausuarioid = aux.in_reply_to_user_id_str,
               idstatus = aux.id_str,
               origem = aux.source )
       
            t.save()
        except Exception as e:
            print '%s (%s)' % (e.message, type(e))
        
    request.session['resultados'] = usuarios
    return render_to_response('index/busca.html', {"busca": usuarios})

def gerar_xml(request):
    
    xml = "<?xml version='1.0' encoding='UTF-8'?>"
    xml = xml + '<principal>'
    xml = xml + '<resultados>'
    for res in request.session['resultados']:
        xml = xml + "<resultado>"
        xml = xml + "<nome>"+res['from_user']+"</nome>"
        xml = xml + "<frase>"+res['text']+"</frase>"
        xml = xml + "<tweetado_em>"+str(res['tweet_created_at'])+"</tweetado_em>"
        if res['geo'] != None:
            xml = xml + "<geo>"+res['geo']+"</geo>"
        xml = xml + "<perfil_criado>"+str(res['created_at'])+"</perfil_criado>"
        xml = xml + "<lingua>"+res['lang']+"</lingua>"
        xml = xml + "<descricao>"+res['description']+"</descricao>"
        xml = xml + "<favoritos>"+str(res['favourites_count'])+"</favoritos>"
        xml = xml + "<seguidores>"+str(res['followers_count'])+"</seguidores>"
        xml = xml + "<amigos>"+str(res['friends_count'])+"</amigos>"
        xml = xml + "<tweets>"+str(res['statuses_count'])+"</tweets>"
        xml = xml + "</resultado>"
    xml = xml + '</resultados>'
    xml = xml + '</principal>'
    response = HttpResponse(mimetype='text/xml')
    response.write(xml)
    response['Content-Disposition'] = 'attachment; filename=twitter.xml'
    
    return response
