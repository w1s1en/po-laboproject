from django.urls import path
from .views import * #importuj wszystko
app_name='zawody'
urlpatterns = [
        path('',form_view),
        path('zawodnik',Playerviev.as_view(),name='type-list'),
        path('zawody',Competitionviev.as_view(),name='type-list'),
        path('rower',Bikeviev.as_view(),name='type-list'),
        path('<slug:slug>/',PlayerDetail.as_view(),name='type-list'),
    ]