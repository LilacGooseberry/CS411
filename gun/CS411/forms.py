from django import forms

#DataFlair #Form
class GetFrom(forms.Form):
    Incident_id = forms.CharField(required = False)
    Address     = forms.CharField(initial = '', required = False)
    City        = forms.CharField(initial = '', required = False)
    State       = forms.CharField(initial = '', required = False)
    Date        = forms.DateField(initial = '', required = False)
    Death       = forms.CharField(initial = '', required = False)
    Report      = forms.CharField(initial = '', required = False)

class GetFrom2(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    
    