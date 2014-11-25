from django.views import generic
from models import Temps

# Create your views here.


class MainView(generic.ListView):
    template_name = 'temp_display/index.html'
    context_object_name = 'last_hour_temperature'

    def get_queryset(self):
        temporal_result = Temps.objects.order_by('-time_stamp')[:13]
        return temporal_result[::-1]

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['current_temperature'] = Temps.objects.raw("SELECT time_stamp AS time_stamp, temperature AS temperature FROM temps.temp_display_temps ORDER BY time_stamp DESC LIMIT 1")
        context['lowest_24_hours'] = Temps.objects.raw("SELECT time_stamp AS time_stamp, (temperature) AS temperature FROM temps.temp_display_temps  WHERE time_stamp >= NOW() - INTERVAL 24 HOUR  ORDER BY temperature ASC LIMIT 1")
        context['highest_24_hours'] = Temps.objects.raw("SELECT time_stamp AS time_stamp, (temperature) AS temperature FROM temps.temp_display_temps  WHERE time_stamp >= NOW() - INTERVAL 24 HOUR ORDER BY temperature DESC LIMIT 1")
        context['last_24_hours'] = Temps.objects.raw("SELECT CONCAT(date(time_stamp), ' ', HOUR(time_stamp), ':00:00') AS time_stamp, AVG(temperature) AS temperature FROM temps.temp_display_temps WHERE time_stamp >= NOW() - INTERVAL 24 HOUR GROUP BY date(time_stamp), HOUR(time_stamp)")
        context['last_1_week'] = Temps.objects.raw("SELECT CONCAT(DAY(time_stamp),'-',DAY(time_stamp)) AS time_stamp, AVG(temperature) AS temperature FROM temps.temp_display_temps WHERE time_stamp >= NOW() - INTERVAL 7 DAY GROUP BY DAY(time_stamp)")
        context['last_1_month'] = Temps.objects.raw("SELECT CONCAT(DAY(time_stamp),'-',MONTH(time_stamp)) AS time_stamp, AVG(temperature) AS temperature FROM temps.temp_display_temps WHERE time_stamp >= NOW() - INTERVAL 30 DAY GROUP BY DAY(time_stamp)")
        context['last_3_month'] = Temps.objects.raw("SELECT CONCAT(WEEK(time_stamp),'-',YEAR(time_stamp)) AS time_stamp, AVG(temperature) AS temperature FROM temps.temp_display_temps WHERE time_stamp >= NOW() - INTERVAL 3 MONTH GROUP BY WEEK(time_stamp)")
        context['last_12_month'] = Temps.objects.raw("SELECT CONCAT(MONTH(time_stamp),'-',YEAR(time_stamp)) AS time_stamp, AVG(temperature) AS temperature FROM temps.temp_display_temps WHERE time_stamp >= NOW() - INTERVAL 12 MONTH GROUP BY YEAR(time_stamp)")
        return context
