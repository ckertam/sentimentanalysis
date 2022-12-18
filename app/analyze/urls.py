from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path("", views.AnalyzeTweetsAPIView.as_view(), name="get tables and send email"),
]