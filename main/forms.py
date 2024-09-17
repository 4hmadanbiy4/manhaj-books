from django.forms import ModelForm
from main.models import Reservation
# Reservation

# Books
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ["pemesan", "buku", "pcs"]
# class ReservationForm(ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ['customer', 'book', 'pcs']
