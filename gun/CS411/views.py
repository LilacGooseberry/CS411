from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import connection
from django.db.models import Q
from django.http.request import HttpRequest
from django.http.response import HttpResponse
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

def search(req):  
    # if request.method = 'POST'
    ID = req.POST.get("Incident_id")
    print(ID)
    projects = 1
    city = 'Bad'
    state = 'Iowa' #kansas oregon
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Violence WHERE city = '"+city +"'"

        cursor.execute(sql)
        results = cursor.fetchall()
    
    print(results)
    # return render(req,'search.html',{'projects':projects})
    return render(req,'results.html',{'data':results})

def delete(req):
    ID = req.POST.get("Incident_id")
    print(ID)
    Incident_id = 1
    address = 'A'
    city = 'B'
    state = 'Iowa'
    with connection.cursor() as cursor:
        sql = "DELETE FROM Violence WHERE state = '"+state +"'"
        cursor.execute(sql)
    return render(req,'delete.html')

def update(req):
    ID = req.POST.get("Incident_id")
    print(ID)
    address = 'A'
    state = 'Iowa'
    with connection.cursor() as cursor:
        sql = "UPDATE Violence SET address = '"+address +"' WHERE state = '"+state +"'"
        cursor.execute(sql)
    return render(req,'update.html')

def insert(req):
    ID = req.POST.get("Incident_id")
    print(ID)
    Incident_id = 10034223
    address = 'A'
    city = 'Bad'
    state = 'C'
    with connection.cursor() as cursor:
            
        cursor.execute("INSERT INTO Violence values(%s,NULL, NULL, NULL, %s,NULL,NULL)",(Incident_id,city))
    return render(req,'insert.html')
