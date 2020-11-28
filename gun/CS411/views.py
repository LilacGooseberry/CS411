from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import connection
from django.db.models import Q
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views import View
from . import forms
import folium
from mongoengine import *
import pymongo
import os
from datetime import datetime
import numpy as np
# Map
class FoliumView(TemplateView):
    template_name = "map.html"
class Violence(DynamicDocument):
    pass

def map(request):  
    # pass the data
    results = []
    form = forms.GetFrom2()
    Latitude = 40
    Longitude = -80
    results = []
    MONGODB_HOST = 'mongodb://127.0.0.1:27017'
    connect(db='CS411', host=MONGODB_HOST, 
        read_preference=pymongo.ReadPreference.PRIMARY_PREFERRED)

    

    if request.method == 'POST':
        form = forms.GetFrom2(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html = html + "The Form is Valid"
            print('success')
            Latitude = form.cleaned_data['latitude']
            Longitude = form.cleaned_data['longitude']


        sql = "select L.incident_id, L.latitude, L.longtitude, V.address, V.date, V.n_killed,V.source_url,P.participant_name\
              from Location L Natural Join Violence V Natural Join Participants P\
               where L.latitude >= "+str(Latitude-0.03)+" AND L.latitude <= "+str(Latitude+0.03)+" AND L.longtitude >= "+str(Longitude-0.03)+" AND L.longtitude <= "+str(Longitude+0.03)
               
        print(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()
            

            print(len(results))
    np_resultc = np.array(results)
    id_array = []
    for i in range(len(results)):
        id_array.append(int(results[i][0]))

    # for i in range(len(results)):
    v = Violence.objects(incident_id__in = id_array)
    source = []
    for i in v:
        source.append(i.soiurce_url)
        

    # draw the map
    m = folium.Map([Latitude, Longitude], zoom_start=10)
    for i in range(len(results)):
        popupString = "Address: "+str(results[i][3])+"<br> Date: "+str(results[i][4])+"<br> Killed: "+str(results[i][5])+"<br> source_url from mangoDB: "+str(source[i])+"<br> Participant Name: "+str(results[i][7])
        folium.Circle(radius = 40, location=[results[i][1], results[i][2]], popup=popupString).add_to(m)
        
    np_resultc = np.array(results)
    id_array = np_resultc[:,0]
    


    folium.Circle(radius = 100, color='#ED553B', location=[Latitude, Longitude], tooltip= str(len(np_resultc))+" accidents around from 2012 to 2018.").add_to(m)
    # np_resultc = np.array(results)

    m=m._repr_html_()
    context = {'map': m,'form': form}
    

    return render(request, 'map.html', context,)


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class SearchPageView(TemplateView):
    template_name = "search.html"

class InsertPageView(TemplateView):
    template_name = "insert.html"
    
class DeletePageView(TemplateView):
    template_name = "delete.html"
    
class UpdatePageView(TemplateView):
    template_name = "update.html"

class OutputPageView(TemplateView):
    template_name = "output.html"
    
class NoticePageView(TemplateView):
    template_name = "notice.html"

def regform(request):
    form = forms.GetFrom()
    if request.method == 'POST':
        form = forms.GetFrom(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html = html + "The Form is Valid"
            print(form)
    else:
        html = 'welcome for first time'
    return render(request, 'signup.html', {'html': html, 'form': form})

def search(request):  
    results = []
    form = forms.GetFrom()
    if request.method == 'POST':
        form = forms.GetFrom(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html = html + "The Form is Valid"
            print('success')
            Incident_id = form.cleaned_data['Incident_id']
            Address     = form.cleaned_data['Address']
            City        = form.cleaned_data['City']
            State       = form.cleaned_data['State'] 
            Date        = form.cleaned_data['Date']
            Death       = form.cleaned_data['Death']
            Report      = form.cleaned_data['Report']
            sql = "SELECT * FROM Violence WHERE "
            if Incident_id != '':
                sql = sql + "incident_id = '"+Incident_id+"'" 
            if Address != '':
                if sql.endswith("'"):
                    sql = sql + " AND address = '"+Address+"'" 
                else:
                    sql = sql + " address = '"+Address+"'" 
            if City != '':
                if sql.endswith("'"):
                    sql = sql + " AND city = '"+City+"'" 
                else:
                    sql = sql + " city = '"+City+"'" 
            if State != '':
                if sql.endswith("'"):
                    sql = sql + " AND state = '"+State+"'" 
                else:
                    sql = sql + " state = '"+State+"'" 

            if Death != '':
                if sql.endswith("'"):
                    sql = sql + " AND n_killed = '"+Death+"'"               
                else:
                    sql = sql + " n_killed = '"+Death+"'" 
            if Report != '':
                if sql.endswith("'"):
                    sql = sql + " AND source_url = '"+Report+"'" 
                else:
                    sql = sql + " source_url = '"+Report+"'" 
            print(sql)
            with connection.cursor() as cursor:

                cursor.execute(sql)
                results = cursor.fetchall()
          
    else:
        html = 'welcome for first time'
    return render(request, 'search.html', {'html': html, 'form': form,'data':results})




def delete(request):

    form = forms.GetFrom()
    if request.method == 'POST':
        form = forms.GetFrom(request.POST)
        html = 'we have recieved this form again '
        if form.is_valid():
            html = html + "The Form is Valid"
            print('success')
            print(type(form))
            Incident_id = form.cleaned_data['Incident_id']
            Address     = form.cleaned_data['Address']
            City        = form.cleaned_data['City']
            State       = form.cleaned_data['State']
            Date        = form.cleaned_data['Date']
            Death       = form.cleaned_data['Death']
            Report      = form.cleaned_data['Report']
            sql = "DELETE FROM Violence WHERE "
            if Incident_id != '':
                sql = sql + "incident_id = '"+Incident_id+"'" 
            if Address != '':
                if sql.endswith("'"):
                    sql = sql + " AND address = '"+Address+"'" 
                else:
                    sql = sql + " address = '"+Address+"'" 
            if City != '':
                if sql.endswith("'"):
                    sql = sql + " AND city = '"+City+"'" 
                else:
                    sql = sql + " city = '"+City+"'" 
            if State != '':
                if sql.endswith("'"):
                    sql = sql + " AND state = '"+State+"'" 
                else:
                    sql = sql + " state = '"+State+"'" 

            if Death != '':
                if sql.endswith("'"):
                    sql = sql + " AND n_killed = '"+Death+"'"               
                else:
                    sql = sql + " n_killed = '"+Death+"'" 
            if Report != '':
                if sql.endswith("'"):
                    sql = sql + " AND source_url = '"+Report+"'" 
                else:
                    sql = sql + " source_url = '"+Report+"'" 
            with connection.cursor() as cursor:

                cursor.execute(sql)
                results = cursor.fetchall()
                print(results)
    else:
        html = 'welcome for first time'
    return render(request, 'delete.html', {'html': html, 'form': form})

def update(request):
    form = forms.GetFrom()
    if request.method == 'POST':
        form = forms.GetFrom(request.POST)
        html = 'we have recieved this form again '
        if form.is_valid():
            html = html + "The Form is Valid"
            print('success')
            Incident_id = form.cleaned_data['Incident_id']
            Address     = form.cleaned_data['Address']
            City        = form.cleaned_data['City']
            State       = form.cleaned_data['State']
            Date        = form.cleaned_data['Date']
            Death       = form.cleaned_data['Death']
            Report      = form.cleaned_data['Report']

            sql = "UPDATE Violence SET "
            
            if Address != '':
                    sql = sql + " address = '"+Address+"'" 
            if City != '':
                if sql.endswith("'"):
                    sql = sql + " ,city = '"+City+"'" 
                else:
                    sql = sql + "  city = '"+City+"'" 
            if State != '':
                if sql.endswith("'"):
                    sql = sql + " ,state = '"+State+"'" 
                else:
                    sql = sql + " state = '"+State+"'" 
            if Death != '':
                if sql.endswith("'"):
                    sql = sql + " ,n_killed = '"+Death+"'"               
                else:
                    sql = sql + " n_killed = '"+Death+"'" 
            if Report != '':
                if sql.endswith("'"):
                    sql = sql + " ,source_url = '"+Report+"'" 
                else:
                    sql = sql + " source_url = '"+Report+"'" 

            sql += " WHERE incident_id = '"+Incident_id+"' "
            print(sql)
            with connection.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                print(type(results))
    else:
        html = 'welcome for first time'
    return render(request, 'update.html', {'html': html, 'form': form})

def insert(request):
    form = forms.GetFrom()
    if request.method == 'POST':
        form = forms.GetFrom(request.POST)
        html = 'we have recieved this form again '
        if form.is_valid():
            html = html + "The Form is Valid"
            print('success')
            Incident_id = form.cleaned_data['Incident_id']
            Address     = form.cleaned_data['Address']
            City        = form.cleaned_data['City']
            State       = form.cleaned_data['State']
            Date        = form.cleaned_data['Date']
            Death       = form.cleaned_data['Death']
            Report      = form.cleaned_data['Report']
            sql = """INSERT INTO Violence values (%s,%s,%s,%s,%s,%s,%s)"""
            
            with connection.cursor() as cursor:
                recordTuple = (Incident_id, Address,City, State, Date, Death, Report)
                print(sql,recordTuple)
                cursor.execute(sql,recordTuple)
                results = cursor.fetchall()
                print(type(results))
    else:
        html = 'welcome for first time'
    return render(request, 'insert.html', {'html': html, 'form': form})

# def map(request):
#     mapbox_access_token = 'pk.my_mapbox_access_token'
#     return render(request, 'map.html', 
#                   { 'mapbox_access_token': mapbox_access_token })






# def search(req):  
#     # if request.method = 'POST'
#     ID = req.POST.get("Incident_id")
#     print(ID)
#     projects = 1
#     city = 'Bad'
#     state = 'kansas' #kansas oregon
#     with connection.cursor() as cursor:
#         sql = "SELECT * FROM Violence WHERE city = '"+city +"'"

#         cursor.execute(sql)
#         results = cursor.fetchall()
    
#     print(results)
#     # return render(req,'search.html',{'projects':projects})
#     return render(req,'results.html',{'data':results})

# def delete(req):
#     ID = req.POST.get("Incident_id")
#     print(ID)
#     Incident_id = 1
#     address = 'A'
#     city = 'B'
#     state = 'kansas'
#     with connection.cursor() as cursor:
#         sql = "DELETE FROM Violence WHERE state = '"+state +"'"
#         cursor.execute(sql)
#     return render(req,'delete.html')

# def update(req):
#     ID = req.POST.get("Incident_id")
#     print(ID)
#     address = 'A'
#     state = 'Iowa'
#     with connection.cursor() as cursor:
#         sql = "UPDATE Violence SET address = '"+address +"' WHERE state = '"+state +"'"
#         cursor.execute(sql)
#     return render(req,'update.html')

# def insert(req):
#     ID = req.POST.get("Incident_id")
#     print(ID)
#     Incident_id = 10034234
#     address = 'A'
#     city = 'Bad'
#     state = 'C'
#     with connection.cursor() as cursor:
            
#         cursor.execute("INSERT INTO Violence values(%s,NULL, NULL, NULL, %s,NULL,NULL)",(Incident_id,city))
#     return render(req,'insert.html')
