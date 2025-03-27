from django.urls import path
from .views import (
    workers, unskilled, skilled, hire, 
    worker_offers, offer_action, hirer_offers
)

urlpatterns = [
    path('', workers, name='workers'),
    path('unskilled/', unskilled, name='unskilled'),
    path('skilled/', skilled, name='skilled'),
    path('hire/<int:user_id>/', hire, name='hire'),
    path('offers/', worker_offers, name='worker_offers'),
    path('offer-action/<int:offer_id>/', offer_action, name='offer_action'),
    path('hirer-offers/', hirer_offers, name='hirer_offers'),
]
