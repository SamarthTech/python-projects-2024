from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'seller'

urlpatterns=[
    url(r"^seller_form/$", views.seller_form.as_view(), name="seller_form"),
]
