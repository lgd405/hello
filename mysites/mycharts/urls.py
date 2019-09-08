from django.urls import path,include
from . import views as mcv

urlpatterns = [
    path('', mcv.home),
    path('bar', mcv.bar),
    path('bar_chart_display_delay', mcv.bar_chart_display_delay),
]


