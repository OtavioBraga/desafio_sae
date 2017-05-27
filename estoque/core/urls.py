from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^purchases/$',
        view=views.ListPurchasesView.as_view(),
        name='purchases-list'),

    url(regex=r'^purchases/new/$',
        kwargs={'pk': 3},
        view=views.NewPurchaseView.as_view(),
        name='new-purchase'),

    url(regex=r'^purchases/new/(?P<pk>[^/]+)$',
        view=views.NewPurchaseView.as_view(),
        name='new-purchase'),

    url(regex=r'^products/$',
        view=views.ListProductsView.as_view(),
        name='products-list'),

    url(regex=r'^products/new/$',
        view=views.NewProductView.as_view(),
        name='new-product'),

    url(regex=r'^tasks/$',
        view=views.TasksView.as_view(),
        name='tasks'),

]
