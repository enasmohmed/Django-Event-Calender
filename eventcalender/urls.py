from django.urls import path

from eventcalender import views
from eventcalender.views import EventListView, EventCreateView, EventUpdateView

app_name = 'eventcalender'

urlpatterns = [
    path('', views.home, name='home'),
    path('event_list/', EventListView.as_view(), name='list'),
    path('event_list/<int:event_id>/', views.event_details, name='detail'),
    path('create/', EventCreateView.as_view(), name='create'),
    path('add_member/<int:event_id>', views.add_eventmember, name='add_member'),
    path('update/<int:pk>/', EventUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', EventDeleteView.as_view(), name="remove_event"),
    path('event/<int:pk>/remove', views.EventMemberDeleteView.as_view(), name="remove_event"),

]