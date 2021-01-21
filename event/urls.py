from django.urls import path

from event import views

urlpatterns = [
    path('', views.index, name='home'),
    path('event_list/', views.EventList.as_view(), name='event_list'),
    path('<int:pk>/', views.EventDetail.as_view(), name='event_detail'),
]