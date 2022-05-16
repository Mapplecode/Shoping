from django.urls import path
from django.views.generic import RedirectView

from . import views
app_name = 'administration'
urlpatterns = [
    path('', RedirectView.as_view(url='dashboard/')),
]
