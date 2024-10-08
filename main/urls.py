from django.urls import path
from main.views import show_main, create_reservation_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, edit_pesanan, delete_pesanan, add_res_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-reservation-entry', create_reservation_entry, name='create_reservation_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-pesanan/<uuid:id>', edit_pesanan, name='edit_pesanan'),
    path('delete/<uuid:id>', delete_pesanan, name='delete_pesanan'),
    path('create-res-entry-ajax', add_res_entry_ajax, name='add_res_entry_ajax'),
]