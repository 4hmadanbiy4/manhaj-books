from django.forms import ModelForm
from main.models import Reservation
from django.utils.html import strip_tags

# Reservation
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ["pemesan", "buku", "pcs"]
    def clean_pemesan(self):
        pemesan = self.cleaned_data["pemesan"]
        return strip_tags(pemesan)
