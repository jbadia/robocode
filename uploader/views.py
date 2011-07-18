# -*- encoding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from robocode.uploader.models import *
from django.contrib import auth
from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory
from robocode.schedule.views import comprovar_submit
import shutil, os, glob, re

def change_basename(file_path, name):
    try:
        extensio = file_path.rsplit('.',1)[1]
        cami = file_path.rsplit(os.sep,1)[0]
        return cami + os.sep + name + '.' + extensio
    except:
        return file_path

def rename_file(file_path, name):
    try:
        new_file_path = change_basename(file_path, name)
        shutil.move(file_path, new_file_path)
        return new_file_path
    except: return file_path

def find_files_in_folder(nom, directori):
    match_list = []
    for fitxer in os.listdir(directori):
        try:
            math_list.append(re.search('^' + nom + '\..*$', fitxer).group())
        except: pass
    
    return match_list

def remove_previous_file(nom, categoria, directori='/home/mycode/robocode/files/submit'):
    file_find = nom + '_' + categoria
    for fitxer in find_files_in_folder(file_find, directori):
        os.remove(directori + os.sep + file_find)

def actions(request, method, model, value):
    """ Apply methods over models using values """
    if method == 'edit': pass
        #if model == 'submit':
        #    if request.POST:
        #        submit = Submit.objects.get(id = value)
        #        submit.category.clear()
        #        category_list = request.POST.getlist('category')
        #        for cat in category_list:
        #            submit.category.add(Category.objects.get(id = cat))
        #        submit.title=request.POST["title"]
        #        submit.comments=request.POST["comments"]
        #        try:
        #            submit.file=request.FILES['file']
        #        except:
        #            pass
        #        submit.save()
        #        
        #        return HttpResponseRedirect('/home/')
        #    else:
        #        user = User.objects.get(username=request.user.username)
        #        subm = Submit.objects.get(id = value)
        #        fitxer = str(subm.file).rsplit("/",1)[1]
        #        #index=0
        #        #cami = str(subm.file).split("/")
        #        #for directori in cami:
        #        #    if directori is '':
        #        #        fitxer = cami[index-1]
        #        #    index += 1
        #        cat = Category.objects.all()
        #        return render_to_response('uploader/edit_%s.html/' % model, locals())
        #else:
        #    return HttpResponse("chu chu!")

    elif method == 'del':
        if request.user.is_authenticated():
            user = User.objects.get(username = request.user.username)

        try:
            request.POST["confirm"]
        except:
            confirm = False
        else:
            confirm = True

        if confirm == False:
            if model == 'submit':
                element = Submit.objects.get(id=value)
            else:
                return HttpResponse("chu chu!")
            return render_to_response('uploader/del_confirm.html/', locals())
        else:
            if model == 'submit':
                element = Submit.objects.get(id=value).delete()
            else:
                return HttpResponse("chu chu!")
            return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/invalid/')

def add_model(request, model):
    """ Add models to user """
    user = User.objects.get(username = request.user.username)
            
    if model == "submit":
        if request.POST:
            
            usuari = User.objects.get(username = request.user.username)
            categoria = Category.objects.get(id=request.POST["category"])
            
            # obtenim el nom d'usuari i la categoria de l'actual submit
            nom_usuari = usuari.username
            nom_categoria = categoria.name
            
            # eliminem els fitxers anteriors de la mateixa categoria #1 submit x categoria
            #remove_previous_file(nom_usuari, nom_categoria)
            entrades_a_borrar = Submit.objects.filter(user=usuari, category=categoria)
            for entrada in entrades_a_borrar:
                try:
                    os.remove(str(entrada.file))
                except: pass
                entrada.delete()
            #Fala eliminar els anteriors submits de l'usuari per la mateixa categoria
            
            #fem el submit del formulari
            form = SubmitForm(request.POST, request.FILES)
            try:
                submit = form.save(commit=False)
            except ValueError:
                return render_to_response('uploader/add_%s.html' % model, locals())
            submit.user = User.objects.get(username = request.user.username)
            submit.save()
            
            # renombrem el fitxer un cop pujat, i li canviem el nom a la BD
            submit.file = rename_file(str(Submit.objects.get(id=submit.id).file), nom_usuari + '_' + nom_categoria)

            submit.save()
            
            return HttpResponseRedirect('/home/')
        else:
            if not comprovar_submit():
                return HttpResponseRedirect('/404/') 
            form = SubmitForm()
            categories = [ [tupla[0]+1, tupla[1]] for tupla in enumerate(Category.objects.all()) ]
            return render_to_response('uploader/add_%s.html' % model, locals())
    else:
        return HttpResponse('%s' % model)
