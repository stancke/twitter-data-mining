# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response
from django.http import HttpResponse
from api.api import Twitter
from pprint import pprint

def index(request):

    return render_to_response('index/index.html')

def busca(request):

    busca = request.REQUEST.get('busca')
    t = Twitter()
    b = t.getBusca(busca)
    
    usuarios = []
    
    for aux in b:
	#pprint(vars(aux.author))

        #usuario = t.getUserInformation(aux.id)
        
        user = {
                'profile_image_url':aux.author.profile_image_url,
                'from_user':aux.author.name,
                'text':aux.text,
                'tweet_created_at': aux.created_at,
                'geo':aux.geo,
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
        print 'OK!'
        
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

