from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^purchases/$',
        view=views.ListPurchasesView.as_view(),
        name='purchases-list'),
]
