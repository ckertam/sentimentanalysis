from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path("simplesimulation/", views.AnalyzeTweetsSimpleSimulationAPIView.as_view(), name="get tables and send email"),
    path("complexsimulation/", views.AnalyzeTweetsComplexSimulationAPIView.as_view(), name="get tables and send email"),
    path("", views.AnalyzeTweetsAPIView.as_view(), name="get tables and send email"),
]