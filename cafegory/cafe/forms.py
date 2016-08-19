from django import forms
from cafe.models import Cafe
from cafe.widgets import GoogleMapPointWidget


class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'is_24', 'is_smoke','is_wifi','is_plug','is_parking','latlng','image',"address",
        "location","end_time","tel",]
        widgets = {
            'latlng': GoogleMapPointWidget,
        }




