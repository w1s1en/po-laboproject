from django.urls import path
from .views import * #importuj wszystko
app_name='zawody'
urlpatterns = [
        path('zawodnik',Playerviev.as_view(),name='type-list')
    ]