from django.urls import path
from . import pviews
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

app_name = 'pmanager'
urlpatterns = [
    # /initiatives/

    path('user_login/', pviews.user_login, name='user'),
    path('logout/', pviews.user_logout, name='logout'),
    path('home/', pviews.IndexView.as_view(), name='home'),
    path('initiative/', pviews.InitiativesView.as_view(), name='initiative'),
    path('leaders/', pviews.LeadersView.as_view(), name='leaders'),
    path('messages/', pviews.EnqueryView.as_view(), name='messages'),
    path('reports/<int:pk>/', pviews.WeekReportView.as_view(), name='reports'),
    path('reports/<int:pk>/details/', pviews.DetailView.as_view(), name='details'),
    path('reports/<int:pk>/details/', pviews.DetailView.as_view(), name='details'),


]

