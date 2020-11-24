from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import connection
from django.db.models import Q
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views import View
from . import forms
        
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
            with connection.cursor() as cursor:
                sql = "SELECT * FROM Violence \
                    WHERE city = '"+City+"'"
                cursor.execute(sql)
                results = cursor.fetchall()
                print(results)
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
            with connection.cursor() as cursor:
                sql = "DELETE FROM Violence \
                    WHERE state = '"+State+ "'"
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
            with connection.cursor() as cursor:
                sql = "UPDATE Violence \
                    SET address = '"+Address+"'\
                    WHERE city = '"+City+"'"

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
            print(type(State))
            with connection.cursor() as cursor:
                sql = """INSERT INTO Violence values (%s,NULL, NULL, NULL, %s,NULL,NULL)"""
                recordTuple = (Incident_id,City)
                print(sql,recordTuple)
                cursor.execute(sql,recordTuple)
                results = cursor.fetchall()
                print(type(results))
    else:
        html = 'welcome for first time'
    return render(request, 'insert.html', {'html': html, 'form': form})


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
