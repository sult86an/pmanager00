from django.views import generic
from django.views.generic import View
from .models import Leaders
from initiatives.models import Initi,  Reports
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings
from global_login_required import login_not_required



@login_not_required
def userindex(request):
    return render(request, 'pmanager/index.html')


@login_not_required
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('pmanager:home'))
    else:
        return render(request, 'pmanager/index.html', {})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(userindex))


class IndexView(generic.ListView):
    template_name = 'pmanager/home.html'
    context_object_name = 'mub'

    def get_queryset(self):
        user = self.request.user
        return Initi.objects.filter(leader__name=user)


# #class IndexView(generic.ListView):
#    # template_name = 'pmanager/home.html'
#     context_object_name = 'mub'
#
#     def get_queryset(self):
#         #return Initi.objects.filter(leader__id=1)
#         return Initi.mub_name
class LeadersView(generic.ListView):
    template_name = 'pmanager/leaders.html'
    context_object_name = 'leaders'

    def get_queryset(self):
        return Leaders.objects.all()


class InitiativesView(generic.ListView):
    template_name = 'pmanager/all_initiatives.html'
    context_object_name = 'detail'

    def get_queryset(self):
        user = self.request.user
        return Initi.objects.filter(leader_name=user)


class WeekReportView(generic.DetailView):
    template_name = 'pmanager/weekly_report.html'
    model = Initi


class ListWeek(generic.ListView):
    template_name = 'pmanager/weekly_report.html'
    context_object_name = 'report'

    def get_queryset(self):
        return Reports.objects.all()


class DetailView(generic.DetailView):
    template_name = 'pmanager/detail.html'
    model = Reports

    def get_queryset(self):
        return Reports.objects.all()


class EnqueryView(View):
    template_name = 'pmanager/enquiry.html'

    def get(self, request):
        return render(request, self.template_name)


