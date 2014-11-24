import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from models import Temps

# Create your views here.


class Last5Reads(generic.ListView):
    template_name = 'temp_display/index.html'
    context_object_name = 'latest_temps_list'

    def get_queryset(self):
        temporal_result = Temps.objects.order_by('-time_stamp')[:5]
        return temporal_result[::-1]


class Last24Hours(generic.ListView):
    template_name = 'temp_display/daily_detail.html'
    context_object_name = 'last_24h_temps_list'

    def get_queryset(self):
        temporal_result = Temps.objects.filter(time_stamp__gte=(datetime.datetime.today() - datetime.timedelta(hours=24)))
        print(type(temporal_result))
        return temporal_result