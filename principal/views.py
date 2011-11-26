# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response
from django.http import HttpResponse
from api.api import Twitter

def index(request):

    return render_to_response('index/index.html')

def busca(request):

    busca = request.REQUEST.get('busca')
    t = Twitter()
    b = t.getBusca(busca)
    
    usuarios = []
    
    for aux in b:
        usuario = t.getUserInformation(aux.from_user_id)
        
        user = {
                'profile_image_url':aux.profile_image_url,
                'from_user':aux.from_user,
                'text':aux.text,
                'geo':aux.geo,
                'location':usuario.location,
                'created_at':usuario.created_at,
                'favourites_count':usuario.favourites_count,
                'followers_count':usuario.followers_count,
                'lang':usuario.lang,
                'description':usuario.description,
                'friends_count':usuario.friends_count,
                'statuses_count':usuario.statuses_count
        }
        
        usuarios.append(user)
        print 1
        
    request.session['resultados'] = usuarios
    return render_to_response('index/busca.html', {"busca": usuarios})

def gerar_xml(request):
    
    xml = "<?xml version='1.0' encoding='UTF-8'?>"
    xml = xml + '<principal>'
    xml = xml + '<resultados>'
    for res in request.session['resultados']: 
        xml = xml + "<resultado nome='"+res.from_user+"'>"+res.text+"</resultado>"
    xml = xml + '</resultados>'
    xml = xml + '</principal>'
    response = HttpResponse(mimetype='text/xml')
    response.write(xml)
    response['Content-Disposition'] = 'attachment; filename=unruly.xml'
    
    return response

