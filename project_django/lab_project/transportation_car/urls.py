from django.urls import path

from .views import *

urlpatterns = [
    path('<int:ile>', index, name='home'),
    path('', main, name='main'),
    path('transportation/<int:id>', transportationId, name='transportation'),
    path('delete_transportation/<int:id>', deleteTransportId, name='delete_transport'),
    path('edit_transportation/<int:id>', editTransportId, name='edit_transport'),
    path('transport/<int:pk>', TransportAPI.as_view()),
    path('getTransportions/', getTransportations.as_view(), name='getTransportantions'),
    path('createTransportations/', create_transportations, name='createTransportations'),
    # path('<int:id>', getTransportationId.as_view(), name='getTransportations'),
    path('ordered/<int:user_id>/', getTransportationId.as_view(), name='getTransportations'),
    # path('my_order/<int:user_id>/<int:ile>/<int:year_1>/<int:mounth_1>/<int:day_1>/<int:year_2>/<int:mounth_2>/<int:day_2>/', getUserOrder, name='myOrder'),
    path('my_order/<int:user_id>/<int:ile>/<str:date1>/<str:date2>/', getUserOrder, name='myOrder'),
]