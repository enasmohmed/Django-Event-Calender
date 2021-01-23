from django.urls import path

from eventcalender import views
from eventcalender.views import EventListView, EventCreateView, EventDetailView, EventUpdateView, EventDeleteView, \
     EventMemberDeleteView

app_name = 'eventcalender'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', EventListView.as_view(), name='list'),
    path('list/<int:pk>/', EventDetailView.as_view(), name='detail'),
    path('create/', EventCreateView.as_view(), name='create'),
    path('add_member/<int:event_id>', views.add_eventmember, name='add_member'),
    path('update/<int:pk>/', EventUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', EventDeleteView.as_view(), name='delete'),
    path('add_member/<int:event_id>/remove', EventMemberDeleteView.as_view(), name="remove_event"),
]