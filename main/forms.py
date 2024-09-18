from django.forms import ModelForm
from main.models import Reservation

# Reservation
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ["pemesan", "buku", "pcs"]
